from pyspark.sql import SparkSession
from pyspark.sql.functions import col, datediff, current_date, to_date, when

# Initialize Spark Session
spark = SparkSession.builder.appName("CustomerDataProcessing").getOrCreate()

# Function to process data from a file
def process_customer_data(file_path):
    # Read the data into a DataFrame
    df = spark.read.option("delimiter", "|").csv(file_path, header=True, inferSchema=True)

    # Filter out header records (Record_Type = 'H')
    df_details = df.filter(col("Record_Type") == "D")

    # Parse dates
    df_details = df_details.withColumn("Open_Date", to_date(col("Open_Date"), "yyyyMMdd")) \
                           .withColumn("Last_Consulted_Date", to_date(col("Last_Consulted_Date"), "yyyyMMdd")) \
                           .withColumn("DOB", to_date(col("DOB"), "yyyyMMdd"))

    # Add derived columns: Age and Days Since Last Consulted
    df_details = df_details.withColumn("Age", (datediff(current_date(), col("DOB")) / 365).cast("int"))
    df_details = df_details.withColumn("Days_Since_Last_Consulted", datediff(current_date(), col("Last_Consulted_Date")))

    # Validate: Ensure no future consultation dates
    df_details = df_details.withColumn("Is_Valid_Consultation", when(col("Last_Consulted_Date") <= current_date(), True).otherwise(False))

    # Filter out invalid records (future consultations)
    df_details = df_details.filter(col("Is_Valid_Consultation") == True)

    # Now, process data by country
    countries = df_details.select("Country").distinct().collect()

    for country_row in countries:
        country = country_row["Country"]
        country_df = df_details.filter(col("Country") == country)
        
        # If there are existing records for the country, merge them based on the latest consultation date
        # Assuming you are working with a SQL-based system (could be Spark SQL, PostgreSQL, etc.)

        # Create or update the corresponding country-specific table (e.g., Table_USA, Table_IND)
        country_df.createOrReplaceTempView(f"temp_{country}")
        
        spark.sql(f"""
            INSERT INTO Table_{country}
            SELECT Customer_Name, Customer_Id, Open_Date, Last_Consulted_Date, Vaccination_Id, 
                   Dr_Name, State, Country, DOB, Is_Active, Age, Days_Since_Last_Consulted
            FROM temp_{country}
            WHERE Last_Consulted_Date = (SELECT MAX(Last_Consulted_Date) FROM temp_{country} WHERE Customer_Id = temp_{country}.Customer_Id)
        """)

    return "Data Processing Completed."

# Example of processing a file
process_customer_data("path_to_data_file.csv")

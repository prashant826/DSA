from pyspark.sql import SparkSession
from pyspark.sql.functions import col, datediff, current_date, year
import datetime

spark = SparkSession.builder \
    .appName("Hospital Customer Data Processing") \
    .getOrCreate()

def calculate_age(dob):
    current_year = datetime.datetime.now().year
    return current_year - dob.year

def days_since_last_consulted(last_consulted_date):
    return (datetime.datetime.now() - last_consulted_date).days

def process_customer_data(df):
    df = df.withColumn("DOB", col("DOB").cast("date"))
    df = df.withColumn("Last_Consulted_Date", col("Last_Consulted_Date").cast("date"))

    # Calculate Age
    df = df.withColumn("Age", calculate_age(col("DOB")))

    # Calculate Days Since Last Consulted
    df = df.withColumn("Days_Since_Last_Consulted", datediff(current_date(), col("Last_Consulted_Date")))

    # Flag if 'Days_Since_Last_Consulted' > 30
    df = df.withColumn("Flag_Consulted_Over_30_Days", 
                       (col("Days_Since_Last_Consulted") > 30).cast("int"))

    return df


def load_and_process_file(file_path):
    # Read the data into a DataFrame
    df = spark.read.csv(file_path, header=True, inferSchema=True)

    # Filter only 'D' records (Customer details)
    df = df.filter(col("Record_Type") == "D")
    
    # Process the data (age calculation, days since last consultation, etc.)
    df_processed = process_customer_data(df)

    return df_processed


def insert_data_to_country_table(df, country):
    # Filter data by country
    df_country = df.filter(col("Country") == country)

    # Write to the country-specific table (using append mode)
    df_country.write \
        .mode("append") \
        .jdbc(url="jdbc:mysql://your-database-url", 
              table=f"Table_{country}", 
              properties={"user": "username", "password": "password"})


def main(file_path):
    # Load and process the data
    df = load_and_process_file(file_path)

    # Insert data into country-specific tables
    countries = df.select("Country").distinct().rdd.flatMap(lambda x: x).collect()
    for country in countries:
        insert_data_to_country_table(df, country)

# Execute the process for the provided file
main("path_to_your_data_file.csv")
import os
import pandas as pd
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load the dataset
csv_file = "../dataset/data.csv"
df = pd.read_csv(csv_file)

# Database connection parameters
db_params = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": int(os.getenv("DB_PORT"))
}

try:
    # Connect to MySQL
    conn = mysql.connector.connect(**db_params)
    cursor = conn.cursor()
    print("Connected to MySQL")

    # Check if stored procedure exists
    cursor.execute("SHOW PROCEDURE STATUS WHERE Name = 'InsertPatient';")
    if cursor.fetchone() is None:
        print("Stored Procedure 'InsertPatient' not found!")

    # SQL queries
    insert_patient = "CALL InsertPatient(%s, %s);"

    insert_tumor_mean = """
    INSERT INTO tumor_mean (
        id, radius_mean, texture_mean, perimeter_mean, area_mean, 
        smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, 
        symmetry_mean, fractal_dimension_mean
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    insert_tumor_se = """
    INSERT INTO tumor_se (
        id, radius_se, texture_se, perimeter_se, area_se, 
        smoothness_se, compactness_se, concavity_se, concave_points_se, 
        symmetry_se, fractal_dimension_se
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    insert_tumor_worst = """
    INSERT INTO tumor_worst (
        id, radius_worst, texture_worst, perimeter_worst, area_worst, 
        smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, 
        symmetry_worst, fractal_dimension_worst
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    # Insert data into MySQL with error handling
    for index, row in df.iterrows():
        patient_id = str(row["id"])
        print(f"🔹 Inserting row {index + 1} (ID: {patient_id})...")

        try:
            cursor.execute(insert_patient, (patient_id, row["diagnosis"]))
            cursor.execute(insert_tumor_mean, (
                patient_id, row["radius_mean"], row["texture_mean"], row["perimeter_mean"], row["area_mean"],
                row["smoothness_mean"], row["compactness_mean"], row["concavity_mean"], row["concave points_mean"],
                row["symmetry_mean"], row["fractal_dimension_mean"]
            ))
            cursor.execute(insert_tumor_se, (
                patient_id, row["radius_se"], row["texture_se"], row["perimeter_se"], row["area_se"],
                row["smoothness_se"], row["compactness_se"], row["concavity_se"], row["concave points_se"],
                row["symmetry_se"], row["fractal_dimension_se"]
            ))
            cursor.execute(insert_tumor_worst, (
                patient_id, row["radius_worst"], row["texture_worst"], row["perimeter_worst"], row["area_worst"],
                row["smoothness_worst"], row["compactness_worst"], row["concavity_worst"], row["concave points_worst"],
                row["symmetry_worst"], row["fractal_dimension_worst"]
            ))

        except Error as e:
            print(f"Error inserting row {index + 1} (ID: {patient_id}): {e}")

    # Commit changes
    conn.commit()
    print("Data successfully inserted into Database.")

except Error as e:
    print(f"MySQL Connection Error: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    print("MySQL connection closed.")

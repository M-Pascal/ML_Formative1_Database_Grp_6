# Breast Cancer Database Setup and Prediction System

## Overview
This project involves designing and implementing a database system for breast cancer data, creating API endpoints for CRUD operations, and developing a machine learning prediction system. The database is implemented using both MySQL (relational) and MongoDB (NoSQL). The API is built using FastAPI, and the prediction system uses a pre-trained machine learning model.

## Database Design and Implementation

### Entity Relationship Diagram (ERD)
You can view the Entity Relationship Diagram (ERD) for the database schema [here.](https://github.com/M-Pascal/ML_Formative1_Database_Grp_6/blob/main/ERD_diagram/ERD_diagram.jpg).

### Step 1: Running the SQL Schema
To set up the MySQL database, run the `sqlSchema.sql` file. This will create the required tables and the database.

```bash
mysql -u root -p < sqlSchema.sql
```

### Database Schema
The database schema consists of the following tables:
- **Patients**: Stores patient details (e.g., patient_id, age, gender, diagnosis).
- **Tumor_Data**: Stores tumor characteristics (e.g., radius_mean, texture_mean, perimeter_mean).
- **Diagnosis_Logs**: Logs changes to patient diagnoses (e.g., log_id, patient_id, old_diagnosis, new_diagnosis, log_timestamp).

### Stored Procedures and Triggers
- **Stored Procedure**: `InsertPatient` - Automates the insertion of patient data.
- **Trigger**: `LogDiagnosisChange` - Logs changes to the diagnosis column in the Patients table.

### Step 2: Data Cleaning
Before inserting data into the database, the following data cleaning steps are applied:
- **Column Names**: Renamed for consistency (e.g., `concave points_mean` → `concave_points_mean`).
- **Missing Values**: Filled with the column mean.
- **Gender Conversion**: Converted to binary values (1 for Male, 0 for Female).
- **Diagnosis Conversion**: Converted to binary values (1 for Malignant, 0 for Benign).

### Step 3: MySQL Setup
Log in to MySQL as the root user:

```bash
mysql -u root -p
```

Check if the database and tables were created successfully:

```sql
SHOW DATABASES;
USE breast_cancer_db;
SHOW TABLES;
```

### Step 4: MongoDB Setup
The MongoDB database used is `breast_cancer_db`, which contains the following collections:
- **patients**: Stores patient details (e.g., age, gender).
- **tumor_data**: Stores tumor characteristics (e.g., radius_mean, texture_mean).
- **diagnosis_logs**: Logs changes to patient diagnoses.

#### Inspecting Collections
You can inspect the collections using MongoDB Compass or the MongoDB shell:

```bash
show dbs
use breast_cancer_db
show collections
```

#### Data Insertion
Data is inserted into MongoDB using `insert_many()`:

```python
patients_collection.insert_many(patients_data_dict)
```

## The API - Task 2
This is a FastAPI-based application for managing patient data and tumor characteristics. It provides endpoints for creating, reading, updating, and deleting records.

### API Repository
- GitHub: [https://github.com/M-Pascal/ML_Formative1_Database_Grp_6.git](https://github.com/M-Pascal/ML_Formative1_Database_Grp_6.git)
- Remote API Link: [https://ml-databaseapi-peer-grp-6.onrender.com](https://ml-databaseapi-peer-grp-6.onrender.com)

### Features
#### Patient Management:
- Create, read, update, and delete patient records.
- Store patient age, gender, and diagnosis.

#### Tumor Data Management:
- Create, read, update, and delete tumor data records.
- Store tumor characteristics (e.g., radius_mean, texture_mean).

#### Diagnosis Logs:
- Retrieve logs of changes to patient diagnoses.

### Endpoints
#### Patient Endpoints
- `POST /patients/`: Create a new patient.
- `GET /patients/`: Retrieve all patients.
- `GET /patients/{patient_id}`: Retrieve a specific patient by ID.
- `PUT /patients/{patient_id}`: Update a patient by ID.
- `DELETE /patients/{patient_id}`: Delete a patient by ID.

#### Tumor Data Endpoints
- `POST /tumor_data/`: Create new tumor data.
- `GET /tumor_data/`: Retrieve all tumor data.
- `GET /tumor_data/{tumor_id}`: Retrieve specific tumor data by ID.
- `PUT /tumor_data/{tumor_id}`: Update tumor data by ID.
- `DELETE /tumor_data/{tumor_id}`: Delete tumor data by ID.

#### Diagnosis Logs Endpoints
- `GET /diagnosis_logs/`: Retrieve all diagnosis logs.

## Breast Cancer Prediction System - Task 3
This system trains a machine learning model to predict breast cancer diagnosis (malignant or benign) and offers multiple ways to use it:
- **Direct Prediction**: Use the model directly with CSV data.
- **API-Based Prediction**: Fetch data from the API and make predictions.
- **Test Server**: For demonstrations without a database.

### Prediction Endpoints
- `POST /predict`: Predict diagnosis based on input data.
- `GET /predict-latest`: Predict diagnosis for the latest patient in the database.

## Contributions
- **Task 1 (Database Design and SQL Implementation & MongoDB Implementation)**: Pascal Mugisha
- **Task 2 (API Development)**: Jean Chrisostome Dufitumukiza
- **Task 3 (Fetch and Prediction)**: Ruth Ishimwe

## How to Run the Project
### Clone the repository:
```bash
git clone https://github.com/M-Pascal/ML_Formative1_Database_Grp_6.git
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Run the FastAPI application:
```bash
uvicorn main:app --reload
```

### Access the API documentation at:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

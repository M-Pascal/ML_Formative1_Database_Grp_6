-- Drop Tables if they exist
DROP TABLE IF EXISTS tumor_mean;
DROP TABLE IF EXISTS tumor_se;
DROP TABLE IF EXISTS tumor_worst;
DROP TABLE IF EXISTS patients;

-- Create Patients Table
CREATE TABLE IF NOT EXISTS patients (
    id VARCHAR(50) PRIMARY KEY,
    diagnosis VARCHAR(10) NOT NULL
);

-- Create Tumor Mean Table
CREATE TABLE IF NOT EXISTS tumor_mean (
    id VARCHAR(50),
    radius_mean FLOAT, texture_mean FLOAT, perimeter_mean FLOAT, area_mean FLOAT,
    smoothness_mean FLOAT, compactness_mean FLOAT, concavity_mean FLOAT, concave_points_mean FLOAT,
    symmetry_mean FLOAT, fractal_dimension_mean FLOAT,
    FOREIGN KEY (id) REFERENCES patients(id) ON DELETE CASCADE
);

-- Create Tumor SE Table
CREATE TABLE IF NOT EXISTS tumor_se (
    id VARCHAR(50),
    radius_se FLOAT, texture_se FLOAT, perimeter_se FLOAT, area_se FLOAT,
    smoothness_se FLOAT, compactness_se FLOAT, concavity_se FLOAT, concave_points_se FLOAT,
    symmetry_se FLOAT, fractal_dimension_se FLOAT,
    FOREIGN KEY (id) REFERENCES patients(id) ON DELETE CASCADE
);

-- Create Tumor Worst Table
CREATE TABLE IF NOT EXISTS tumor_worst (
    id VARCHAR(50),
    radius_worst FLOAT, texture_worst FLOAT, perimeter_worst FLOAT, area_worst FLOAT,
    smoothness_worst FLOAT, compactness_worst FLOAT, concavity_worst FLOAT, concave_points_worst FLOAT,
    symmetry_worst FLOAT, fractal_dimension_worst FLOAT,
    FOREIGN KEY (id) REFERENCES patients(id) ON DELETE CASCADE
);

-- Drop procedures if they already exist to prevent duplication errors
DROP PROCEDURE IF EXISTS InsertOrUpdatePatient;
DROP PROCEDURE IF EXISTS UpdateDiagnosis;

-- Create Stored Procedure for inserting/updating Patients
DELIMITER //
CREATE PROCEDURE InsertOrUpdatePatient(IN p_id VARCHAR(50), IN p_diagnosis VARCHAR(10))
BEGIN
    INSERT INTO patients (id, diagnosis)
    VALUES (p_id, p_diagnosis)
    ON DUPLICATE KEY UPDATE diagnosis = p_diagnosis;
END;
//
DELIMITER ;

-- Create Stored Procedure to Update Diagnosis
DELIMITER //
CREATE PROCEDURE UpdateDiagnosis(IN p_id VARCHAR(50), IN new_diagnosis VARCHAR(10))
BEGIN
    -- Update the diagnosis only if the patient exists
    UPDATE patients 
    SET diagnosis = new_diagnosis 
    WHERE id = p_id;
END;
//
DELIMITER ;

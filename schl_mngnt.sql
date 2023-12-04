-- Software Engineering (SE)
-- Data Science
-- Cybersecurity (CS)
-- Product Design (UI/UX)
-- DevOps Engineering
-- Data Visualization with Python

-- C R U D

SHOW TABLES;

-- C SE --
CREATE TABLE software_engineering_students(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    reg_id VARCHAR(100),
    major VARCHAR(100),
    languages VARCHAR(100),
    status VARCHAR(100),
    work_availability VARCHAR(100)
);

-- add column --
ALTER TABLE software_engineering_students
ADD date_started DATE;

DESCRIBE software_engineering_students;

-- C CS --
CREATE TABLE cybersecurity_students(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    reg_id VARCHAR(100),
    major VARCHAR(100),
    languages VARCHAR(100),
    status VARCHAR(100),
    work_availability VARCHAR(100),
    date_started DATE
);

-- C UI/UX --
CREATE TABLE ui_ux_students(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    reg_id VARCHAR(100),
    major VARCHAR(100),
    languages VARCHAR(100),
    status VARCHAR(100),
    work_availability VARCHAR(100),
    date_started DATE
);

SHOW TABLES;


-- INSERT (I)
-- I SE --
INSERT INTO software_engineering_students VALUES
(1, "Nathan Kiprotich", "nathan.kiprotich@student.moringaschool.com", "G301", "FrontEnd", "REACT", "Active", "Available", "2023-09-04"),
(2, "Beatrice Mwenje", "beatrice.mwenje@student.moringaschool.com", "G302", "FullStack", "PHP", "Active", "Available", "2023-09-04"),
(3, "Kibet Nathan", "kibet.nathan@student.moringaschool.com", "G303", "BackEnd", "SQL", "Active", "Available", "2023-09-04"),
(4, "Linder Opondo", "linder.opondo@student.moringaschool.com", "G304", "FullStack", "PYTHON", "Active", "Available", "2023-09-04"),
(5, "Gad Ongoro", "gad.ongoro@student.moringaschool.com", "G305", "FullStack", "C", "Active", "Available", "2023-09-04"),
(6, "Samuel Otieno", "samuel.otieno@student.moringaschool.com", "G306", "FrontEnd", "REACT", "Active", "Available", "2023-09-04")
;

SELECT * FROM software_engineering_students;

DELETE FROM software_engineering_students;
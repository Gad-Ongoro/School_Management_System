-- TABLES --
-- Software Engineering (SE)
-- Data Science
-- Cybersecurity (CS)
-- Product Design (UI/UX)
-- DevOps Engineering
-- Data Visualization with Python
-- Supervisor (sup)
-- Courses (crs)

-- ~ C R U D

-- CREATE DATABASE school_management_system;

-- USE DATABASE school_management_system;

SHOW TABLES;

-- C crs --
CREATE TABLE courses(
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    sup_id INT,
    duration VARCHAR(50)
);
DESCRIBE courses;

-- C sup --
CREATE TABLE supervisors(
    sup_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    major VARCHAR(50)
);

-- C SE --
CREATE TABLE software_engineering_students(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    reg_id VARCHAR(100),
    major VARCHAR(100),
    languages VARCHAR(100),
    status VARCHAR(100),
    work_availability VARCHAR(100),
    sup_id INT
);

-- add column --
ALTER TABLE software_engineering_students ADD date_started DATE;

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
    date_started DATE,
    sup_id INT
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
    date_started DATE,
    sup_id INT
);

SHOW TABLES;

-- ALTER -- 
ALTER TABLE courses ADD FOREIGN KEY (sup_id) REFERENCES supervisors(sup_id) ON DELETE SET NULL;
ALTER TABLE cybersecurity_students ADD FOREIGN KEY (sup_id) REFERENCES supervisors (sup_id) ON DELETE SET NULL;
ALTER TABLE software_engineering_students ADD FOREIGN KEY (sup_id) REFERENCES supervisors (sup_id) ON DELETE SET NULL;
ALTER TABLE ui_ux_students ADD FOREIGN KEY (sup_id) REFERENCES supervisors (sup_id) ON DELETE SET NULL;


-- INSERT (I)
-- I sup --
INSERT INTO supervisors
VALUES
(1001, "Abdi Rashid", "abdulrashid@gmail.com", "FrontEnd"),
(1002, "Sean Newton", "seannewton@gmail.com", "BackEnd"),
(1003, "Khalifa Muyideen", "kmuyideen@outlook.com", "FullStack")
;
SELECT * FROM supervisors;

-- I SE --
DESCRIBE software_engineering_students;
INSERT INTO software_engineering_students VALUES
(1, "Nathan Kiprotich", "nathan.kiprotich@student.moringaschool.com", "G301", "FrontEnd", "REACT", "Active", "Available", 1001, "2023-09-04"),
(2, "Beatrice Mwenje", "beatrice.mwenje@student.moringaschool.com", "G302", "FullStack", "PHP", "Active", "Available", 1003, "2023-09-04"),
(3, "Kibet Nathan", "kibet.nathan@student.moringaschool.com", "G303", "BackEnd", "SQL", "Active", "Available", 1002, "2023-09-04"),
(4, "Linder Opondo", "linder.opondo@student.moringaschool.com", "G304", "FullStack", "PYTHON", "Active", "Available", 1003, "2023-09-04"),
(5, "Gad Ongoro", "gad.ongoro@student.moringaschool.com", "G305", "FullStack", "C", "Active", "Available", 1003, "2023-09-04"),
(6, "Samuel Otieno", "samuel.otieno@student.moringaschool.com", "G306", "FrontEnd", "REACT", "Active", "Available", 1001, "2023-09-04")
;

-- R SE --
SELECT * FROM software_engineering_students;

SELECT * FROM software_engineering_students
WHERE major = "FrontEnd"
ORDER BY id DESC
LIMIT 5;

-- U SE --
UPDATE software_engineering_students
SET major = "FE"
WHERE major = "FrontEnd";

SELECT * FROM software_engineering_students;

-- D SE --
DELETE FROM software_engineering_students WHERE id = 5;

DELETE FROM software_engineering_students;

SELECT * FROM software_engineering_students;

-- I CS --
INSERT INTO cybersecurity_students VALUES
(1, "Nathan Kiprotich", "nathan.kiprotich@student.moringaschool.com", "G301", "FrontEnd", "REACT", "Active", "Available", "2023-09-04", 1001),
(2, "Beatrice Mwenje", "beatrice.mwenje@student.moringaschool.com", "G302", "FullStack", "PHP", "Active", "Available", "2023-09-04", 1003),
(3, "Kibet Nathan", "kibet.nathan@student.moringaschool.com", "G303", "BackEnd", "SQL", "Active", "Available", "2023-09-04", 1002),
(4, "Linder Opondo", "linder.opondo@student.moringaschool.com", "G304", "FullStack", "PYTHON", "Active", "Available", "2023-09-04", 1003),
(5, "Gad Ongoro", "gad.ongoro@student.moringaschool.com", "G305", "FullStack", "C", "Active", "Available", "2023-09-04", 1003),
(6, "Samuel Otieno", "samuel.otieno@student.moringaschool.com", "G306", "FrontEnd", "REACT", "Active", "Available", "2023-09-04", 1001)
;
SELECT * FROM cybersecurity_students;

-- I UI/UX --

-- RESET DB TO DEFAULT -- 
SHOW TABLES;

DROP TABLE courses;

DROP TABLE cybersecurity_students;

DROP TABLE software_engineering_students;

DROP TABLE ui_ux_students;

DROP TABLE supervisors;
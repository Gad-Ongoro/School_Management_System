-- TABLES --
-- Courses (courses)
-- Phases (phases)
-- Students (stud)
-- Supervisor (sup)
-- ~ Software Engineering (Phase-0)
-- ~ Product Design (Phase-1)
-- ~ Data Science (Phase-2)
-- ~ Data Visualization with Python (Phase-3)
-- ~ DevOps Engineering (Phase-4)
-- ~ Cybersecurity (Phase-5)
-- C R U D
-- CREATE DATABASE school_management_system;
-- USE DATABASE school_management_system;
SHOW TABLES;
-- C courses --
CREATE TABLE courses(
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    sup_id INT,
    duration VARCHAR(50)
);
DESCRIBE courses;
CREATE TABLE phases(
    phase_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    sup_id INT
);
-- C sup --
CREATE TABLE supervisors(
    sup_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    major VARCHAR(50)
);
DESCRIBE supervisors;
-- C stud --
CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    reg_id VARCHAR(100),
    course_id INT,
    status VARCHAR(100),
    phase INT,
    work_availability VARCHAR(100),
    sup_id INT
);
DESCRIBE students;
-- add column --
ALTER TABLE students
ADD date_started DATE;
DESCRIBE students;
SHOW TABLES;
-- ALTER -- 
ALTER TABLE courses
ADD FOREIGN KEY (sup_id) REFERENCES supervisors(sup_id) ON DELETE
SET NULL;
ALTER TABLE students
ADD FOREIGN KEY (sup_id) REFERENCES supervisors (sup_id) ON DELETE
SET NULL;
ALTER TABLE students
ADD FOREIGN KEY (phase) REFERENCES phases (phase_id) ON DELETE
SET NULL;
-- INSERT (I)
-- I phases --
DESCRIBE phases;
INSERT INTO phases
VALUES (1, "Phase-0", 1000),
    (2, "Phase-1", 1001),
    (3, "Phase-2", 1002),
    (4, "Phase-3", 1003),
    (5, "Phase-4", 1004),
    (6, "Phase-5", 1005);
-- I sup --
INSERT INTO supervisors
VALUES (
        1000,
        "Khalifa Muyideen",
        "kmuyideen@outlook.com",
        "FullStack"
    ),
    (
        1001,
        "Abdi Rashid",
        "abdulrashid@gmail.com",
        "FrontEnd"
    ),
    (
        1002,
        "Sean Newton",
        "seannewton@gmail.com",
        "backend"
    ),
    (
        1003,
        "David Kingston",
        "davidkings@gmail.com",
        "Data Science"
    ),
    (
        1004,
        "Emma Maart",
        "emmamaart@outlook.com",
        "DevOps Engineering"
    ),
    (
        1005,
        "Wales Wallace",
        "wallace1@yahoo.com",
        "backend"
    );
SELECT *
FROM supervisors;
DELETE FROM supervisors
WHERE sup_id = 1003;
-- I stud --
DESCRIBE students;
INSERT INTO students
VALUES (
        1,
        "Nathan Kiprotich",
        "nathan.kiprotich@student.moringaschool.com",
        "G301",
        100,
        "Active",
        3,
        "Available",
        1001,
        "2023-09-04"
    ),
    (
        2,
        "Beatrice Mwenje",
        "beatrice.mwenje@student.moringaschool.com",
        "G302",
        100,
        "Active",
        3,
        "Available",
        1003,
        "2023-09-04"
    ),
    (
        3,
        "Kibet Nathan",
        "kibet.nathan@student.moringaschool.com",
        "G303",
        100,
        "Active",
        3,
        "Available",
        1002,
        "2023-09-04"
    ),
    (
        4,
        "Linder Opondo",
        "linder.opondo@student.moringaschool.com",
        "G304",
        100,
        "Active",
        3,
        "Available",
        1003,
        "2023-09-04"
    ),
    (
        5,
        "Gad Ongoro",
        "gad.ongoro@student.moringaschool.com",
        "G305",
        100,
        "Active",
        3,
        "Available",
        1003,
        "2023-09-04"
    ),
    (
        6,
        "Samuel Otieno",
        "samuel.otieno@student.moringaschool.com",
        "G306",
        100,
        "Active",
        3,
        "Available",
        1001,
        "2023-09-04"
    );
-- R stud --
SELECT *
FROM students;
SELECT *
FROM students
WHERE major = "FrontEnd"
ORDER BY id DESC
LIMIT 5;
-- U stud --
UPDATE students
SET major = "FE"
WHERE major = "FrontEnd";
SELECT *
FROM students;
-- D stud --
DELETE FROM students
WHERE id = 5;
DELETE FROM students;
SELECT *
FROM students;
-- JOIN --
SELECT stud.name AS stud_name,
    sup.name AS sup_name
FROM students AS stud
    RIGHT JOIN supervisors AS sup ON stud.sup_id = sup.sup_id;
-- RESET DB TO DEFAULT -- 
SHOW TABLES;
DROP TABLE courses;
DROP TABLE students;
DROP TABLE phases;
DROP TABLE supervisors;
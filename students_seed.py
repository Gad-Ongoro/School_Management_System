from sqlalchemy.orm import sessionmaker
from models import engine, Student
import click
from faker import Faker

faker = Faker()

""" Using click CLI Library to get and map user input to the DataBase """
@click.command()
# @click.option("--count", default=1)
# @click.option("--name", prompt="Student Name")
# @click.option("--email", prompt="Email")
# @click.option("--reg_id", prompt="Reg_ID")
# @click.option("--status", prompt="Status")
# @click.option("--phase_id", prompt="Phase ID")
# @click.option("--sup_id", prompt="Sup_ID", type=int)
# @click.option("--course_id", prompt="Course ID", type=int)

def student_handler(count, name, email, reg_id, status, phase_id, sup_id, course_id):
    for _ in range(count):
        stud = {"Name": name, "Email": email, "Reg_id": reg_id, "Status": status, "Phase": phase_id, "Sup_id": sup_id, "Course_id": course_id}
        print(stud)

        new_student = Student(name = name, email = email, reg_id = reg_id, status = status, phase_id = phase_id, sup_id = sup_id, course_id = course_id)

        session.add(new_student)
        session.commit()

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    # student_handler()
    pass

""" CREATE """
# filling DB with initial set of data
student_1 = Student(name = faker.name(), email = faker.email(), reg_id = "G301", status = "Active", phase_id = 104, sup_id = 1000, course_id = 1)
student_2 = Student(name = faker.name(), email = faker.email(), reg_id = "G302", status = "Inactive", phase_id = 105, sup_id = 1000, course_id = 1)
student_3 = Student(name = faker.name(), email = faker.email(), reg_id = "G303", status = "Active", phase_id = 105, sup_id = 1000, course_id = 1)
student_4 = Student(name = faker.name(), email = faker.email(), reg_id = "G304", status = "Inactive", phase_id = 105, sup_id = 1000, course_id = 1)
student_5 = Student(name = faker.name(), email = faker.email(), reg_id = "G305", status = "Active", phase_id = 105, sup_id = 1000, course_id = 1)
#session.add_all([student_1, student_2, student_3, student_4, student_5])
# session.commit()

""" READ """
# students_list = session.query(Student)
# print([stud for stud in students_list])
# for stud in students_list:
#     print(stud)

""" using OOP """
class student_data_query:
    def __init__(self):
        pass
    
    # CREATE    
    def add_new_student(self, name, email, reg_id, status, phase_id, sup_id, course_id):
        new_student = Student(name = name, email = email, reg_id = reg_id, status = status, phase_id = phase_id, sup_id = sup_id, course_id = course_id)
        session.add(new_student)
        session.commit()
    
    # READ
    def get_all_students_data(self):
        all_students = session.query(Student).all() #.all() returns a list []
        for student in all_students:
            print(student)   
            pass     
        # print(all_students)
        pass
    
    # UPDATE
    def update_student_data(self, id:int, new_status):
        for student in session.query(Student).all(): #using a list to update student
            if student.stud_id == id:
                student.status = new_status
        session.commit()
    
    # DELETE
    def delete_student(self, name):
        self.name = name
        for student in session.query(Student).all():
            if student.name == name:
                session.delete(student)
                session.commit()
    
studs = student_data_query()

""" CREATE """
studs.add_new_student(faker.name(), faker.email(), "G105", status = "Active", phase_id = 105, sup_id = 1002, course_id = 2)

""" READ """
studs.get_all_students_data()

""" UPDATE """
studs.update_student_data(5, "Inactive")

""" DELETE """
studs.delete_student("Sam G")
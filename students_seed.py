from sqlalchemy.orm import sessionmaker
from models import engine, Student
import click
from faker import Faker

faker = Faker()

@click.command()
@click.option("--count", default=1)
# @click.option("--super_id", prompt="ID", type=int)
@click.option("--name", prompt="Student Name")
@click.option("--email", prompt="Email")
@click.option("--reg_id", prompt="Reg_ID")
@click.option("--status", prompt="Status")
@click.option("--phase_id", prompt="Phase ID")
@click.option("--sup_id", prompt="Sup_ID", type=int)
@click.option("--course_id", prompt="Course ID", type=int)

def supervisor_handler(count, name, email, reg_id, status, phase_id, sup_id, course_id):
    for _ in range(count):
        stud = {"Name": name, "Email": email, "Reg_id": reg_id, "Status": status, "Phase": phase_id, "Sup_id": sup_id, "Course_id": course_id}
        print(stud)

        new_student = Student(name = name, email = email, reg_id = reg_id, status = status, phase_id = phase_id, sup_id = sup_id, course_id = course_id)

        session.add(new_student)
        session.commit()

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    supervisor_handler()
    pass

student_1 = Student(name = faker.name(), email = faker.email(), reg_id = "G301", status = "Active", phase_id = 104, sup_id = 1000, course_id = 1)
student_2 = Student(name = faker.name(), email = faker.email(), reg_id = "G302", status = "Active", phase_id = 105, sup_id = 1000, course_id = 1)
student_3 = Student(name = faker.name(), email = faker.email(), reg_id = "G303", status = "Active", phase_id = 105, sup_id = 1000, course_id = 1)
student_4 = Student(name = faker.name(), email = faker.email(), reg_id = "G304", status = "Active", phase_id = 105, sup_id = 1000, course_id = 1)
student_5 = Student(name = faker.name(), email = faker.email(), reg_id = "G305", status = "Active", phase_id = 105, sup_id = 1000, course_id = 1)
session.add_all([student_1, student_2, student_3, student_4, student_5])
# session.commit()
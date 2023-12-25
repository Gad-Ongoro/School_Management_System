from sqlalchemy.orm import sessionmaker
from models import engine, Course
import click

""" Using click CLI Library to get and map user input to the DataBase """
@click.command()
# @click.option("--count", default=1)
# @click.option("--name", prompt="Name")
# @click.option("--sup_id", prompt="Supervisor ID")

def course_handler(count, name, sup_id):
    for _ in range(count):
        # click.echo("Sup ID: %d" % id)
        # click.echo("Name: %s" % name)
        # click.echo("Email: %s" % email)
        # click.echo("Major: %s" % major)
        course = {"Name": name, "Supervisor ID": sup_id}
        print(course)

        new_course = Course(name = name, sup_id = sup_id)

        session.add(new_course)
        session.commit()
        

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    # course_handler()
    pass

""" CREATE """
# filling DB with initial set of data C
course_1 = Course(name = "Software Engineering", sup_id = 1000)
course_2 = Course(name = "Product Design", sup_id = 1001)
course_3 = Course(name = "Data Science", sup_id = 1002)
course_4 = Course(name = "Data Visualization with Python", sup_id = 1003)
course_5 = Course(name = "DevOps Engineering", sup_id = 1004)
course_6 = Course(name = "Cybersecurity", sup_id = 1005)

session.add_all([course_1, course_2, course_3, course_4, course_5, course_6])
session.commit()

""" CRUD using OOP """
class course_data_query:
    def __init__(self):
        pass
    
    # CREATE    
    def add_new_course(self, name, sup_id):
        new_course = Course(name = name, sup_id = sup_id)
        session.add(new_course)
        session.commit()
    
    # READ
    def get_all_courses_data(self):
        all_courses = session.query(Course).all() #.all() returns a list []
        for course in all_courses:
            print(course)     
        # print(all_courses)
    
    # UPDATE
    def update_course_data(self, id:int, new_sup):
        for course in session.query(Course).all(): #using a list to update course
            if course.course_id == id:
                course.sup_id = new_sup
        session.commit()
    
    # DELETE
    def delete_course(self, id):
        for course in session.query(Course).all():
            if course.course_id == id:
                session.delete(course)
                session.commit()
    
course_data = course_data_query()

""" CREATE """
course_data.add_new_course("Mobile Application Development", 1004)

""" READ """
course_data.get_all_courses_data()

""" UPDATE """
course_data.update_course_data(4, 1010)

""" DELETE """
course_data.delete_course(7)
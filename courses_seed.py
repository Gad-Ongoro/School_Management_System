from sqlalchemy.orm import sessionmaker
from models import engine, Course
import click

@click.command()
@click.option("--count", default=1)
@click.option("--name", prompt="Name")
@click.option("--sup_id", prompt="Supervisor ID")

def course_handler(count, name, sup_id):
    for _ in range(count):
        # click.echo("Sup ID: %d" % id)
        # click.echo("Name: %s" % name)
        # click.echo("Email: %s" % email)
        # click.echo("Major: %s" % major)
        course = {"Name": name, "Supervisor ID": sup_id}
        print(course)

        new_course = Course(name =  name, sup_id = sup_id)

        session.add(new_course)
        session.commit()
        

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    course_handler()
    pass

course_1 = Course(name = "Software Engineering", sup_id = 1)
course_2 = Course(name = "Product Design", sup_id = 1)
course_3 = Course(name = "Data Science", sup_id = 1)
course_4 = Course(name = "Data Visualization with Python", sup_id = 1)
course_5 = Course(name = "DevOps Engineering", sup_id = 1)
course_6 = Course(name = "Cybersecurity", sup_id = 1)

# session.add_all([supervisor1, supervisor2])
# session.commit()
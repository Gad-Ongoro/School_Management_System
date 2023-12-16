from sqlalchemy.orm import sessionmaker
from models import engine, Course
import click

@click.command()
@click.option("--count", default=1)
@click.option("--name", prompt="Name")
@click.option("--sup_id", prompt="Supervisor ID")

def phase_handler(count, name, sup_id):
    for _ in range(count):
        # click.echo("Sup ID: %d" % id)
        # click.echo("Name: %s" % name)
        # click.echo("Email: %s" % email)
        # click.echo("Major: %s" % major)
        course = {"Phase Name": name, "Supervisor ID": sup_id}
        print(course)

        new_course = Course(name =  name, sup_id = sup_id)

        session.add(new_course)
        session.commit()
        

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    phase_handler()
    pass
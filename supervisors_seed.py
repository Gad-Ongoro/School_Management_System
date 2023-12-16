from sqlalchemy.orm import sessionmaker
from models import engine, Supervisor
import click

@click.command()
@click.option("--count", default=1)
@click.option("--super_id", prompt="Supervisor ID", type=int)
@click.option("--super_name", prompt="Name")
@click.option("--super_email", prompt="Email")
@click.option("--super_major", prompt="Major")

def supervisor_handler(count, super_id, super_name, super_email, super_major):
    for _ in range(count):
        # click.echo("Sup ID: %d" % id)
        # click.echo("Name: %s" % name)
        # click.echo("Email: %s" % email)
        # click.echo("Major: %s" % major)
        sup = {"ID": super_id, "name": super_name, "email": super_email, "major": super_major}
        print(sup)

        new_supervisor = Supervisor(sup_id = super_id, name = super_name, email = super_email, major = super_major)

        session.add(new_supervisor)
        session.commit()
        

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    supervisor_handler()
    pass

supervisor1 = Supervisor(sup_id = 1000, name="Khalifa Muyideen", email="kmuyideen@outlook.com", major="Software Engineering")
supervisor2 = Supervisor(sup_id = 1001, name="Abdi Rashid", email="abdulrashid@gmail.com", major="Product Design")
supervisor3 = Supervisor(sup_id = 1002, name="Sean Newton", email="seannewton@gmail.com", major="Data Science")
supervisor4 = Supervisor(sup_id = 1003, name="Emma Maart", email="emmamaart@outlook.com", major="Cybersecurity")

# session.add_all([supervisor1, supervisor2])
# session.commit()
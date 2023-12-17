from sqlalchemy.orm import sessionmaker
from models import engine, Phase
import click

@click.command()
@click.option("--count", default=1)
@click.option("--name", prompt="Phase Name")
@click.option("--sup_id", prompt="Supervisor ID")

def phase_handler(count, name, sup_id):
    for _ in range(count):
        # click.echo("Sup ID: %d" % id)
        # click.echo("Name: %s" % name)
        # click.echo("Email: %s" % email)
        # click.echo("Major: %s" % major)
        course = {"Phase Name": name, "Supervisor ID": sup_id}
        print(course)

        new_phase = Phase(name = name, sup_id = sup_id)

        session.add(new_phase)
        session.commit()
        

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    phase_handler()
    pass

# filling DB with initial set of data
phase_0 = Phase(phase_id = 100, name="Phase_0", sup_id = 1000)
phase_1 = Phase(phase_id = 101, name="Phase_0", sup_id = 1001)
phase_2 = Phase(phase_id = 102, name="Phase_0", sup_id = 1002)
phase_3 = Phase(phase_id = 103, name="Phase_0", sup_id = 1003)
phase_4 = Phase(phase_id = 104, name="Phase_0", sup_id = 1004)
phase_5 = Phase(phase_id = 105, name="Phase_0", sup_id = 1005)

# session.add_all([phase_0, phase_1, phase_2, phase_3, phase_4, phase_5])
# session.commit()
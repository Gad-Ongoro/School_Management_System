from sqlalchemy.orm import sessionmaker
from models import engine, Phase
import click

""" Using click CLI Library to get and map user input to the DataBase """
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

""" CREATE """
# filling DB with initial set of data C
phase_0 = Phase(phase_id = 100, name="Phase-0", sup_id = 1000)
phase_1 = Phase(phase_id = 101, name="Phase-1", sup_id = 1001)
phase_2 = Phase(phase_id = 102, name="Phase-2", sup_id = 1002)
phase_3 = Phase(phase_id = 103, name="Phase-3", sup_id = 1003)
phase_4 = Phase(phase_id = 104, name="Phase-4", sup_id = 1004)
phase_5 = Phase(phase_id = 105, name="Phase-5", sup_id = 1005)

session.add_all([phase_0, phase_1, phase_2, phase_3, phase_4, phase_5])
session.commit()

""" CRUD using OOP """
class phase_data_query:
    def __init__(self):
        pass
    
    # CREATE    
    def add_new_phase(self, name, sup_id):
        new_phase = Phase(name = name, sup_id = sup_id)
        session.add(new_phase)
        session.commit()
    
    # READ
    def get_all_phases_data(self):
        all_phases = session.query(Phase).all() #.all() returns a list []
        for phase in all_phases:
            print(phase)     
        # print(all_phases)
    
    # UPDATE
    def update_phase_data(self, id:int, new_sup):
        for phase in session.query(Phase).all(): #using a list to update phase
            if phase.phase_id == id:
                phase.sup_id = new_sup
        session.commit()
    
    # DELETE
    def delete_phase(self, id):
        for phase in session.query(Phase).all():
            if phase.phase_id == id:
                session.delete(phase)
                session.commit()
    
phase_data = phase_data_query()

""" CREATE """
phase_data.add_new_phase("Phase-6", 1009)

""" READ """
phase_data.get_all_phases_data()

""" UPDATE """
phase_data.update_phase_data(106, 1000)

""" DELETE """
phase_data.delete_phase(106)
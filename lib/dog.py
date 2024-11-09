from models import Dog

def create_table(Base, engine):
    """Creates tables in the database using the provided Base and engine."""
    Base.metadata.create_all(engine)
    

def save(session, dog_instance):
    """Adds a Dog instance to the session and commits it to save to the database."""
    session.add(dog_instance)
    session.commit()

def get_all(session):
    """Fetches all Dog instances from the database and returns them as a list."""
    return session.query(Dog).all()

def find_by_name(session, name):
    """Fetch a Dog instance from the database by name."""
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    """Fetch a Dog instance from the database by id."""
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    """Fetch a Dog instance from the database by name and breed."""
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, new_breed):
    """Update the breed of a Dog instance in the database."""
    dog.breed = new_breed
    session.commit()
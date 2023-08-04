from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    paintings = db.relationship("Painting", back_populates="users")

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'
    


class Plants(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prompt = db.Column(db.String)
    plant_list = db.Column(db.String)  # Adjust the type as necessary

    def __init__(self, prompt, plant_list):
        self.prompt = prompt

    
def connect_to_db(flask_app, db_uri="postgresql:///paintbynumbers", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
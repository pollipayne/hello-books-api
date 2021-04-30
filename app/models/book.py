from app import db 

class Book(db.Model): #an instance of SQLAlchemy Books is inheriting 
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #creates a DB column called ID, of type INT, assigns it as PK & tells it 
    #to auto increment 
    title = db.Column(db.String)
    # creates a DB column called title, sets it of type String
    description = db.Column(db.String)
    # creates a DB column called description, sets it of type String

    def to_json(self):
        return {"id": self.id, 
                "title": self.title, 
                "description": self.description}

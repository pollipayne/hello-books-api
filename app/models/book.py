from app import db 

class Book(db.Model):
    __tablename__ = "books_table"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
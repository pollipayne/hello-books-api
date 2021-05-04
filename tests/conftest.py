import pytest 
from app import create_app 
from app import db 
from app.models.book import Book 



@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app 

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_books(app):
    # here we are setting up an arrange step for 
    #that we can reuse for several tests 
    noodle_book = Book(title="Noodles!", 
                        description="All noodles all the time.")
    bean_book = Book(title="Beans!", 
                    description="All beans all the time!")

    db.session.add_all([noodle_book, bean_book])
    db.session.commit()
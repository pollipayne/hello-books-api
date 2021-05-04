







# get all books and return no records 
def test_get_all_books_with_no_records(client):
    #act
    response = client.get("/books")
    response_body = response.get_json()

    #assert 
    assert response.status_code == 200
    assert response_body[0] == []


#get one book by id 
def test_get_one_book_by_id(client):
    response = client.get("/books/1")
    response_body = response.get_json()
    

# update one book by id 


# delete one book by id 



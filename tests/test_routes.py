







# get all books and return no records 
def test_get_all_books_with_no_records(client):
    #act
    response = client.get("/books")
    response_body = response.get_json()

    #assert 
    assert response.status_code == 200
    assert response_body[0] == []


# get /books with valid data returns 200 w/ app data 
def test_get_all_books_with_valid_records(client, two_saved_books):
    #act
    response = client.get("/books")
    response_body = response.get_json()

    #assert 
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0][0] == { "id": 1, 
                            "title": "Noodles!", 
                            "description": "All noodles all the time."}
    assert response_body[0][1] == { "id": 2, 
                                    "title": "Beans!", 
                                    "description": "All beans all the time."}


#get one book by id 
def test_get_one_book_by_id(client, two_saved_books):
    #Act
    response = client.get("/books/1")
    response_body = response.get_json()

    #assert 
    assert response.status_code == 200
    assert response_body == { "id": 1, 
                            "title": "Noodles!", 
                            "description": "All noodles all the time."}
    


# get one book with no data returns 404 
def test_get_one_book_by_id_with_no_valid_data(client):
    #act 
    response = client.get("/books/1")
    response_body = response.get_json()

    #assert 

    assert response.status_code == 404
    assert response_body is None


#post books returns 201 w/ valid request body 
def test_post_book_with_valid_data(client):
    post = client.post('/books', json={"title":"Pasta", 
                        "description": "All pasta all the time."})

    response_body = post.get_json()


    assert post.status_code == 201
    assert response_body["Success"] == True


#get one book with query params 
def test_get_one_book_by_query_params(client, two_saved_books):
    #Act
    response = client.get("/books", query_string={"title": "Noodles!"})
    response_body = response.get_json()

    #assert 
    assert response.status_code == 200
    assert response_body[0] == [{ "id": 1, 
                            "title": "Noodles!", 
                            "description": "All noodles all the time."}]



#
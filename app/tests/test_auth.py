import pytest
# from app import models, forms
from app.models import User, Post
from app.forms import LoginForm
#from app import routes


def test_login(client):
    response = client.get('/login')
    assert response.status_code == 200
    
    
def test_add_user_to_db(db):
    test_user = User(email='test_user@gmail.com',username = 'user', password_hash='1234')
    db.session.add(test_user)
    db.session.commit()
    assert len(User.query.all()) == 1    
    
def test_verify_user_exists(db):
    user = User.query.get(1)
    assert user.is_authenticated == True 
    
def test_valid_register(client, db):
    response = client.post('/login',
                           data=dict(uasername='user', email='testing@testing.com',
                                     password='testing', confirm='testing'),
                           follow_redirects=True)
    assert response.status_code == 200  


#  testing the add task  
def test_add(db):
    post = Post(nameTitle= 'Studying for all Finals',user_id='1', content='studying')
    db.session.add(post)
    db.session.commit()
    assert len(User.query.all()) == 1
    assert Post.query.get(1).content =='studying'
    assert Post.query.get(1).nameTitle == 'Studying for all Finals'

# testing login page is html 
def test_index(client):
     response = client.get('/login', content_type='html/text')
     assert response.status_code == 200

def test_user_requires_login(client):
    response = client.get("/", follow_redirects=True)
    assert b"Please log in to access this page." in response.data



def test_finish(client,db):
     response = client.post('/login',
                           data=dict(uasername='huan89', password='huean89'),
                           follow_redirects=True) 

     response = client.post("/edit", data=dict(status=True), follow_redirects=True )
     assert response.status_code == 404  

    
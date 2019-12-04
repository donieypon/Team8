import pytest
from app import routes
from app.models import User, Post
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user

@pytest.fixture(scope = 'module')
def new_user():
    user = User(email = 'yennhilam@ymail.com' , username = 'username', password_hash = generate_password_hash('1234'))
    return user

@pytest.fixture(scope = 'module')
def new_task():
    task = Post(nameTitle=' Studying Finals', content= " Finals include : COMPE 131 and CS 146 ", complete = False) 
    # author = 'current_user._get_current_object()' )
    return task

# Pytest 1
# testing validating new user yennhilam@ymail.com <---  maybe need to change
def test_new_user(new_user):
    assert new_user.email == 'yennhilam@ymail.com'
    assert new_user.password_hash != generate_password_hash('1234')
    print('Yay')
  
# Pytest 2
# verifying the new user is yennhilam@ymail.com
def test_login(new_user):
    assert new_user.is_authenticated == True
  
# Pytest 3
# testing the name content of model when it is not empty
def test_new_task(new_task):
    assert new_task.nameTitle != None
    
# Pytest 4 
# testing the task 'Studying Finals' is not a complete task
def test_complete(new_task):
    assert new_task.complete == False

# Pytest 5
# testing content is not empty
def test_content(new_task):
    assert new_task.content != None
    

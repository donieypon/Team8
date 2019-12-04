import pytest
from app import routes
from app.models import User, Post
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user

@pytest.fixture(scope = 'module')
def new_user():
  user = User(email = 'yennhilam@ymail.com' , username = 'username', password_hash = generated_password_hash('1234'))
  return user

# Pytest 1
# testing validating new user yennhilam@ymail.com <--- maybe need to change 
def test_new_user(new_user):
  assert new_user.email == 'yennhilam@ymail.com' 
  assert new_user.password_hash != generate_password_hash('1234')
  
# Pytest 2
# verifying the new user
def test_login(new_user):
  assert new_user.is_authenticated == True

# import pytest
# from app.models import User, Post
# from app.forms import LoginForm


# def test_get_login(client):
#     response = client.get('/login')
#     assert response.status_code == 200


# def test_add_user_to_db(db):
#     test_user = User(username='huan98', email='huan98@gmail.com', password='huan98')
#     db.session.add(test_user)
#     db.session.commit()
#     assert len(User.query.all()) == 1


# def test_valid_register(client, db):

#     response = client.post('/login',
#                                 data=dict(username='huan98', email='huan98@gmail.com', password='huan98', confirm='testing'),
#                                 follow_redirects=True)
#     assert response.status_code == 200

# def test_index(self):
#     response = self.client.get("/login", content_type="html/text")
#     self.assertEqual(response.status_code,200)

# def test_add(db):
#     post = Post(user_id='1', content='hello world')
#     db.session.add(post)
#     db.session.commit()
#     assert len(Post.query.all()) == 1
#     assert Post.query.get(1).content == 'hello world'

# def test_edit(client, db):
#     response = client.post("/login",
#                                 data=dict(username="huan98", password="huan98"),
#                                 follow_redirects=True       
#     )
#     response = client.post("/edit", 
#                                     data=dict(nameTitle="test", content="test"),
#                                 follow_redirects=True,
#     )

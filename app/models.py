from datetime import datetime
from app import db, login, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    followed = db.relationship('User',
                               secondary=followers,
                               primaryjoin=(followers.c.follower_id == id),
                               secondaryjoin=(followers.c.followed_id == id),
                               backref=db.backref('followers', lazy='dynamic'),
                               lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # def follow(self, user):
    #     if not self.is_following(user):
    #         self.followed.append(user)
    #         return self
    #
    # def unfollow(self, user):
    #     if self.is_following(user):
    #         self.followed.remove(user)
    #         return self
    #
    # def is_following(self, user):
    #     return self.followed.filter(followers.c.followed_id == user.id).count() > 0
    #
    # def followed_posts(self):
    #     return Post.query.join(followers, (followers.c.followed_id == Post.user_id)).filter(
    #         followers.c.follower_id == self.id).order_by(Post.timestamp.desc())

    def getResetToken(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verifyResetToken(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.leads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nameTitle = db.Column(db.String(256),  index=True)
    content = db.Column(db.UnicodeText, index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    complete = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Posts {}>'.format(self.nameTitle)

class Friend(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    friend_username = db.Column(db.String(64), index=True)
    friend_email = db.Column(db.String(64), index=True)
    friend_id = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Friend {}>'.format(self.id)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
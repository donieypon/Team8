from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, createAccount, PostForm, addFriend
from app.models import User, Post, Friend
from flask_login import current_user, login_user, login_required
from flask_login import logout_user
from flask_login import login_required
from werkzeug.urls import url_parse
from flask_bootstrap import Bootstrap

Bootstrap(app)

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = Post.query.all()
    return render_template('index.html', user=current_user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        # look at first result first()
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        # return to page before user got asked to login
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)
    return render_template('login.html', title='Sign in', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = createAccount()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/add', methods =['GET','POST'])
@login_required
def add(): 
    form = PostForm()
    if request.method == 'POST' :
        nameTitle = request.form.get('nameTitle')
        content = request.form.get('content')
        post = Post(nameTitle = nameTitle, content = content, author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        flash('Successfully to create task!')
        return redirect(url_for('index'))
    return render_template('task.html',form=form, legend='Add', title='New Tasks')

@app.route('/delete<int:id>')
@login_required
def delete(id):
    post = Post.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit(id): 
    post = Post.query.filter_by(id = id).first()
    form = PostForm()
    if request.method == 'POST':
            post.nameTitle = request.form.get('nameTitle')
            post.content =  request.form.get('content')
            db.session.commit()
            flash('Successfully Editted', 'success')
            return redirect(url_for('index'))
    return render_template('task.html', title='Edit', legend='Edit', form=form, post=post)

@app.route('/friends', methods=['GET', 'POST'])
@login_required
def friends():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    form = addFriend()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        #if already friends
        friendList = Friend.query.filter_by(user_id=current_user.id).all()
        isFriend = False
        for friend in friendList:
            if friend.friend_username == user.username:
                isFriend = True

        #if not friends
        if user and user != current_user:
            if isFriend:
                flash('You are already friends with this user.')
                return redirect(url_for('friends'))
            else:
                friend = Friend(author=current_user, friend_username=user.username, friend_id=user.id, friend_email=user.email)
                db.create_all()
                db.session.add(friend)
                db.session.commit()
                print(Friend.query.filter_by(user_id=current_user.id).all())
                flash('You are now friends with ' + user.username + '.')
                return redirect(url_for('friends'))
        #if invalid name
        else:
            flash('Error. Please enter a valid username.')
            return redirect(url_for('friends'))

        #get friends of user
        friends = current_user.friends.all()
        allFriends = []
        for friend in friends:
            user = User.query.filter_by(username=friend.friend_username).first()
            allFriends.append(friend.friend_username)

        return render_template('friendList.html', form=form, friends=allFriends)

    
if __name__ =='__main__':
    db.create_all()
    app.run(debug=True)


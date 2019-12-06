from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, createAccount, PostForm, mailForm
from app.models import User, Post
from flask_login import current_user, login_user, login_required
from flask_login import logout_user
from flask_login import login_required
from werkzeug.urls import url_parse
from flask_bootstrap import Bootstrap
from flask_mail import Message, Mail

Bootstrap(app)

mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'stufftodocmpe131@gmail.com'
app.config["MAIL_PASSWORD"] = 'cmpe131sjsu'

mail.init_app(app)

@app.route('/')
@app.route('/index')
@login_required
def index():
    post = Post.query.all()
    return render_template('index.html', user=current_user, post=post)

#login
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
    return render_template('LLogin.html', title='Sign in', form=form)

#______________________________________________________________________________

#logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

#______________________________________________________________________________

#register
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
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

#______________________________________________________________________________

#add task
@app.route('/add', methods =['GET','POST'])
@login_required
def add(): 
    form = PostForm()
    if request.method == 'POST' :
        nameTitle = request.form.get('nameTitle')
        content = request.form.get('content')
        post = Post(nameTitle=nameTitle, content=content, complete=False, author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        flash('Successfully created a task!')
        return redirect(url_for('index'))
    return render_template('task.html', form=form, legend='Create Task', title='New Tasks')

#______________________________________________________________________________

#delete task
@app.route('/delete<int:id>')
@login_required
def delete(id):
    post = Post.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))

#______________________________________________________________________________

#edit task
@app.route('/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit(id): 
    post = Post.query.filter_by(id = id).first()
    form = PostForm()
    if request.method == 'POST':
            post.nameTitle = request.form.get('nameTitle')
            post.content =  request.form.get('content')
            post.complete = form.complete.data
            db.session.commit()
            flash('Successfully Editted', 'success')
            return redirect(url_for('index'))
    return render_template('task.html', title='Edit', legend='Edit Task', form=form, post=post)

#______________________________________________________________________________

#complete task
@app.route('/complete/<int:id>')
@login_required
def complete(id):
    post = Post.query.filter_by(id = id).first()
    post.complete = True
    db.session.commit()
    return redirect(url_for('index'))

#______________________________________________________________________________

#send email message

@app.route('/mail', methods=['GET', 'POST'])
def mes():
    form = mailForm()
    if request.method == "POST":
        message = Message(form.subject.data, sender=current_user.email, recipients=[form.email.data], )
        message.body = """
            StuffToDo
              
                From:  %s 
                Content: 
                    %s 
            """ % (
            current_user.email,
            form.content.data,
        )
        mail.send(message)
        flash("Congratulation! Your message has been sent successfully!", "success")
        return redirect(url_for("index"))
    return render_template('mail.html', title="Send Message", legend="Send Message", form =form)

#______________________________________________________________________________

#share task

@app.route('/share/<int:id>', methods=['GET', 'POST'])
def share(id):
    form = mailForm()
    post = Post.query.filter_by(id = id).first()
    if request.method == "POST":
        shareTask = Message(subject='Task Shared', sender=current_user.email, recipients=[form.email.data], )
        shareTask.html = render_template('share.html', form=form, post=post)
        mail.send(shareTask)
        flash("Congratulation! Your message has been sent successfully!", "success")
        return redirect(url_for('index'))
    return render_template('mail.html', title='Share Task', legend='Share Task', form=form, post=post)

#______________________________________________________________________________

#add friend
@app.route('/friends', methods=['GET', 'POST'])
@login_required
def friends():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    form = addFriend()
    print('hi')
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #
    #     #checks if friends
    #     friendList = Friend.query.filter_by(user_id=current_user.id).all()
    #     isFriend = False
    #     for friend in friendList:
    #         if friend.friend_username == user.username:
    #             isFriend = True
    #
    #     #if user entered is valid, and not current user
    #     if user and user != current_user:
    #         # if friends or not friends
    #         if isFriend:
    #             flash('You are already friends with this user.')
    #             return redirect(url_for('friends'))
    #         else:
    #             friend = Friend(author=current_user, friend_username=user.username, friend_id=user.id, friend_email=user.email)
    #             db.create_all()
    #             db.session.add(friend)
    #             db.session.commit()
    #             print(Friend.query.filter_by(user_id=current_user.id).all())
    #             flash('You are now friends with ' + user.username + '.')
    #             return redirect(url_for('friends'))
    #
    #     #if invalid name
    #     else:
    #         flash('Error. Please enter a valid username.')
    #         return redirect(url_for('friends'))
    #
    #     #get friends of user
    #
    #     #friends = current_user.friends.all()
    #     for friend in friends:
    #         user = User.query.filter_by(username=friend.friend_username).first()
    #         allFriends.append(friend.friend_username)

    #return render_template('addFriend.html', form=form, friends=allFriends)

    return render_template('addFriend.html', form=form)

#______________________________________________________________________________

#follow
@app.route('/follow/<nickname>')
@login_required
def follow(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    if user == g.user:
        flash('You can\'t follow yourself!')
        return redirect(url_for('user', nickname=nickname))
    u = g.user.follow(user)
    if u is None:
        flash('Cannot follow ' + nickname + '.')
        return redirect(url_for('user', nickname=nickname))
    db.session.add(u)
    db.session.commit()
    flash('You are now following ' + nickname + '!')
    return redirect(url_for('user', nickname=nickname))

#______________________________________________________________________________

#unfollow
@app.route('/unfollow/<nickname>')
@login_required
def unfollow(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    if user == g.user:
        flash('You can\'t unfollow yourself!')
        return redirect(url_for('user', nickname=nickname))
    u = g.user.unfollow(user)
    if u is None:
        flash('Cannot unfollow ' + nickname + '.')
        return redirect(url_for('user', nickname=nickname))
    db.session.add(u)
    db.session.commit()
    flash('You have stopped following ' + nickname + '.')
    return redirect(url_for('user', nickname=nickname))

# @app.route('/user/<username>')
# @login_required
# def user1(username):
#     user = User.query.filter_by(username=username).first()
#     if user is None:
#         flash('User %s is not found.' % username)
#         return redirect(url_for('index'))
#
#     return render_template('profile.html', user=user)

#______________________________________________________________________________

if __name__ =='__main__':
    db.create_all()
    app.run(debug=True)


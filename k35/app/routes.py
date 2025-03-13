from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required, UserMixin, LoginManager
from bcrypt import hashpw, gensalt, checkpw
from . import create_app
from .models import get_db_connection

app = create_app()
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM user WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    if user is None:
        return None
    return User(user['id'], user['username'], user['email'], user['password'])

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = hashpw(password.encode('utf-8'), gensalt())

        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO user (username, email, password) VALUES (?, ?, ?)',
                         (username, email, hashed_password))
            conn.commit()
            flash('Your account has been created!', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username or email already exists', 'danger')
        finally:
            conn.close()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM user WHERE email = ?', (email,)).fetchone()
        conn.close()
        
        if user and checkpw(password.encode('utf-8'), user['password']):
            user_obj = User(user['id'], user['username'], user['email'], user['password'])
            login_user(user_obj, remember=request.form.get('remember'))
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/blog/new', methods=['GET', 'POST'])
@login_required
def new_blog():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = current_user.id

        conn = get_db_connection()
        conn.execute('INSERT INTO blog (title, content, date_posted, user_id) VALUES (?, ?, datetime("now"), ?)',
                     (title, content, user_id))
        conn.commit()
        conn.close()

        flash('Your blog has been created!', 'success')
        return redirect(url_for('home'))

    return render_template('create_blog.html')

@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    conn = get_db_connection()
    blog = conn.execute('SELECT * FROM blog WHERE id = ?', (blog_id,)).fetchone()
    conn.close()
    return render_template('view_blog.html', blog=blog)

@app.route('/blog/<int:blog_id>/update', methods=['GET', 'POST'])
@login_required
def update_blog(blog_id):
    conn = get_db_connection()
    blog = conn.execute('SELECT * FROM blog WHERE id = ?', (blog_id,)).fetchone()

    if blog['user_id'] != current_user.id:
        flash('You do not have permission to edit this blog.', 'danger')
        return redirect(url_for('home'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        conn.execute('UPDATE blog SET title = ?, content = ? WHERE id = ?', (title, content, blog_id))
        conn.commit()
        conn.close()

        flash('Your blog has been updated!', 'success')
        return redirect(url_for('blog', blog_id=blog_id))

    conn.close()
    return render_template('create_blog.html', blog=blog)

@app.route('/blog/<int:blog_id>/delete', methods=['POST'])
@login_required
def delete_blog(blog_id):
    conn = get_db_connection()
    blog = conn.execute('SELECT * FROM blog WHERE id = ?', (blog_id,)).fetchone()

    if blog['user_id'] != current_user.id:
        flash('You do not have permission to delete this blog.', 'danger')
        return redirect(url_for('home'))

    conn.execute('DELETE FROM blog WHERE id = ?', (blog_id,))
    conn.commit()
    conn.close()

    flash('Your blog has been deleted!', 'success')
    return redirect(url_for('home'))

@app.route('/')
@app.route('/home')
def home():
    conn = get_db_connection()
    blogs = conn.execute('SELECT * FROM blog').fetchall()
    conn.close()
    return render_template('home.html', blogs=blogs)

@app.route('/base')
def base():
    return render_template('base.html')

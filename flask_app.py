from web.main import *
def Posts():
    with app.app_context():
        #db.create_all()
        Posts=Post.query.all()
    return Posts

@app.route('/')
def home():
    return render_template('home.html',posts=Posts())

@app.route('/post/<name>')
def post_route(name):
    return render_template('post.html',content_url=f'posts/{name}/',name=name)


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
import json
import uuid


app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    with open("data_storage.json", "r") as file:
        posts = json.load(file)
    return render_template("index.html", posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        post_id = str(uuid.uuid4())
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')
        
        new_post = {"postid":post_id, "author": author, "title": title, "content": content}
        
        with open('data_storage.json', 'r') as file:
            posts = json.load(file)
            
        posts.append(new_post)
        
        with open('data_storage.json', 'w') as file:
            json.dump(posts, file, indent=4)
        
        return redirect(url_for('index'))
    
    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

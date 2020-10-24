from itertools import groupby
import sqlite3
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

#connects to database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__, static_url_path='/static')

# setup for email
app.config['SECRET_KEY'] = 'secret_random_string'
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "mailtestm16@gmail.com"
app.config['MAIL_PASSWORD'] = "itnefgxjcygivpwd"
app.config['MAIL_DEFAULT_SENDER'] = "mailtestm16@gmail.com"
mail = Mail(app)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about_me")
def about():
    return render_template('about_me.html')

@app.route("/contacts", methods=['GET'])
def contacts():
    if request.method == 'GET':
        email = request.args.get('email')
        title = request.args.get('title')
        textIn = request.args.get('textIn')
        msg = Message(title, sender = email, recipients = ["heart1@inbox.lv"])
        msg.body = textIn
        if isinstance(textIn, str) :
            mail.send(msg)

    return render_template('contacts.html')

@app.route("/projects")
def projects():
    conn = get_db_connection()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM article")
    imgCursor = conn.cursor()
    imgCursor.execute("SELECT * FROM images")

    imgs = imgCursor.fetchall()
    mainData = cursor.fetchall()

    lists = []
    listCount = 0
    for i in mainData:
        listCount += 1
        dataList = []
        imgList = []
        dataList.append(i)
        for j in imgs:
            if(j['list_id'] == listCount):
                imgList.append(j)
        dataList.append(imgList)
        lists.append(dataList)

    conn.close()
    
    print(lists[0][1][0]['articleImages'])

    # return render_template('projects.html', lists=lists)
    return render_template("public/projects.html", lists=lists, listLen=len(lists))

@app.route("/projects/<post>")
def page(post):
    conn = get_db_connection()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM article")

    #fetches all text data for article
    cursor = cursor.fetchall()    
    i = 0
    for x in cursor:
        i += 1
        if x['urlExtension'] == post:            
            break

    images = conn.cursor()
    images.execute("SELECT * FROM images")

    #fetches all data for images
    imageList = []
    images = images.fetchall()
    for x in images:
        if x['list_id'] == i:
            imageList.append(x)
    
    video = False
    if cursor[i-1]['videoLink'] != None:
        video = True

    conn.close()
    return render_template("public/post.html", values=cursor[i-1], imageList=imageList, imageListLen=len(imageList), video=video)

if __name__ == '__main__':
    app.run(debug=True)
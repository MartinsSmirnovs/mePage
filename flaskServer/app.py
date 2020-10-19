from itertools import groupby
import sqlite3
from flask import Flask, render_template, request, flash, redirect, url_for

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_random_string'


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about_me")
def about():
    return render_template('about_me.html')

@app.route("/contacts")
def contacts():
    return render_template('contacts.html')

@app.route("/projects")
def projects():
    conn = get_db_connection()
    
    # articles = conn.execute('SELECT i.imageName, l.title FROM images i JOIN article l \
    #                       ON i.list_id = l.id ORDER BY l.title;').fetchall()
    # lists = {}
    # for k, g in groupby(articles, key=lambda t: t['title']):
        # lists[k] = list(g)

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
    
    # print(lists[0][1][0]['articleImages'])

    conn.close()
    # return render_template('projects.html', lists=lists)
    return render_template('projects.html', lists=lists)

if __name__ == '__main__':
    app.run(debug=True)
DROP TABLE IF EXISTS article;
DROP TABLE IF EXISTS images;

CREATE TABLE article (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    videoLink TEXT
);

CREATE TABLE images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    list_id INTEGER NOT NULL,
    articleImages TEXT,
    testText TEXT,
    imageName TEXT NOT NULL,
    FOREIGN KEY (list_id) REFERENCES article (id)
);
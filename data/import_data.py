import json
import mysql.connector
from datetime import datetime


articles = json.load(open('data/articles.json'))

try:
    connection = mysql.connector.connect(
        host="127.0.0.1", 
        user="root", 
        password="root", 
        database="discussion"
    )
    cursor = connection.cursor()

    for article in articles:
        # insert article and get article_id
        cursor.execute(
            "INSERT INTO article (content, author, created, updated) VALUES (%s, %s, %s, %s)",
            (article['content'], article['author'], datetime.now(), datetime.now())
        )
        connection.commit()
        article_id = cursor.lastrowid
        print(f'{cursor.rowcount} record inserted, article_id: {article_id}')

        for comment in article['comments']:
            # insert comment and get comment_id
            cursor.execute(
                "INSERT INTO comment (content, author, article, created, updated) VALUES (%s, %s, %s, %s, %s)",
                (comment['content'], comment['author'], article_id, datetime.now(), datetime.now())
            )
            connection.commit()
            comment_id = cursor.lastrowid
            print(f'\t{cursor.rowcount} record inserted, comment_id: {comment_id}')

            for reply in comment['replies']:
                # insert reply and get reply_id
                cursor.execute(
                    "INSERT INTO comment (content, author, article, root_comment, created, updated) VALUES (%s, %s, %s, %s, %s, %s)",
                    (reply['content'], reply['author'], article_id, comment_id, datetime.now(), datetime.now())
                )
                connection.commit()
                reply_id = cursor.lastrowid
                print(f'\t\t{cursor.rowcount} record inserted, reply_id: {reply_id}')

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table, {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

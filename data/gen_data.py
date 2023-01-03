import random
import json


number_of_users = 20
max_comments = 10
max_reply_comments = 2
number_of_article = 100000

articles = []
for i in range(1, number_of_article+1):
    article = {
        'author': f'user {random.randint(1, number_of_users)}',
        'content': f'article {i}'
    }

    comments = []
    for j in range(1, random.randint(1, max_comments)+1):
        comment = {
            'author': f'user {random.randint(1, number_of_users)}',
            'content': f'comment {j}'
        }

        replies = []
        for k in range(1, random.randint(0, max_reply_comments)+1):
            reply = {
                'author': f'user {random.randint(1, number_of_users)}',
                'content': f'reply {k}'
            }
            replies.append(reply)
        
        comment['replies'] = replies
        comments.append(comment)
    
    article['comments'] = comments
    articles.append(article)
    
articles_json = json.dumps(articles, indent=4)

with open("data/articles.json", "w") as outfile:
    outfile.write(articles_json)

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
Docker and Docker Compose are required, check the [Documentation](https://docs.docker.com/compose/install/).

### Installation

1. Clone the repo
  ```sh
  git clone https://github.com/khnhkd/discussion_api.git
  ```
  Unzip mysql data
  ```sh
  cd discussion_api/data
  unzip discussion.zip discussion.sql
  ```
2. Check Docker IP address and replace database host in config/settings.py
  ```sh
  ip a
  ```
  ```sh
  docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
  link/ether 02:42:5f:80:f0:39 brd ff:ff:ff:ff:ff:ff
  inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
      valid_lft forever preferred_lft forever
  inet6 fe80::42:5fff:fe80:f039/64 scope link 
      valid_lft forever preferred_lft forever
  ```
  Edit HOST's default database in config/settings.py as bellow
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql', 
          'NAME': 'discussion',
          'USER': 'khanhkd',
          'PASSWORD': 'abcd@1234',
          'HOST': '172.17.0.1',   # Or an IP Address that your DB is hosted on
          'PORT': '3307',
      },
  }
  ```
3. Build docker-compose
  Database MySQL
  ```sh
  cd discussion_api/mysql
  docker-compose up -d
  ```
  <!-- Grant user khanhkd with all privileges
  ```sh
  docker exec -it db mysql -u khanhkd -pabcd@1234
  grant ALL PRIVILEGES ON *.* TO 'khanhkd'@'%';
  flush privileges;
  ``` -->

  Backend API Django
  ```sh
  cd discussion_api
  docker-compose up -d
  ```
  After done, please check the API availability by access [127.0.0.1](http://127.0.0.1:8000/api/article). If wrong, please restart API container
  ```sh
  docker restart api
  ```
<!-- USAGE EXAMPLES -->
## Usage
  API Routes
1. Get all articles
  ```http
  GET /api/article?p=1&p_size=2
  ```
  | Parameter | Type | Description |
  | :--- | :--- | :--- |
  | `p` | `int` | The page number (default 1) |
  | `p_size` | `int` | The record number per page (defaul 10) |
  
  Responses
  ```json
  [
    {
        "id": 1,
        "author": "user 1",
        "content": "article 1",
        "created": "2023-01-02T18:39:45.367907Z",
        "updated": "2023-01-02T18:39:45.367911Z",
        "all_comments": [
            {
                "id": 1,
                "content": "comment 1",
                "author": "user 11",
                "article": 1,
                "root_comment": null,
                "updated": "2023-01-02T18:39:45.376484Z",
                "all_replies": []
            },
            {
                "id": 2,
                "content": "comment 2",
                "author": "user 16",
                "article": 1,
                "root_comment": null,
                "updated": "2023-01-02T18:39:45.383390Z",
                "all_replies": [
                    {
                        "id": 3,
                        "content": "reply 1",
                        "author": "user 14",
                        "article_id": 1,
                        "root_comment_id": 2,
                        "created": "2023-01-02T18:39:45.392115Z",
                        "updated": "2023-01-02T18:39:45.392117Z"
                    }
                ]
            }
        ]
    },
    ...
  ]
  ```
  
2. Get an article by id
  ```http
  GET /api/article/<article_id>
  ```

  Responses
  ```json
  {
    "id": 1,
    "author": "user 1",
    "content": "article 1",
    "created": "2023-01-02T18:39:45.367907Z",
    "updated": "2023-01-02T18:39:45.367911Z",
    "all_comments": [
        {
            "id": 1,
            "content": "comment 1",
            "author": "user 11",
            "article": 1,
            "root_comment": null,
            "updated": "2023-01-02T18:39:45.376484Z",
            "all_replies": []
        },
        {
            "id": 2,
            "content": "comment 2",
            "author": "user 16",
            "article": 1,
            "root_comment": null,
            "updated": "2023-01-02T18:39:45.383390Z",
            "all_replies": [
                {
                    "id": 3,
                    "content": "reply 1",
                    "author": "user 14",
                    "article_id": 1,
                    "root_comment_id": 2,
                    "created": "2023-01-02T18:39:45.392115Z",
                    "updated": "2023-01-02T18:39:45.392117Z"
                }
            ]
        }
    ]
  }
  ```

3. Get top 10 articles (have most comments)
  ```http
  GET /api/article/top10
  ```

  ```json
  [
    {
      "id": 13947,
      "author": "user 15",
      "content": "article 13947",
      "created": "2023-01-02T18:57:14.540903Z",
      "updated": "2023-01-02T18:57:14.540906Z",
      "all_comments": [
        {
          "id": 152758,
              "content": "comment 1",
              "author": "user 20",
              "article": 13947,
              "root_comment": null,
              "updated": "2023-01-02T18:57:14.547483Z",
              "all_replies": [
                {
                  "id": 152759,
                  "content": "reply 1",
                  "author": "user 16",
                  "article_id": 13947,
                  "root_comment_id": 152758,
                  "created": "2023-01-02T18:57:14.554299Z",
                  "updated": "2023-01-02T18:57:14.554302Z"
                }
              ]
        }, 
        ...
      ]
    },
    ...
  ]
  ```

  <!-- <ol>
    <li>[Get all articles](http://127.0.0.1:8000/api/article)</li>
    <li>[Get article by id](http://127.0.0.1:8000/api/article/1)</li>
    <li>[Get top 10 articles](http://127.0.0.1:8000/api/article/top10)</li>
  </ol> -->
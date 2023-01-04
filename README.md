<!-- # Clone source: https://github.com/khnhkd/discussion_api.git
# Unzip data/discussion.zip
# Install docker, docker-compose
# cd discussion_api
# docker-compose build && docker up -d -->

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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- GETTING STARTED -->
## Getting Started
This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
Docker and Docker Compose are required, check the [Documentation](https://docs.docker.com/compose/install/).

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/khnhkd/discussion_api.git
   ```
2. Check docker ip address and replace database host in config.settings.py
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
2. Build docker-compose
   ```sh
   cd discussion_api
   // database mysql
   cd mysql
   docker-compose up -d
   // api django
   cd ..
   docker-compose up -d
   ```
3. Check api 
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>
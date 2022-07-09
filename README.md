[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<br />
<p align="center">
  <a href="https://github.com/banjoanton/plex-web">
    <img src="https://i.imgur.com/WjsN7MC.png" alt="Logo" width="150" height="150">
  </a>
  <h3 align="center">PlexWeb</h3>

  <p align="center">
    Add IMDb playlists to your Plex server
    <br />
    <a href="https://plex-web.herokuapp.com/">View Website</a>
    ·
    <a href="https://github.com/banjo/plex-web/issues/new">Report Bug or Request Feature</a>
  </p>
</p>

## Disclaimer

This project was created when I first started with programming. It does not work anymore since the Plex API has changed. I mostly leave it here for nostalgic reasons. 

## Table of contents
- [Table of contents](#table-of-contents)
- [About](#about)
  - [Built with](#built-with)
- [Download and run](#download-and-run)
- [Features](#features)
- [Info](#info)
- [Docker](#docker)
- [Contributing](#contributing)

## :clapper: About
![PlexWeb web app](https://i.imgur.com/H08RhfC.png)

PlexWeb is a web manager for Plex servers. Connect to your server via your URL and token to access features like viewing current activity and adding playlists based on IMDb lists.

### 📋 Built with
* Python
  * Flask
  * Beautiful Soup
  * PlexAPI
* HTML
* CSS
  * Bootstrap
* Javascript
  * jQuery

## ☁️ Download and run

- Install [Python](https://www.python.org/) and [Git](https://git-scm.com/)

```bash
# Clone repository
$ git clone https://github.com/banjoanton/plex-web.git

# Change directory to repository
$ cd "plex-web"

# Install requirements
$ pip install -r requirements.txt
# or pip3 in some cases
$ pip3 install -r requirements.txt

# Run flask server
$ flask run
```
## ✔️ Features

* Sign in to your Plex server.
  * Use **url** and **token**.
* See users connected to the server.
  * See what they are **currently watching**.
* **Search** the Plex library for shows and movies.
* See playlists on the server.
  * Click on a playlist to get the **full list of movies**, including:
    * Title
    * Year released
    * Rating (from TheMovieDB)
    * Link to IMDb
* **Add playlist** to server.
  * Based on already created IMDb lists.
  * Choose name
  * **Choose users** that should receive the playlists as well

## :information_source:	 Info
This is my **final project** in the **[CS50](https://www.edx.org/course/cs50s-introduction-to-computer-science)** course. It includes most of the programming languages that are covered in the course; HTML, Python, Javascript and Jinja. Python is used as back-end with Flask, and Javascript is used to make the page dynamic. The page design hasn't been the main focus, but Bootstrap has been used to make it look as good as possible.

This project was based on **lack of playlists in Plex**. When you have a movie library, the built in selection are pretty much useless. Therefore, I created a simple web app that adds playlists based on scraping a choosen IMDb list (like [this](https://www.imdb.com/list/ls026173135/)). You can add any list you find, and the web is full of them. All movies that you have in your library that matches the movies in the list will be added to a playlist.

The other features of the web app are just neat implementations that enhances the management of playlists.

## :whale: Docker
[christronyxyocum](https://github.com/christronyxyocum) created a Docker image which can be accessed [here](https://hub.docker.com/r/tronyx/plex-web).

Github link [here](https://github.com/christronyxyocum/docker-plex-web).


## 🔧 Contributing
Pull requests are welcome. Feel free to add anything.

<!-- LINKS AND IMAGES -->
[stars-shield]: https://img.shields.io/github/stars/banjo/plex-web
[stars-url]: https://github.com/banjo/plex-web/stargazers
[issues-shield]: https://img.shields.io/github/issues/banjo/plex-web
[issues-url]: https://github.com/banjo/plex-web/issues
[forks-shield]: https://img.shields.io/github/forks/banjo/plex-web
[forks-url]: https://github.com/banjo/plex-web/network/members

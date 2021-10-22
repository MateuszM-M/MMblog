# MMblog - blog about programming

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [Setup](#setup)
* [Inspiration](#inspiration)


## General info

Simple blog app created with Django. My main focus was to gain basic skills in web development with this framework, HTML and CSS. This is my first web app created only by me.

![Alt text](static/images/screens/1.png "Main site")
![Alt text](static/images/screens/2.png "Rich text edited post")
![Alt text](static/images/screens/3.png "Comments")
![Alt text](static/images/screens/4.jpg "Mobile")


## Technologies

 - Python 
 - Django 
 - PostgreSQL
 - AWS S3
 - Heroku
 - Django ckeditor 6
 - HTML
 - CSS

Database is currently hosted on Heroku. At first I used AWS RDS but unfortunately my free trial expired.
 

## Features

 - CRUD of posts using admin panel
 - Adding comments by readers
 - Hamburger menu in html&css
 - Pagination
 
## Setup 

Clone repo `git clone https://github.com/MateuszM-M/MMblog`,

Go to repo directory `cd MMblog`,

Create virtual environment `python -m venv venv`,

Activate environment `venv\scripts\activate`,

Install required packages `pip install -r requirements.txt`,

Rename MMblog/settings/`.env-example` to `.env`,

Migrate database `python manage.py migrate`,

Create superuser `python manage.py createsuperuser`,

Make server up and running `python manage.py runserver`,

Browse http://127.0.0.1:8000/

Or

Online demo: https://m-m-blog.herokuapp.com/

## Inspiration

Some parts of code are inspired from:
 - Book: Django 2 by Example by Antonio Mele 
 - Tutorial: https://www.youtube.com/watch?v=xv_bwpA_aEA&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=1&ab_channel=DennisIvy

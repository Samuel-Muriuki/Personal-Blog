# Personal-Blog

## Built By [Samuel Muriuki](https://github.com/Samuel-Muriuki/)

## Description

The Pitch is a web application that displays a list of various news sources. On choosing a pitch category, it will preview that category and give you the option to create another pitch.

You can view the site at:[Heroku](https://samm-blog.herokuapp.com/)

## User Stories

These are the behaviours/features that the application implements for use by a user.

* As a user, I would like to view the blog posts on the site
* As a user, I would like to comment on blog posts
* As a user, I would like to view the most recent posts
* As a user, I would like to an email alert when a new post is made by joining a subscription.
* As a user, I would like to see random quotes on the site
* As a writer, I would like to sign in to the blog.
* As a writer, I would also like to create a blog from the application.
* As a writer, I would like to delete comments that I find insulting or degrading.
* As a writer, I would like to update or delete blogs I have created.

## Specifications

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display random quotes | **On page load** | List of blogs created |


## SetUp / Installation Requirements

### Prerequisites

* Python 3.9.10
* pip
* virtualenv

### Cloning

* In your terminal:

        $ git clone https://github.com/Samuel-Muriuki/Personal-Blog/
        $ cd Pitch

## Running the Application

* Creating the virtual environment

        $ python3.9 -m venv --without-pip env
        $ source env/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.9 -m pip install flask
        $ python3.9 -m pip install flask_Bootstrap
        $ python3.9 -m pip install flask_script


* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application

* To run the tests for the class files:

        $ python3.9 manage.py tests

## Technologies Used

* Python 3.9.10
* Flask 2.0.3
* Werkzeug 2.0.3

## License

MIT License

Copyright (c) [2022] [Samuel-Muriuki]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Go Back to the top](#Personal-Blog)

## Author Bio

Slack Profile - [Samuel-Muriuki](https://app.slack.com/)

[Go Back to the top](#Personal-Blog)

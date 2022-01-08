# 100 Days of Code Pipeline

Hi folks. This is a project I'm working on to help improve my programming and automation skills. I also thought it might be interesting. 

I used to partake in #100DaysOfCode on Twitter. Essentially, this is where one committs to coding everyday for 100 days. To document this, they write something on twitter everyday telling the world what they did using the 100 days of code hashtag.

The aim of this project is to extract the top 100 or so of these tweets, store them in a database, and from this, generate a dashboard displaying interesting statistics. I will then automate this to fetch new tweets every day, week or month. Haven't quite figured out the smaller details, but will work this out as I go along.

I'll document the steps I take below. Note that this is performed on an M1 Mac. Sytax and steps may need to be altered for other OS machines:

1. Create a Twitter developer account. This allows us access to Twitter data through APIs (application programming interfaces). When we sign up, we need to register an **application**. Read more (here](https://help.twitter.com/en/rules-and-policies/twitter-api). 

1. Setup our files and folders. To start with, I created a **tweets.py** file in my project folder where I'll write my API script. I also set up a virtual environment using python's **venv** package. Virtual environments are great as they allow us to contain all the 3rd party libraries we need for a particular project, without interfering with our projects on our local machine. To set this up just type the following into a terminal (make sure you're in your project folder):

```
python -m venv venv
```

We then need to activate it using;

```
source venv/bin/activate
```

Make sure this remains active while working on your project and intstalling new python packages. To deactivate:

```
deactivate
```

You'll know it's activated when `(venv)` shows before the command prompt. 

1. I then installed a couple of libraries:

* Pandas - this is great for data manipulation
* tweepy - this will allow us to connect to the Twitter API

To install, just run:

```
pip install pandas tweepy
```

1. Next up, I created a requirements.txt file, which I'll periodically update. This helps anyone else following along with this project install the same packages as me (so far, pandas and tweepy). To generate this file, I ran `pip freeze` which show all packages I've installed via pip thus far. I then redirected this into a file called **requirements.txt**.

```
pip freeze > requirements.txt
```

If someone wishes to install these libraries, they can add the requirements file to their current directory and run the following:

```
pip install -r requirements.txt
```

1. I then initialised a **git** repo, staged everything I've done this far, and committed:

```
git init
git add .
git commit -m "First Commit"
```

1. Now, for your API, you should have taken note of a a few keys, and setup a Project. Within the project, you'll also need to find the section to create an access token - which will give you an access token and token secret key. These are used to authenticate the user, whereas the API key and API secret key are used to authenticate the app.

Because these should be kept private, I'll store them into a JSON file called `twitter_cred.json`.

1. 



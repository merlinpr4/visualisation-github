
# Visualisation-Github

## Overview :
Check out the data from my github account here :) : https://merlinpr4.github.io/repovisual/

This is a visualisation of metrics from github user's repositories which can be used to help in the software engineering process. 
It pulls data from the Github Rest API ( https://docs.github.com/en/rest).

The backend is written in python3 and is supported by a mongodb database. The frontend is written in HTML,CSS and Javascript with the help of chart.js and bootstrap.

There are two folders API-access and visualise . <br>
The visualise folder contains all relevant files for the actual visualisation of my project <br>
The api-access folder shows my first attempts at interacting with Github API. 

## Motivation :


### Discussion :
I used the professsor videos as a starting point as I was a new to using API or even creating websites.
This was my first time interacting with an API so I had a lot of inital difficulties in trying to access the data I wanted. However I was able to eventually get some interesting data. I was a beginner with using both python and javascript but decided to use both in order to gain experience instead of soley doing it in one language.
I also incorporated a mongoDB database so that if I wanted to gather further information my backend would be organised. 
I spend a lot of time on the visualisation acsept of my project by customising my graphs colorschemes , tooltips etc which was quite fun and I think the end product is great.

## Dependencies
- Python 3
- Pip
- PyGithub
- Docker
- PyMongo

## How to run:
Live version :  https://merlinpr4.github.io/repovisual/

There are bat files available for quick use on windows

### Inital setup
1. Have python 3 installed on laptop
2. git clone this repo
3. Cd into the visualise folder
4. Have pip installed on laptop ( python3 get_pip.py )
5. Install pyGithub on laptop using pip (pip install pyGithub )
6. pip install pymongo
7. cd into visualise folder
8. start mongodb container (docker-compose up)


### Run with personal access token 
1.  Cd into the visualise folder
2.  Go to api.env  and write in your personal access token into the TOKEN (TOKEN = "place-token-here"). <br> If you want to use a username instead replace the NAME = "merlinpr4" with the username you wish to look up but this can get rate limited. If neither is supplied it automatically defaults to my github account.
3.  Type python3 cleardb.py to clear the previous files in the repo and database (clear to run the bat script)
5.  Type python3 getdata.py to access the basic data of the user file and store it in the database (gather  to run the bat script).
6.  Type python3 processdata.py to process the data in the database and create csv files (process to run the bat script).
7.  Type python3 -m http.server to see the visulaisation on localhost:8000 (server)
8. Go to localhost:800 (http://localhost:8000/) to see visualisation.







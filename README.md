
# visualisation-github

Check out the data from my github account here :) https://merlinpr4.github.io/testwebsite/

Trying to access github api using github access token 
Currently able to display users followers in a simple bar chart

Access github api of a specifc user gathers info into mongadb database , create a graph on localhost:8000.

Had a lot of initial difficulty with accessing the data I wanted from the api. Realised it would be better to scale back and gather another data and come back . Spending time accessing meant visualising took a hit

So I struggled with accessing the data I wanted in python and tried switching over to javascript so I could just do the fetching and visualisation as one. However I realised later that after spending all this time on python it is probably better to just stick with using it so Im back to using python to create json files for a logged in user.

Aiming to visualise commits per repo and than see how that goes


### Note :
 Include your own access token as a env variable named TOKEN  
 This is my first time using an API and I am a beginner in python

### Dependencies
Python 3
Pip
PyGithub and requests
Faker
Docker

### run with prefetched data  (data from my github to be exact)
1. Type server.bat
1. Go to localhost:800 (http://localhost:8000/) to see visualisation.


### Inital setup)
1. Have python 3 installed on laptop
2. Have pip installed on laptop ( python3 get_pip.py ) --come back to check if there inital set up instructions are correct)
3. Install pyGithub,Faker on laptop using pip (pip install Faker or install.bat)
4. git clone this repo


### Run with personal access token and fetch new data to display
There are bat files available for easier setup if you are on windows aswell
1.  Go to visualise folder .
1. Start mongadb container container with docker-compose up (start-database.bat/start-database)
3.  Clear the previous files in the repo and database with clear (python3 cleardb.py , clear.bat)
4.  Write your user access token in env file for token (ie TOKEN = useraccesstoken)
5.  Type python3 gather.py to access the basic data of the user file (or gather.bat to run the bat script).
6.  Type python3 process.py to access the data in the database (or process.bat to run the shell script).
7.  Type python3 -m http.server to see the visulaisation on localhost:8000 (or server.bat)
8. Go to localhost:800 (http://localhost:8000/) to see visualisation.

Accessing api simple )
1. Type python3 username.py basic data on the different repos of the user in accessing api folder






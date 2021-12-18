
# visualisation-github
Trying to access github api using github access token 
Currently able to display users followers in a simple bar chart

Access github api of a specifc user gathers info into mongadb database , create a graph on localhost:8000.


### Note :
 Include your own access token as a env variable named TOKEN  
 This is my first time using an API and I am a beginner in python

### Dependencies
Python 3
Pip
PyGithub and requests
Faker
Docker

### Inital setup)
1. Have python 3 installed on laptop
2. Have pip installed on laptop ( python3 get_pip.py ) --come back to check if there inital set up instructions are correct)
3. Install pyGithub,Faker on laptop using pip (pip install Faker or install.bat)
4. git clone this repo
5. Start mongadb container container with docker-compose up (start-database.bat/start-database)


### To run)
There are bat files available for easier setup if you are on windows aswell
6.  Type python3 gather.py to access the basic data of the user file (or gather.bat to run the bat script).
7.  Type python3 process.py to access the data in the database (or process.bat to run the shell script).
8.  Type python3 cleardb.py to clear the database 
9.  Type python3 -m http.server to see the visulaisation on localhost:8000 (or run-server.bat)
10. Go to localhost:800 (http://localhost:8000/) to see visualisation.

Alt run options )
1. Type python3 username.py basic data on the different repos of the user







## Questions from video
1. I realise there will be a video on mon to show how to connect different backend and frontend but I guess I just wanted to check how I am doing so far. My current implementation takes data from github api . I dont exactly know how to put this into a json to send to the .js and html file . Basically how to exactly go about connecting the frontend and backend though I do have ideas such as prefetching the data.
2.  I first want to do something simple for the visulisation such as piechart of a repo of the user and the number of lines of code  in each languge . I then want  do a the number of commits per day in like a bar chart. Once I can do this I want to measure code churn by tracking the number of commits and deletions per day in line graph. Would these be suffient for visualisations ? and do you have any tips or advice ?.
3. Is my current level of access of the github api suffient to get the 20 % ?
4. Will I also be getting marks for writing unit tests for this assigment or is that soley for the gameficiation game ? 
5.  To reiterate I have been able to access the API and I understand how visualisation libraries work. My struggle is currently what way I should connect these components as I have never hosted a website before or did this kind of work . This is also my first time using an API or really python so I guess the struggle is expected.
6.  Also is the deadline for the 3rd of december going to be fixed as I have 4 assigments due for that day or are we allowed to keep working on it afterwords ?

Thank you for any guidance :) 

# visualisation-github
Trying to access github api using github access token 
Currently able to display basic data using a github access token . 



### Note :
 I have not placed my own token in the repo so make sure to add it in when compiling the program.
 This is my first time using an API and I am a beginner in python

### Dependencies
Python 3
Pip
PyGithub and requests

### To run)
1. Have python 3 installed on laptop
2. Have pip installed on laptop
3. git clone this repo
4. Start mongadb container container with up docker-compose
5.  Type python3 script.py to access the basic data of the user file (or sh gather.sh to run the shell script).
6.  Type python3 script2.py to access the data in the database (or sh process.sh to run the shell script).
7.  Type python3 cleardb.py to clear the database 

Alt run options )
1. Type python3 username.py basic data on the different repos of the user

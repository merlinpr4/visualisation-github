
## Questions from video
1. I realise there will be a video on mon to show how to connect different backend and frontend but I guess I just wanted to check how I am doing so far. My current implementation takes data from github api . I dont exactly know how to put this into a json to send to the .js and html file . Basically how to exactly go about connecting the frontend and backend though I do have ideas such as prefetching the data. Im not really sure what mongaDb are or node.js. Theres a lot of information online and I guess I would like a guide on where to start . I think once Im able to connect and do one visualisation I should be ok.
2.  From my understanding prefetch the data could allow me to do quicker visualisations but then am I allowed to limit what users repos you can see . Like just be able to visualise mine and few others? Would this be fine as the data being fetched could be outdated? and limits the users. 
3.  Also wondering about user access tokens for people that arent me as I noticed I can use the username to search but this gets rate limited quickly. This is more for the prefetch stage would this be an issue or would it not matter if I limit the users to a few and just show visualisations for them?
4.   For the visualisation what Id really like to do is be able to search by any github username or access token and show my visualise on that on a website online .
5.   Are we getting marked more on complexity of the visualisation ? on what we are actually measuring or how we deliver that data?
6.  I first want to do something simple for the visulisation such as piechart of a repo of the user and the number of lines of code  in each languge . I then want  do a the number of commits per day in like a bar chart. Once I can do this I want to measure code churn by tracking the number of commits and deletions per day in line graph. Would these be suffient for visualisations ? and do you have any tips or advice ?.
7. Is my current level of access of the github api suffient to get the 20 % ?
8. Will I also be getting marks for writing unit tests for this assigment or is that soley for the gameficiation game ? 
9.  To reiterate I have been able to access the API and I understand how visualisation libraries work. My struggle is currently what way I should connect these components as I have never hosted a website before or did this kind of work . This is also my first time using an API or really python so I guess the struggle is expected.
10.  Also are we expected to unit test our code for api access or is that just for the gamefification score and will it not impact our marks here?
11.  Also is the deadline for the 3rd of december going to be fixed as I have 4 assigments due for that day or are we allowed to keep working on it afterwords ?

Thank you for any guidance I realised I ask quite a few questions . I don't mind also going on a call with a demonstrator if that would help with answering these queries .
My email is prasadme@tcd.ie and my student number is 19333557.

Thank you so much for any help and guidance . :) 


# visualisation-github
Trying to access github api using github access token 
Currently able to display users followers in a simple bar chart




### Note :
 In;cude your own access token as env variable names TOKEN 
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
5.  Type python3 gather.py to access the basic data of the user file (or gather.bat to run the bat script).
6.  Type python3 process.py to access the data in the database (or process.bat to run the shell script).
7.  Type python3 cleardb.py to clear the database 
8.  Type python3 -m http.server to see the visulaisation on localhost:8000 (or run-server.bat)

Alt run options )
1. Type python3 username.py basic data on the different repos of the user

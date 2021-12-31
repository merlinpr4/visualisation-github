
# Visualisation-Github

## Overview :
Check out the data from my github account here : https://merlinpr4.github.io/repovisual/

This is a visualisation of metrics from a github user's repositories which can be used to help in the software engineering process. <br>
It pulls data from the Github Rest API ( https://docs.github.com/en/rest).

There are two folders accessing github api and visualise . <br>
The visualise folder contains all relevant files for the actual visualisation of my project <br>
The api-access folder shows my first attempts at interacting with the Github API aswell as my unit tests.

## Dependencies
- Python 3
- Pip
- PyGithub
- Docker
- PyMongo

## How to run:
Live version :  https://merlinpr4.github.io/repovisual/

There are bat files available for quick use on windows

### Initial  setup
1. Have python 3 installed on laptop
2. git clone this repo
3. Cd into the visualise folder
4. Have pip installed on laptop ( python3 get_pip.py )
5. Install pyGithub on laptop using pip (pip install pyGithub )
6. pip install pymongo
7. cd into visualise folder
8. start mongodb container (docker-compose up)

### Run with prefetched data
1.  Type python3 -m http.server to make the graphs  on localhost:8000 (server to run bat script)
2. Go to localhost:8000 (http://localhost:8000/) to see the visualisation. <br> The webpage should display the previously fetched information

### Run with personal access token 
1.  Cd into the visualise folder
2.  Go to api.env  and write in your personal access token into the TOKEN (TOKEN = "place-token-here"). <br> If you want to use a username instead replace the NAME = "merlinpr4" with the username you wish to look up but this can get rate limited. If neither is supplied it automatically defaults to my github account.
3.  Type python3 cleardb.py to clear the previous files in the repo and database (clear to run the bat script)
5.  Type python3 getdata.py to access the basic data of the user file and store it in the database (gather  to run the bat script).
6.  Type python3 processdata.py to process the data in the database and create csv files (process to run the bat script).
7.  Type python3 -m http.server to make the graphs on localhost:8000 (server to run bat script)
8. Go to localhost:8000 (http://localhost:8000/) to see the visualisation of the data fetched


## Motivation:
I focused my analysis on the github repositories of a user in order to see if I could gain an insight into the user behaviours.
I thought that if I was able to analyse all the repos of a specific user I would notice common attributes as well as see how good of a metric total commits in a repo was in measuring software engineering. I assumed that such metrics could be used to judge how many commits it would take them to do a similar project to one they have already done. I also examined their top repo language to see the users proficiency in different programming languages

## Discussion :
The backend is written in python3 and is supported by a mongodb database with API access done through PYGithub . The frontend is written in HTML and Javascript with the help of chart.js, d3 and bootstrap. <br>
I used the professor's github access through python videos as a starting point. <br>
This was my first time using an API and a database. I was also a beginner in python. I also spend a lot of time on the visualisation aspect as I was a beginner in using chart.js and javascript. Using two programming languages I wasn't familiar with was a struggle at the start but I think it paid off in the end as now I have gained a lot of valuable experience. I focused heavily on the visualisation aspect of the project by making my graphs well labeled, color coordinated and interactive.

### Top language chart
![language chart ](images/languageChart.gif) <br>
By counting only the main language of the repo I could see their proficiency in that language by the number of repos they used it in as well as see what percentage it accounted for in the overall total. I thought measuring this would be more interesting than counting the lines of code of each language used in a repo as some languages are more verbose than others .

### Total Commits barchart
![total commits](images/totalCommitsChart.gif) <br>
This barchart allows the user to easily compare all their repos against each other as well as against the average commits. By adding additional details about the project in the tooltip such as the percentage the commits in this repo account for the total, the size and contributors I think  they could use this graph in order to help estimate how many commits a similar project would take until completion. The chart works best for projects that are started on github and not when fully finished projects are uploaded as the commits here don’t reflect the effort put into the project as it was worked on outside of Github.

### Total Commits vs Size
![commits vs size](images/sizeChart.gif) <br>
The line graphs compare total commits in a repo against total size in order to see if there was a correlation between these two metrics as I would assume the more times you commit the bigger the repo would be. My graph seems to reflect my hypothesis except for some cases such as when a contains a large amount of data in external files like json increasing the size of the repo heavily.

### Total Commits vs Days
![commits vs days](images/daysChart.gif) <br>
I wanted to see how the number of days spent on the repo would affect the total commits of the repo. I calculated the days by counting the days between when the repo was created and its final push . I worked under the assumption that they created a repo at the start of the project and their last commit would be when they were finished. I thought this might be a more interesting metric to analyse than active days as I could also account for days when the user wasn't coding but was still working on the project . Generally the more time spent on the repo the higher the total commits would be.  One issue is that  if the user makes a small change to the repo after a long time has passed it would heavily affect the total days with the current calculation. I think that this graph could be used to gauge how long another similarly difficult project would take the user to complete.

I had originally set out to measure code churn of each repository of the user along with these other repository metrics but I struggled to access this information from the API . If I did this project again I would definitely try to measure that information on top of the data I have already gathered.
Overall this assignment was a lot of fun and really helped me improve and learn multiple new skills. I am proud of the end product and it also helped highlight to me the amount of data software engineers produce along with the advantages and disadvantages that come along with the different metrics one can use to measure it.






# School Funding
 
## Overview
 ### What is this website for?
This website is to show how bad funding is in  some schools and what I'd do to change it.
 ### How does it work?
I have used mongo to get the data from excel and store it on the dashboard. i used a pie chart and a line graph.

## Features
 ### Existing Features
This website has pie charts, line graphs and a table on records on the funding in schools.
 
## Tech Used
 ### Some the tech used includes:
- [Notepad plus](https://notepad-plus-plus.org)
    - We use **Notepad plus** to handle page routing, we also use it to make calls to the REST API and build custom directives
- [mongodb](http://mongo.com/)
    - We use **Mongodb** to retrieve the data from excel and deploy it to heroku
- [heroku](https://www.heroku.com/)
    - We use **heroku** to display the data once the projects complete
- [excel] (Microsoft excel)
      - We use excel to write the data	

 
## Contribution
 ### Getting the code up and running
1.Clone this repository by running the ```git clone <project's Github URL>``` command
2. After you've that you'll need to make sure that you have **npm** and **bower** installed
  1. You can get **npm** by installing Node from [here](https://nodejs.org/en/)
  2. Once you've done this you'll need to run the following command:
     `npm install -g bower # this may require sudo on Mac/Linux`
3. Once **npm** and **bower** are installed, you'll need to install all of the dependencies in *package.json* and *bower.json*
  ```
  npm install
 
  bower install
  ```
4. After those dependencies have been installed you'll need to make sure that you have **http-server** installed. You can install this by running the following: ```npm install -g http-server # this also may require sudo on Mac/Linux```
5. Once **http-server** is installed run ```http-server -c-1```
6. The project will now run on [localhost](http://127.0.0.1:8080)
7. Make changes to the code and if you think it belongs in here then just submit a pull request
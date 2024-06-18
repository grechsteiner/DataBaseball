# Set Up

1. Run `git clone https://github.com/sisixili/baseball-app.git` into your desired local directory
2. Follow the steps outlined in the setupdb README if you have not yet set up the database
3. Install the latest stable version of [Node](https://nodejs.org/en/download/package-manager/). This project uses Express (backend web app framework for RESTful APIs in Node) and React (front end JS library for UI).
4. 3. Create a .env file with your local MySQL db's login info and place it in `baseball-app/server` (DO NOT upload your .env file), for example:
```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=password
MYSQL_DATABASE=baseball-dev
```
5. Run `npm start` from `baseball-app/server`
6. If you run into issues running nodemon, you may have to run the following to update it's permissions: `chmod +x baseball-app/server/node_modules/.bin/nodemon`
7. Open another terminal and run `npm start` from `baseball-app/client`
8. If you run into issues running react-scripts, you may have to run the following to update it's permissions: `chmod +x baseball-app/client/node_modules/.bin/react-scripts`
9. Go to localhost:3000 to access the website. 

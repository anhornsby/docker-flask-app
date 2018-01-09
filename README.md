## A skeleton for building apps on Google App Engine with [Flask](http://flask.pocoo.org), [React](https://facebook.github.io/react/), [Webpack](https://webpack.github.io/) and [Babel](https://babeljs.io/) via Docker.

This repository is dockerized version of https://github.com/AxoSal/GAE-Flask-React-skeleton (though there may be some other differences)

## Run Locally
1. Install Docker on your machine.

2. Clone this repo with

   ```
   git clone https://github.com/anhornsby/docker-flask-app.git
   ```
3. Run 
   ```
   docker build --rm -t docker-flask-app:latest .
   ```

4. Run 
   ```
   docker run -it -p 5000:5000 -v $(pwd):/app docker-flask-app /bin/bash
   ```
   
5. Run 
   ```
   webpack --watch &
   ```
   from comand line so that you can `require` your components and compile .jsx files to .js.
   
4. Run local server from the command line:

   ```
   python main.py y
   ```
   And visit the application on [http://localhost:5000](http://localhost:5000). The `docker run` command connects to port 5000 on your localhost.

For deploying to App Engine, use the Google Cloud SDK *outside* of the container. You do not need to push the Docker container to App Engine, as it will package everything up in a virtual machine for you.

See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver)
for options when running dev_appserver.

## Deploy
To deploy the application:

1. Use the [Admin Console](https://appengine.google.com) to create a
   project/app id. (App id and project id are identical)
1. [Deploy the
   application](https://developers.google.com/appengine/docs/python/tools/uploadinganapp) with

   ```
   appcfg.py -A <your-project-id> update app.yaml
   ```
1. Your application is now live at your-app-id.appspot.com



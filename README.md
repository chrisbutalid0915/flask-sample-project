# flask-book-app
Python Flask Sample Project

## Docker Deployment
1. Run `poetry install --with dev` to install dependencies
2. Run `docker-compose build` to build the docker image
3. Run `docker-compose up -d` to start app and database
4. Run `docker-compose exec web flask db upgrade` to run migrations
5. Browse to http://127.0.0.1:5000/ to see the app running

### API DOCS
Browse to http://127.0.0.1:5000/ to see the API docs.

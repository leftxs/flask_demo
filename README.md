# flask_demo
Flask demo project with auto generated Swagger documentation.

![Flask Demo Screenshot](https://teste-martinho-page.s3-eu-west-1.amazonaws.com/share/flask_demo.png)

## Start Application Instructions

Clone the repo to your local machine by running the command:

git clone https://github.com/pedromartinho/flask_demo

You must have the python installed in your machine. The code presented will consider python3. If you want to use python2 or/and are following this procedure in a Windows machine, please refer to the instructions presented in the [Flask installation guide](https://flask.palletsprojects.com/en/1.1.x/installation/)

After that, go into the folder with the project and create a virtual environment with the following command:

```sh
python3 -m venv venv
```

Active the the respective environment by running:

```sh
. venv/bin/activate
```

**Note:** It might be important to specify the environment you are considering when running this code in your IDE.

Install the projects dependicies with the following command line. This will consider the packages detailed in the requirements.txt file. This is done using [pip]
(https://pypi.org/) (Python package installer):

```sh
pip install -r requirements.txt
````

Before running the application set the Flask environment variables:

```sh
export FLASK_APP=main.py
export FLASK_ENV=development
```

Run Flask... RUN!!

```sh
run flask
```

## Relevant endpoints

The application has three different "modules" presented in detail in the [IC blog post]()

### Basic and classic hello world

Basic endpoints for demo purposes:

* https://flask-ic.herokuapp.com/basic_api/hello_world | GET method
* https://flask-ic.herokuapp.com/basic_api/entities | GET and POST methods
* https://flask-ic.herokuapp.com/basic_api/entities/<entity_id> | GET, PUT and DELETE methods

### Jinja

Example of a Jinja template render with dynamic content change based on query params **top** and **bottom**. This allows you to create your own **Business Cat** meme:

* https://flask-ic.herokuapp.com/jinja_template?top=cancel%20my%203%20o%27clock&bottom=the%20mouse%20is%20moving

### Docummented endpoints

Endpoints created based on the Flask-RESTPlus suggested structure and documentation. All the endpoints previously created are created with a better structure inside the blueprints folder. You can check the generated documentation by refering to this link: https://flask-ic.herokuapp.com/documented_api/doc

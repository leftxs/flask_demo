# flask_demo
Flask demo project with auto generated Swagger documentation 

## Start Application Instructions

Clone the repo to your local machine by running the command:

git clone https://github.com/pedromartinho/flask_demo

You must have the python installed in your machine. The code presented will consider python3. If you want to use python2 or/and are doing following this procedure in a Windows machine, please refer to the instructions presented in the [Flask installation guide](https://flask.palletsprojects.com/en/1.1.x/installation/)

After that, go into the folder with the project and create a virtual environment with the following command:

```sh
python3 -m venv venv
```

After that, activate the respective environment by running:

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

run flask

## Relevant endpoints

The application has three different "modules" presented in detail in the [IC blog post]()

### Basic and classic hello world



### Jinja



### CRUD with swagger documentation


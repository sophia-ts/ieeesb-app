# IEEE Ionian SB app
## Installation 

Must have installed on your computer 
- pip
- python

The required packages exist in the file named "reqirements.txt" To install them run the following command
```
pip install -r requirements.txt
```

If you do not want all the requirements installed in our device feel free to install a *virtual environment*!

## Check linters and fortmatters

- Black: Checks the format of the written code. To check if the code follows the coding standards run:
```
black src
```

- Flake8: Analyze source code looking for problems.To check if the code follows the coding standards run:
```
flake8 src
```

## Run the application

### Migrate
In order to run the application the database table have to be created. To run the necessary migrations go to the subfolder named "src" and run:
```
python manage.py migrate
```

### Make migrations
If there are changes on the models.py files, the changes have to be implemented. To do that, go to the subfolder named "src" and run:
```
python manage.py makemigrations
python manage.py migrate
```
### Super user
In order to gain access to the dashboard, a super user has to be created. To do that, go to the subfolder named "src" and run:
```
python manage.py createsuperuser
```

Give the user a user name and a password and you are good to go. 

Go to "localhost:8000/admin" to access the dashboard to add an event. 

## Run server
To be able to run the application you have to open the server. In order to do that, go to the subfolder named "src" and run:
```
python manage.py runserver
```


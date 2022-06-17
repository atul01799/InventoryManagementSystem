# Inventory Management System

## Introduction
Inventory Management System help us to store and manage all the inventory details in easiest way.

## Requirements and Recommended modules

To get this project up and running you should start by having `Python` installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```
Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

To create a new folder `env` in your project directory and then to activate it with this command on mac/linux/windows terminal:

### For Mac/ Linux
```
virtualenv env
```
```
source env/bin/activate
```
### For Window
```
python -m venv env
```
```
env\scripts\activate
```


## For Installation & configuration
To install all packages use this command on mac/linux/windows terminal:
```
pip install -r requirements.txt
```
## To create those model tables in your database
By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.
```
python manage.py makemigrations
```
The migrate command takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called django_migrations) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.
```
python manage.py migrate
```
migrate command also create a sqlite file if it doesn't exist.
## Deployment
To deploy the project on local server use this command on mac/linux/windows terminal:
```
python manage.py runserver
```
Then to run the project on browser type the following in address bar:
```
127.0.0.1:8000
```
Or
```
localhost:8000
```
## To create admin user
To get admin panel access we need to create superuser:
```
python manage.py createsuperuser
```
To access alredy created admin, use the credentials given below:
```
Username: atul
password: kumar@5236
```
### Access admin panel
```
127.0.0.1:8000/admin
```
Or
```
localhost:8000/admin
```
## TO run the test cases
To run the unit test cases we have to call specific case at once. Use the command given below:
```
python manage.py test inventory.tests.URLTests.homepage 
```
```
python manage.py test inventory.tests.URLTests.inventory_view 
```
```
python manage.py test inventory.tests.URLTests.api 
```


## Troubleshooting

### macOS permissions
If you’re using macOS, you may see the message “permission denied” when you try to run django-admin. This is because, on Unix-based systems like macOS, a file must be marked as “executable” before it can be run as a program. To do this, open Terminal.app and navigate (using the cd command) to the directory where django-admin is installed, then run the command sudo chmod +x django-admin.

### Issue during installation of requirements.txt
In some cases user may found error during installation of some packages of requirements.txt. They can handle it by removing that package name from requirements file and again try to install requirements file.

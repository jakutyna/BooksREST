## BooksREST

This project is a recruitment task for a Python internship. 
The purpose of the project is to create an online
book store based on Django REST framework. 
Application allows users to buy books with 
money deposited on their accounts.

### Used technologies
* __Python 3.8__
* __Django__
* __Django REST__
  
### Used technologies - testing
* __pytest__
* __pytest-django__
* __factory-boy__
* __faker__

### Installation

* Install dependencies from `Pipfile` with `pipenv`:

`pipenv install`

* For development purposes (includes `[dev-packages]` from `Pipfile`):

`pipenv install --dev`

* Start virtualenv:

`pipenv shell`

* Apply migrations (SQLite database used by default - see `settings.py`):

`python manage.py runserver`

* Run Django development server:

`python manage.py runserver`

### Django admin

Django admin was added to the project for easier 
communication with database i.e. for manual testing.

Django admin panel is available under `/admin` endpoint.
For full access to the admin panel create a superuser:

`python manage.py createsuperuser`
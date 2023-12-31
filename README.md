# django-rest-api
A REST api written in Django for people with deadlines

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](https://www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs


## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/MgZayarNaing/learning-management-system.git

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd Django_api
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```
    4. Make admin create user
        ```bash
            $ python manage.py createsuperuser
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```

# Django Api

##  Files API Reference

#### Login (POST)

```https
https://127.0.0.1/api/auth/login
```

| Arguments | Type   | Description                  |
| :-------- | :----- | :--------------------------- |
| username  | string | **Required** admin           |
| password  | string | **Required** superuser       |

####  Files list (GET)

```https
https://127.0.0.1:8000/api/files/all
```
####  Files create (POST)
| Arguments | Description                  |
| :-------- | :--------------------------- |
| name      | **Required**                 |

####  Files view (GET)

```https
https://127.0.0.1:8000/api/files/view/{id}
```
####  Files update (PUT)

```https
https://127.0.0.1:8000/api/files/change/{id}
```
####  Files create (POST)
| Arguments | Description                  |
| :-------- | :--------------------------- |
| name      | **Required**                 |

####  Files delete (DELETE)

```https
https://127.0.0.1:8000/api/files/delete/{id}
```

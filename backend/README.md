# OrionVault Landing page API

### Requirements
* Python3
* PIP
* PostgreSQL (or sqlite3 for development)

### Install
* Create python3 virtual env
```
python3 -m venv venv 
```
* Source into venv
```
source venv/bin/active
```
* Install dependencies
```
pip install -r requirements.txt
```
* cd to the project
```
cd api
```
* Make DB migrations
```
python manage migrate
```
* Run dev server
```
python manage runserver
```

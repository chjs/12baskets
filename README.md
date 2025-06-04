# 열두광주리교회 홈페이지

## Getting Started

### Create a virtual environment 
To create a virtual environment, run the following command in the terminal:
```bash
cd 12baskets/
python3 -m venv venv
source venv/bin/activate
```
To install the packages listed in the file, use the following command:
```bash
pip install -r requirements.txt
```

### Create a file to manage environment variables
Write the environment variables required for running this homepage in the ```.env``` file.
```
DB_NAME=name
DB_USER=id
DB_PASSWORD=password
DB_HOST=host
DB_PORT=port
KAKAO_JS_API_KEY=key
LAT=latitude
LNG=longitude
```

### Apply migrations in Django before running the server
If you’ve made changes to your models or created new ones, generate migration files by running:
```bash
python manage.py makemigrations
```
To apply the migrations to your database, run:
```bash
python manage.py migrate
```
This command updates the database schema according to the migration files.

### Create an admin account in Django
Execute the following command to create a superuser account:
```bash
python manage.py createsuperuser
```
Enter the required information:
1. Username
2. Email address
3. Password

### Start the Development Server
Run the following command to start Django’s built-in development server:
```bash
python manage.py runserver
```
By default, the server will start at http://127.0.0.1:8000/.

# 열두광주리교회 홈페이지

## Getting Started

### Install the necessary packages
```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip
sudo apt install -y postgresql postgresql-contrib libpq-dev
sudo apt install -y nginx
```

### Create a PostgreSQL Database & User
```bash
sudo -i -u postgres
psql
```

```
postgres=# CREATE DATABASE "12baskets_db";
postgres=# CREATE USER "12baskets_user" WITH PASSWORD 'your_strong_password_here';
postgres=# GRANT ALL PRIVILEGES ON DATABASE "12baskets_db" TO "12baskets_user";
```

### Create a virtual environment 
To create a virtual environment, run the following command in the terminal:
```bash
git clone https://github.com/chjs/12baskets.git
cd 12baskets/
python3 -m venv venv
source venv/bin/activate
```
To install the packages listed in the file, use the following command:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Create a file to manage environment variables
Write the environment variables required for running this homepage in the ```.env.dev``` file.
```ini
DJANGO_DEBUG = 1
DJANGO_SECRET_KEY = 'django_secret_key'
DJANGO_ALLOWED_HOSTS = localhost 127.0.0.1 [::1]

# Database configuration
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=dbname
SQL_USER=username
SQL_PASSWORD=password
SQL_HOST=db
SQL_PORT=5432

# Kakao JS API Key for maps (if your pages use Kakao map)
KAKAO_JS_API_KEY=kakao_js_api_key

# Coordinates for map view
MAP_LAT=37.299142
MAP_LNG=126.979092
```
#### Generate a strong ```SECRET_KEY```: You can quickly generate one locally with Python:
```bash
python3 - <<EOF
import secrets
print(secrets.token_urlsafe(50))
EOF
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

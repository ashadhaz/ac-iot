# Backend for IOT systems

#Installation guide

* Please install python 3.4 or above before proceding. Follow these commands.

```
git clone https://github.com/ashadhaz/ac-iot
cd ac-iot
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manag.py runserver
```
* The API will now be accessible at localhost:8000

For checking out the urls, they are present at backend/urls.py

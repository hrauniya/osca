# OSCA_Database
## Quick Start

To get this project up and running locally on your computer:
1. Set up the [Python development environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment).
   We recommend using a Python virtual environment.
2. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):
   ```
   
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py runserver
   ```
5. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.

You can also access it through https://desolate-river-20580.herokuapp.com/accounts/login/?next=/catalog/

and this is the form used to add data to the database https://docs.google.com/forms/d/e/1FAIpQLSd5KIQD-r1UpgBZfgyis5HtAUwXtqgATfj1QEBpP_mHSchL3Q/viewform

Our database models are stored in catals/models.py

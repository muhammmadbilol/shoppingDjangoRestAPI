# variables
python = python
django = $(python) .\manage.py

# commands
admin:
	$(django) createsuperuser

migrate:
	$(django) makemigrations
	$(django) migrate

freeze:
	$(python) -m pip freeze > .\requirements.txt

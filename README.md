# MetaGreenData

## Usage

1. Create a virtual environment.

```
python3 -m venv .venv
```

2. Activate the virtual environment.

```
source .venv/bin/activate
```

3. Install requirements.

```
pip install -r requirements.txt
```

4. Run the Django server.

```
python3 manage.py runserver
```

## Installing new packages

You can install a new package using `pip install <package_name>`. Then freeze 
the same using `pip freeze > requirements.txt`.

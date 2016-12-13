# 6. Tools for APIs

## Requirements

- install python
- install pip https://pip.pypa.io/en/stable/installing/
```
curl https://bootstrap.pypa.io/get-pip.py | python -
```
- install virutalenv
```
pip install virutalenv
```

## Setup

```
# Create a virutal environment for the project
virutalenv .venv
# Activate the virutal environment
source .venc/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Running App

```
python app.py
```

In a browser goto any of
- `http://localhost:5000/api/v1/`
- `http://localhost:5000/api/v1/hello_world`
- `http://localhost:5000/api/v1/hello_world`
- `http://localhost:5000/api/v1/members/`
- `http://localhost:5000/api/v1/members/0`
- `http://localhost:5000/api/v1/members/1`

# 5. Testing and Debugging

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
pip install -r test_requirements.txt
```

## Running Tests
Simply run:
```
nosetests
```

## Running App

```
python app.py
```

In a browser goto any of
- `http://localhost:5000/`
- `http://localhost:5000/error/`

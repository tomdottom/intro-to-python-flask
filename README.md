# 1. The Bare Minimum

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
virutalenv .bm
# Activate the virutal environment
source .bm/bin/activate

# Install dependencies
pip install flask

# or alternatively
pip install -r requirements.txt
```

## Running

```
python app.py
```

In a browser goto `http://localhost:5000`

# 4. Static files & Storage Engines

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

# Initial and empty DB
python init_db.py  # Ignore the warnings about feature deprecration if it appears
```

## Running

```
python app.py
```

In a browser goto `http://localhost:5000`

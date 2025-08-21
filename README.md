# Router → Location Links

This project reads router/locations, and prints unique location-to-location links.  
If two routers in different locations are linked, their locations are considered connected.

# Run

# From local file

```bash
python main.py --file data.json


# From API

python main.py --url https://my-json-server.typicode.com/marcuzh/router_location_test_api/db

# Test code

python -m pytest -q
python -m pytest -v

# Installation

pip install -r requirements.txt


# Example Output

Birmingham Hippodrome <-> Williamson Park
Lancaster Brewery <-> Lancaster University
Lancaster Brewery <-> Loughborough University
Lancaster Castle <-> Loughborough University
```

## Setup

#### plug wires

Needs Python>=3.11.8

```bash
pip3 install -r requirements.txt
```

#### boot servers

```bash
docker compose up # boot the db
source venv/bin/activate
sanic server # start server
```

API doc. can be viewed at `http://localhost:8000/docs`
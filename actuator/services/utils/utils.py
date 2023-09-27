

from fastapi import FastAPI
from uvicorn import Server

from uvicorn.config import Config
from pyctuator.pyctuator import Pyctuator
from uvicorn import run
import requests  # Import requests library for HTTP requests


app_name = "FastAPI App with Pyctuator"
app = FastAPI(title=app_name)


#@app.get("/")
#def hello():
  #  return "Hello World!"


Pyctuator(
    app,
    "FastAPI Pyctuator",
    app_url="http://host.docker.internal:8001",
    pyctuator_endpoint_url="http://host.docker.internal:8001/pyctuator",
    registration_url="http://localhost:8080/instances"
)

#Server(config=(Config(app=app, loop="asyncio"))).run()
if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8001)
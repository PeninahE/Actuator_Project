
from fastapi import FastAPI
from uvicorn import Server
from uvicorn import run
from uvicorn.config import Config
from pyctuator.pyctuator import Pyctuator
import requests  # Import requests library for HTTP requests


#app_name = "FastAPI App with Pyctuator"#app = FastAPI(title=app_name)
app = FastAPI()

@app.get("/hello")
def hello():
    return "Hello World!"


my_pyctuator = Pyctuator(
    app,
    "FastAPI Pyctuator",
    app_url="http://localhost:8000",
    pyctuator_endpoint_url="http://localhost:8000/pyctuator",
    registration_url="http://localhost:8080/instances"
)
#Server(config=(Config(app=app, loop="asyncio"))).run()


@app.get("/peninah")
def hello():
    return ("Hello peninah!")


@app.get("/greetings")
def hello():
    """
    This function receives name of user as payload and greets them
    input param name: str , the  name of the user
    return: greetings: Str , personalized greetings of a user
    """
    return "Greetings {name}!"

if __name__ == "__main__":
   run(app, host="8000", port=8000)



#try:
    # Attempt to register with the "boot-admin" server
  #  registration_response = requests.post("http://localhost:8080/instances")
   # registration_response.raise_for_status()  # Raise an exception if the registration fails
   # print("Registered with boot-admin successfully")
#except requests.exceptions.RequestException as e:
 #   print(f"Failed to register with boot-admin: {e}")






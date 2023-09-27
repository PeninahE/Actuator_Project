


from fastapi import FastAPI
app = FastAPI()




@app.get("/")
async def root():
    return {"message": "Hello Peninah. This is the Actuator Project"}

@app.get("/sum")
async def sum():
    return {"message": "Hello Peninah. This is the sum"}
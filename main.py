from fastapi import FastAPI

app = FastAPI()

print("test ok")

@app.get("/")
def hello():
  return {"message": "hello world!"}

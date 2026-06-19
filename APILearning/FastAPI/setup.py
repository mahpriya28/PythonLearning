# Tip for zsh: quote or escape bracketed extras. Example:
# pip3 install fastapi uvicorn sqlalchemy requests "passlib[bcrypt]" python-jose python-multipart
# ...existing code...

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World!"}
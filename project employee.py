import os
import time
import random
import requests
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/employees/{id}")
def read_employee(id: int):
    return requests.get(f'http://localhost:5000/employees/{id}').json()

@app.post("/employees/")
def create_employee():
    return requests.post('http://localhost:5000/employees/').json()

@app.put("/employees/{id}")
def update_employee(id: int):
    return requests.put(f'http://localhost:5000/employees/{id}').json()

@app.delete("/employees/{id}")
def delete_employee(id: int):
    return requests.delete(f'http://localhost:5000/employees/{id}').json()
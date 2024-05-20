from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"], 
     allow_headers=["*"],
)

students = [
    {"id": 1, "name": "Faker", "age": 20, "address": "T1", "phone": "555-555-5555", "email": "skt1_faker@gmail.com", "class": "Tliet"},
    {"id": 2, "name": "Zeus", "age": 18, "address": "T1", "phone": "555-555-5556", "email": "skt1_zeus@gmail.com", "class": "Tliet"},
    {"id": 3, "name": "Onner", "age": 19, "address": "T1", "phone": "555-555-5557", "email": "skt1_onner@gmail.com", "class": "Tliet"},
    {"id": 4, "name": "Gumayusi", "age": 17, "address": "T1", "phone": "555-555-5558", "email": "skt1_killer@gmail.com", "class": "Tliet"},
    {"id": 5, "name": "Keria", "age": 16, "address": "T1", "phone": "555-555-5559", "email": "skt1_killer@gmail.com", "class": "Tliet"},
]



@app.get("/students")
def get_students():
    return students
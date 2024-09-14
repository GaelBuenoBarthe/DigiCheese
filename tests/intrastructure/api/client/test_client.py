from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.schemas.client import ClientCreate, ClientUpdate,Client
app = FastAPI()



@app.post("/clients/", response_model=Client)
def create_client(client: ClientCreate):
    # Implementation of client creation
    return Client(id=1, name=client.name, email=client.email)

@app.get("/clients/{client_id}", response_model=Client)
def get_client(client_id: int):
    # Implementation to get client by id
    return Client(id=client_id, name="Test Client", email="testclient@example.com")

@app.put("/clients/{client_id}", response_model=Client)
def update_client(client_id: int, client: ClientUpdate):
    # Implementation of client update
    return Client(id=client_id, name=client.name, email=client.email)

@app.delete("/clients/{client_id}", response_model=dict)
def delete_client(client_id: int):
    # Implementation of client deletion
    return {"message": "Client deleted successfully"}

@app.get("/clients/", response_model=List[Client])
def get_all_clients():
    # Implementation to get all clients
    return [Client(id=1, name="Test Client", email="testclient@example.com")]

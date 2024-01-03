from fastapi import FastAPI, HTTPException, Depends
import databases
import asyncpg

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/student_management_db"  # Replace with your PostgreSQL connection details
database = databases.Database(DATABASE_URL)

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    await database.disconnect()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}

@app.get("/user/list")
async def read_item():
    query = "SELECT * FROM users"
    users = await database.fetch_all(query=query)
    if users is None:
        raise HTTPException(status_code=404, detail="Users not found")
    return users

@app.get("/user/details")
async def read_item(user_id: str = None):
    query = "SELECT * FROM users where user_id=:user_id"
    values = {"user_id": user_id }
    user = await database.fetch_one(query=query, values=values)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

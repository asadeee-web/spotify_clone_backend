from fastapi import FastAPI 
from pydantic import BaseModel
app=FastAPI()

class UserCreate(BaseModel):
    name:str
    email:str
    password:str
    


@app.post('/signup')
async def test(user:UserCreate):
    print(user.name)
    print(user.email)
    print(user.password) 
    
    return 'Sign Up Successfully' 
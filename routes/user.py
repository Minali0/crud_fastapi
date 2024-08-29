from fastapi import APIRouter
from config.db import engine
from models.index import users
from schemas.index import User

user = APIRouter()

@user.get("/read_data")
async def read_data():
    with engine.connect() as db:
        user_list = db.execute(users.   select()).fetchall()
        print(user_list)
        user_list_ = list(map(lambda user_list: User(**user_list._mapping), user_list))
        return user_list_

# all elements get with id 
@user.get("/all_data/{id}")
async def read_user_by_id(id: int):
    with engine.connect() as db:
        result = db.execute(users.select().where(users.c.id==id)).fetchall()
        return list(map(lambda result: User(**result._mapping), result))

#insert data
@user.post("/write_data")
async def write_data(user:User):
    with engine.connect() as db:
        db.execute(users.insert().values(
            name = user.name,
            email = user.email,
            password = user.password
        ))
        db.commit()
        user_list = db.execute(users.select()).fetchall()
        print(user_list)
        return list(map(lambda user_list: User(**user_list._mapping), user_list))
        

# update data
@user.put("/{id}")
async def update_data(id:int,user:User):
    with engine.connect() as db:
        db.execute(users.update().where(users.c.id == id).values(
            name=user.name,
            email=user.email,
            password=user.password
        ))
        db.commit()
        updated_list = db.execute(users.select()).fetchall()
        return list(map(lambda updated_list: User(**updated_list._mapping), updated_list))
    
@user.delete("/")
async   def delete_data(id:int):
    with engine.connect() as db:
        db.execute(users.delete().where(users.c.id==id))
        db.commit()
        remaining_users =db.execute(users.select()).fetchall()
        return list(map(lambda remaining_users: User(**remaining_users._mapping), remaining_users))


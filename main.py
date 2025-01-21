from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models.single_user import ResponseData
from models.create_user import CreateUserResponse, CreateUserRequest
from models.update_user import UpdateUserResponse, UpdateUserRequest
from random import randint


app = FastAPI()

@app.get("/api/users/{user_id}", response_model=ResponseData)
def get_user(user_id: int):
    users = {
        2: {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg",
        }
    }

    support_info = {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you.",
    }

    user = users.get(user_id)
    if not user:
        return JSONResponse(status_code=404, content={})

    return {
        "data": user,
        "support": support_info,
    }

@app.post("/api/users", status_code=201, response_model=CreateUserResponse)
def create_user(user: CreateUserRequest):
    user_id = str(randint(1, 999))
    created_at = datetime.utcnow().isoformat() + 'Z'

    response_data = CreateUserResponse(
        name=user.name,
        job=user.job,
        id=user_id,
        createdAt=created_at
    )

    return response_data

@app.put("/api/users/{user_id}")
def put_user(user_id: int, user: UpdateUserRequest):
    updated_at = datetime.utcnow().isoformat() + 'Z'

    response_data = UpdateUserResponse(
        name=user.name,
        job=user.job,
        updatedAt=updated_at
    )

    return response_data

@app.patch("/api/users/{user_id}")
def put_user(user_id: int, user: UpdateUserRequest):
    updated_at = datetime.utcnow().isoformat() + 'Z'

    response_data = UpdateUserResponse(
        name=user.name,
        job=user.job,
        updatedAt=updated_at
    )

    return response_data

@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    return {}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)
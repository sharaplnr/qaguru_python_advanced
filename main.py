from fastapi import FastAPI, HTTPException
from models.single_user import ResponseData

app = FastAPI()

@app.get("/api/users/{user_id}", response_model=ResponseData)
def get_user(user_id: int):
    # Mock data for demonstration purposes
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
        # todo improve exception
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "data": user,
        "support": support_info,
    }


# To run this app, use the following command in your terminal:
# uvicorn filename:app --reload

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
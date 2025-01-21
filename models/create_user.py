from pydantic import BaseModel, Field

class CreateUserRequest(BaseModel):
    name: str
    job: str

class CreateUserResponse(BaseModel):
    name: str
    job: str
    id: str
    created_at: str = Field(alias="createdAt")
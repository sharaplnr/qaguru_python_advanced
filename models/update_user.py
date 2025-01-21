from pydantic import BaseModel, Field

class UpdateUserRequest(BaseModel):
    name: str
    job: str

class UpdateUserResponse(BaseModel):
    name: str
    job: str
    updated_at: str = Field(alias="updatedAt")
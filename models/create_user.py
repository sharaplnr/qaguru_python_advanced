from pydantic import BaseModel, Field

class CreateUserResponse(BaseModel):
    name: str
    job: str
    id: str
    created_at: str = Field(alias="createdAt")
from pydantic import BaseModel, Field

class UpdateUserResponse(BaseModel):
    name: str
    job: str
    updated_at: str = Field(alias="updatedAt")
from pydantic import BaseModel, HttpUrl

class CreateLinkDTO(BaseModel):
    original_url: HttpUrl

class ShowLinkDTO(BaseModel):
    id: int
    original_url: str
    short_code: str
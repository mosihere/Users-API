from pydantic import BaseModel




class User(BaseModel):
    id: int
    username: str
    password: str
    age: int
    city: str
    country: str
    gender: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
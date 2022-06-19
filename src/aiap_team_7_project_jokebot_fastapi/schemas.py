import typing
import pydantic


class Review(pydantic.BaseModel):
    id: int
    text: str


class MovieReviews(pydantic.BaseModel):
    reviews: typing.List[Review]


class InferJoke(pydantic.BaseModel):
    joke: str


class PreGenText(pydantic.BaseModel):
    text: str

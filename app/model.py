from redis_om import Field
from aredis_om import HashModel
from pydantic import BaseModel


class Result(BaseModel):
    home_goal: int = Field(index=False)
    away_goal: int = Field(index=False)


class Coupon(HashModel):
    my_bet: int = Field(index=False)

    home: str = Field(index=True)
    away: str = Field(index=True)
    odd: float = Field(index=False)

    home_goal = Field(default="-")
    away_goal = Field(default="-")

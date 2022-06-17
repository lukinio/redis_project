from fastapi import APIRouter, status, HTTPException
from app.model import Coupon, Result
from app.utils import get_logger
from aredis_om import NotFoundError


logger = get_logger(__name__)
app_routes = APIRouter(prefix="/api/v1", tags=["coupons"])


async def get_coupon(pk: str):
    coupon = await Coupon.get(pk)

    return {
        "id": coupon.pk,
        "my_bet": coupon.my_bet,
        "home": coupon.home,
        "away": coupon.away,
        "odd": coupon.odd,
        "home_goal": coupon.home_goal,
        "away_goal": coupon.away_goal
    }


@app_routes.get("/coupons/{pk}", status_code=status.HTTP_200_OK)
async def get_coupon(pk: str):
    try:
        return await Coupon.get(pk)
    except NotFoundError:
        return HTTPException(status_code=404, detail="Coupon not found")


@app_routes.get("/coupons", status_code=status.HTTP_200_OK)
async def get_all_coupons():
    return [await get_coupon(pk) async for pk in await Coupon.all_pks()]


@app_routes.post("/coupons", status_code=status.HTTP_201_CREATED)
async def create_coupon(data: Coupon):
    return await data.save()


@app_routes.delete("/coupons/{pk}")
async def delete_coupon(pk: str):
    return await Coupon.delete(pk)


@app_routes.put("/coupons/{pk}", status_code=status.HTTP_200_OK)
async def update_coupon(pk: str, result: Result):
    try:
        old_coupon = await Coupon.get(pk)
        old_coupon.home_goal = result.home_goal
        old_coupon.away_goal = result.away_goal
        return await old_coupon.save()
    except NotFoundError:
        return HTTPException(status_code=404, detail="Coupon not found")

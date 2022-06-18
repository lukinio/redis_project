import json
import requests
from utils import get_logger

logger = get_logger(__name__)

with open("data/coupons.json") as f:
    coupons = json.load(f)

for coupon in coupons:
    r = requests.post("http://127.0.0.1:8080/api/v1/coupons", data=json.dumps(coupon))
    logger.info(f"created coupon: {coupon}")

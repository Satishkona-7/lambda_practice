from dotenv import load_dotenv
import json

load_dotenv("lambda1/.env")

from common.config import get_config
from common.logger import get_logger

logger = get_logger(__name__)


def lambda_handler(event, context):

    config = get_config()

    name = "Guest"

    if event.get("queryStringParameters"):
        name = event["queryStringParameters"].get(
            "name",
            "Guest"
        )

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "app": config["APP_NAME"],
            "message": config["MESSAGE"],
            "user": name
        })
    }
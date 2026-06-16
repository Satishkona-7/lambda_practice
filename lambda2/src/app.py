from dotenv import load_dotenv
import json

load_dotenv("lambda2/.env")

from common.config import get_config


def lambda_handler(event, context):

    config = get_config()

    a = int(event.get("a", 0))
    b = int(event.get("b", 0))

    result = a + b

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "app": config["APP_NAME"],
            "message": config["MESSAGE"],
            "a": a,
            "b": b,
            "result": result
        })
    }
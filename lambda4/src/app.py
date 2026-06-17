from dotenv import load_dotenv
import json

load_dotenv("lambda4/.env")

from common.config import get_config


def lambda_handler(event, context):

    config = get_config()

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "app": config["APP_NAME"],
            "message": config["MESSAGE"],
            "status": "healthy",
            "version": "1.0.0"
        })
    }
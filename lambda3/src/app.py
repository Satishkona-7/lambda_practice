from dotenv import load_dotenv
import json
from datetime import datetime

load_dotenv("lambda3/.env")

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
            "current_time": datetime.utcnow().isoformat()
            "environment": "dev",
            "version": "2.0"
        })
    }
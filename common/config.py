import json
import os

import boto3


def get_config():

    if os.getenv("ENVIRONMENT") == "local":

        return {
            "APP_NAME": os.getenv("APP_NAME"),
            "API_KEY": os.getenv("API_KEY"),
            "MESSAGE": os.getenv("MESSAGE")
        }

    secret_name = os.environ["SECRET_NAME"]

    client = boto3.client("secretsmanager")

    response = client.get_secret_value(
        SecretId=secret_name
    )

    return json.loads(response["SecretString"])
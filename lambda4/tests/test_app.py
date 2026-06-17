from lambda1.src.app import lambda_handler


def test_lambda():

    response = lambda_handler({}, {})

    assert response["statusCode"] == 200
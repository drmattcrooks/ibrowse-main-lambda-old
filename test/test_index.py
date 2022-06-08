from src.index import lambda_handler


def test_lambda_returns_dict():
    assert type(lambda_handler(1, 2)) == dict
import json
# import numpy as np

print("loading lambda")


def lambda_handler(event, context):
    question = "A question"
    return {
        'statusCode': 200,
        'question': question,
        'body': json.dumps({'Matt Says': f'A Random Number: {1}'})
    }

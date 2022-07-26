import json
import boto3

def translate(phrase):
    client = boto3.client('translate', region_name='us-east-1')
    result = client.translate_text(Text=phrase, SourceLanguageCode="auto", TargetLanguageCode="en")
    text = result['TranslatedText']
    return text

def lambda_handler(event, context):
    # check that the request has some input body
    if 'body' in event:
        event = json.loads(event["body"])
    # get phrase"
    payload_phrase = event["phrase"]
    trans = translate(payload_phrase)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "English": trans
            }
        ),
    }

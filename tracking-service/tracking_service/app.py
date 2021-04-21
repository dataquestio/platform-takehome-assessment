import json

EVENTS_TABLE = "events"

TERMINAL_COLOR = "\033[94m"
TERMINAL_ENDC = "\033[0m"


def db_insert(tracking_event):
    """
    Stub function representing insertion of event in database.

    In order to simplify the exercise, we are not connecting to a real
    database. Instead we'll print the row that should be inserted.

    Args:
        tracking_event (dict): The event data which we should insert into the database.
    """
    columns = list(tracking_event.keys())
    values_str = ",".join(
        [
            f"'{tracking_event[col]}'"
            if type(tracking_event[col]) not in (int, float)
            else f"{tracking_event[col]}"
            for col in columns
        ])
    #### QUESTION 3 REFERENCE
    sql = f"INSERT INTO {EVENTS_TABLE} ({','.join(columns)}) VALUES ({values_str})"
    # instead of executing the SQL, let's just print it!
    print(f"{TERMINAL_COLOR}{sql}{TERMINAL_ENDC}")


def lambda_handler(event, context):
    """Lambda function handler for tracking event data insertion.

    Args:
        event (dict): API Gateway Lambda Proxy Input Format
            Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
        context (object): Lambda Context runtime methods and attributes
            Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns:
        dict: API Gateway Lambda Proxy Output Format
            Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    body = json.loads(event.get("body", "{}"))
    event_name = body.pop("event")
    user = body.pop("user")
    location = body.pop("location")
    tracking_event = {
        # some data from the request itself
        "id": event["requestContext"]["requestId"],
        "ip": event["requestContext"]["identity"].get("sourceIp"),
        "user_agent": event.get("headers", {}).get("User-Agent"),
        # common parameters (required on every event) get their own field
        "event": event_name,
        "user": user,
        "location": location,
        "received_at": event["requestContext"].get("requestTime"),
        # remaining parameters are stored in a json field in the DB
        "extra": json.dumps(body)
    }
    db_insert(tracking_event)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Success!",
        }),
    }

from datetime import datetime, timezone
from html import escape

def lambda_handler(event, context):
    # 1. Read the name from the web address: ...?name=Polina
    params = event.get("queryStringParameters") or {}
    name = escape(params.get("name", "students"))
    # 2. Find out the time and the ID of this call
    time = datetime.now(timezone.utc).strftime("%H:%M:%S UTC")
    request_id = context.aws_request_id[:8]
    # 3. Build a small web page (HTML)
    page = (f"<h1>Hello, {name}!</h1>"
            f"<p>Made by AWS Lambda at {time}, request {request_id}</p>")
    # 4. Send the page back to the browser
    return {"statusCode": 200,
            "headers": {"Content-Type": "text/html; charset=utf-8"},
            "body": page}

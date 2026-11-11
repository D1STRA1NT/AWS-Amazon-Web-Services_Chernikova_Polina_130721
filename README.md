# Amazon Web Services (AWS)

A presentation about AWS for the course **Cloud and Fog Computing**, with a small AWS Lambda demo in Python.

**Author:** Polina Chernikova, group 1307
**Date:** November 2026
**Language:** English

## Repository contents

| File | What it is |
| --- | --- |
| `Amazon_Web_Services_AWS.pdf` | The presentation (19 slides) |
| `lambda_function.py` | The AWS Lambda function used in the demo (17 lines of Python) |
| `README.md` | This file |

## Presentation outline

About 20–22 minutes of talk and 4–5 minutes of demo.

| # | Slide | Main idea |
| --- | --- | --- |
| 1 | Amazon Web Services (AWS) | Title |
| 2 | Own servers vs the cloud | Cost, speed, growth and repairs compared |
| 3 | Amazon Web Services in short | Started in 2006, 200+ services, 39 Regions, 123 Availability Zones |
| 4 | AWS is the market leader | Market share Q3 2026: AWS 26%, Azure 19%, Google Cloud 16% |
| 5 | How AWS is built around the world | Regions, Availability Zones, edge locations |
| 6 | How AWS keeps an app running | Elastic Load Balancing, Auto Scaling, Multi-AZ database |
| 7 | Three service models | IaaS, PaaS, SaaS and who manages what |
| 8 | Six services to know first | EC2, Lambda, S3, RDS, DynamoDB, CloudFront |
| 9 | How the services work together | Example: an online shop with no server to manage |
| 10 | Security is a shared job | Shared responsibility model, IAM, VPC |
| 11 | AI on AWS | Amazon Bedrock and Amazon SageMaker |
| 12 | Cloud vs fog computing | IoT Greengrass, Outposts, Local Zones, Wavelength |
| 13 | How you pay for AWS | On-Demand, Savings Plans, Spot, Free Tier |
| 14 | Who uses AWS and what for | Netflix and common use cases |
| 15 | Strengths and weaknesses | Pros, cons, the October 2025 outage |
| 16–18 | Demo: How AWS Lambda works | Steps, code, request flow |
| 19 | Key takeaways | Summary |

## Demo: a web page with no server

The demo shows a small serverless app. The function returns a web page that says hello, with the current time and the unique ID of the call.

The demo is explained step by step on slides 16–18. It is not run live, because creating an AWS account requires a bank card.

### The code

```python
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
```

### How it works

1. A person opens the function's web address (Function URL), for example with `?name=Polina` at the end.
2. AWS turns the request into the `event` dictionary and calls `lambda_handler`.
3. The function reads the name, gets the time and the request ID, and builds the HTML page. `escape` protects the page from HTML code in the address.
4. AWS sends the response to the browser, which shows **Hello, Polina!**

Every refresh starts the code again, so the time and the request ID change. When nobody opens the page, the code does not run and costs nothing.

### How to deploy it on AWS

You need an AWS account.

1. Open the AWS console → **Lambda** → **Create function** → **Author from scratch**.
2. Enter a name (for example `hello-demo`) and choose a **Python** runtime.
3. Paste the code into `lambda_function.py` and click **Deploy**.
4. Go to **Configuration** → **Function URL** → **Create function URL**, choose auth type **NONE** and save.
5. Open the URL in a browser. Add `?name=YourName` to the end of the address.

### How to test it locally (no AWS account needed)

The function needs no external libraries. This command calls it the same way AWS does, with a test event and a fake request ID:

```bash
python3 -c "import uuid, types, lambda_function as f; print(f.lambda_handler({'queryStringParameters': {'name': 'Polina'}}, types.SimpleNamespace(aws_request_id=str(uuid.uuid4()))))"
```

Expected output (the time and the ID will differ):

```
{'statusCode': 200, 'headers': {'Content-Type': 'text/html; charset=utf-8'}, 'body': '<h1>Hello, Polina!</h1><p>Made by AWS Lambda at 07:29:20 UTC, request 7ab932a5</p>'}
```

## Sources

- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [AWS Free Tier](https://aws.amazon.com/free)
- [AWS Lambda: building functions with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)
- [AWS Lambda: Function URL access control](https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html)
- Synergy Research Group, cloud market data for Q3 2026

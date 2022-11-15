# serverless 🚀
Learning about serverless options for Python like AWS Lambda

## What is serverless for?

For short running tasks, like a stateless web service (often reffered to as [RESTful API](https://aws.amazon.com/what-is/restful-api/)) a call to the serverless function will spin up a machine, perform the task and turn off the machine. The task might be receiving data through the call to a simple public URL (also called the API Gateway) or fetch data from a bucket. It would then compute your code. And it will save or return the results before shutting down the machine. As such, you don't need to manage the server running your code in serverless mode.

## What it is not

For serving web assets, consider a content delivery network (CDN). Amazon CloudFront is an AWS service built specifically for this purpose. Her is a guide on how to use it with S3 and other options: [Using various origins with CloudFront distributions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistS3AndCustomOrigins.html)

## Chalice

![](https://aws.github.io/chalice/_static/img/chalice-logo-icon-small.png)

repo: [aws/chalice](https://github.com/aws/chalice) - website: [aws.github.io/chalice/](https://aws.github.io/chalice/)

---

First create a virtual environment
```
python -m venv env
.\env\Scripts\activate
```
Once activated, install Chalice
```
(env) pip install -r requirements.txt
```
Then create a new project:
```
chalice new-project helloworld
```

Move to the created project folder:
```
cd helloworld
code app.py
```

Create a simple REST API:
```python
from chalice import Chalice

app = Chalice(app_name="helloworld")

@app.route("/")
def index():
    return {"hello": "world"}
```


## Resources

* [serverless/examples](https://github.com/serverless/examples/)
* [examples/aws-python-flask-api](https://github.com/serverless/examples/tree/master/aws-python-flask-api)
* [Tutorial Serverless](https://newrelic.com/blog/best-practices/create-a-serverless-function-in-python)

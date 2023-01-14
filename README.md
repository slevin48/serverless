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

Simply deploy the lambda function:
```
chalice deploy
```

Delete the function once you stop playing:
```
chalice delete
```


### Tuto video
[streamlit-streamlit_app-2022-11-14-22-11-15.webm](https://user-images.githubusercontent.com/12418115/201817792-1ea00a76-aa99-468e-96f7-2b7217add872.webm)

Call REST API from Postman 
![image](https://user-images.githubusercontent.com/12418115/201817921-999befd8-f69c-4d36-a02f-010c7b127851.png)

Finally the Lambda function can be managed from the AWS console:
![image](https://user-images.githubusercontent.com/12418115/201818285-4977245a-0c56-4e9b-8f7a-9d9f664bda4e.png)

## Deploy serverless container with Fargate
https://github.com/slevin48/fargate

## Resources

* [serverless/examples](https://github.com/serverless/examples/)
* [examples/aws-python-flask-api](https://github.com/serverless/examples/tree/master/aws-python-flask-api)
* [Tutorial Serverless](https://newrelic.com/blog/best-practices/create-a-serverless-function-in-python)
* [Running TensorFlow on AWS Lambda using Serverless](https://medium.com/@mike.p.moritz/running-tensorflow-on-aws-lambda-using-serverless-5acf20e00033)
* [RealPython Tutorial](https://realpython.com/aws-chalice-serverless-python/)
* [Using Chalice to serve SageMaker predictions](https://julsimon.medium.com/using-chalice-to-serve-sagemaker-predictions-a2015c02b033)
*[AWS Chalice — Painless Serverless Adventure](https://awstip.com/aws-chalice-painless-serverless-adventure-2-a7aa5f93840f) - [last part (in turkish)](https://kemalcanbora.medium.com/aws-chalice-ac%C4%B1s%C4%B1z-serverless-ser%C3%BCveni-3-61a57d9a248e)

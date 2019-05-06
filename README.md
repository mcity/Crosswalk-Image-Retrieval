# Crosswalk Image Retrieval.
Fetches an image from a get endpoint and uploads it to an S3 Bucket.

### Installation
Built for Python 3.x.

```sh
$ brew install python3
```

Create a virtual env and install dependencies 
```sh
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Copy the env_sample to .env and configure it as needed for your system.
```sh
$ cp env_sample .env
```

Startup script:
```sh
$ python run.py
```

### Deployment

Schedule as a Lambda or with cron on an EC2 instance.

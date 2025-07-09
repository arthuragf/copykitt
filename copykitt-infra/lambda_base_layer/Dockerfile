FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt .

RUN yum install -y zip

RUN pip install -r requirements.txt -t python/

RUN zip -r layer.zip python/
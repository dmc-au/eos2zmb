FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install lazyqsar==0.3

WORKDIR /repo
COPY . /repo

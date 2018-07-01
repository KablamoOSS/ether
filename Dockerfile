FROM alpine:latest
ENV http_proxy ${http_proxy}
ENV https_proxy ${https_proxy}

RUN apk add --no-cache python && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools && \
    rm -r /root/.cache

COPY ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

WORKDIR /opt/app
COPY ./src /opt/app/
WORKDIR /opt/app
ENTRYPOINT ["invoke"]

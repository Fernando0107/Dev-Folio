# Drone CI test.
#
#     docker build --rm=true -t Fernando0107/my-plugin .

FROM gliderlabs/alpine:3.2
MAINTAINER Fernando Gonzalez <rmfernando@outlook.com>

RUN apk-install python3
RUN mkdir -p /opt/drone
COPY requirements.txt /opt/drone/
WORKDIR /opt/drone
RUN pip3 install -r requirements.txt
COPY plugin /opt/drone/

ENTRYPOINT ["python3", "/opt/drone/plugin/main.py"]

FROM ubuntu:latest
LABEL authors="ASF"

ENTRYPOINT ["top", "-b"]
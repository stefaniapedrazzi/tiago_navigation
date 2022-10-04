FROM stpedrazzi/opendr-on-webots-cloud:latest
ARG PROJECT_PATH
RUN mkdir -p $PROJECT_PATH
COPY . $PROJECT_PATH

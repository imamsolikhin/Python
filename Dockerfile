# Use an official Python runtime as an image
FROM alpine:3.12

## make a local directory
RUN mkdir /api_telnet_noc

RUN apk --update add bash nano

# set "flask_app" as the working directory from which CMD, RUN, ADD references
WORKDIR /api_telnet_noc

# now copy all the files in this directory to /flask_app
ADD . /api_telnet_noc

# install mysql-client
#RUN apt-get update && apt-get install --no-install-recommends -y mysql-client

# pip install the local requirements.txt
RUN pip install -r reqs.txt

CMD export FLASK_APP=run.py
CMD flask run -h 0.0.0.0 -p 9999

# Listen to port 9999 at runtime
EXPOSE 9999

# Define our command to be run when launching the container
ENTRYPOINT /api_telnet_noc/run.sh

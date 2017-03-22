FROM python:2.7

RUN mkdir /app

#we add this line so the docker build cache doesnt skip this if new requirements are added
ADD ./app/requirements.txt /app/requirements.txt

#now install our requirments
RUN pip install -r /app/requirements.txt

#add the app directory
ADD ./app /app

#lets get away from root user and make our own
RUN adduser --uid 1000 --disabled-password --gecos '' onefastpython && \
    chown -R onefastpython:onefastpython /app
USER onefastpython
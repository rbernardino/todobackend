FROM ryanbernardino/todobackend-base:latest
LABEL Author='Ryan Bernardino <r.bernardino17@gmail.com>'

# Install dev/build dependencies
RUN apt-get update && \
    apt-get install -qy python3-dev libmysqlclient-dev gcc

# Activate virtual environment and install wheel support
RUN . /appenv/bin/activate && \
    pip install wheel --upgrade

# PIP environment variables (NOTE: must be set after installing wheel)
ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache

# OUTPUT: Build artifacts (Wheels) are output here
VOLUME /wheelhouse

# OUTPUT: Test reports are output here
VOLUME /reports

# OUTPUT: Build cache shared by the 'test' and 'builder' service
# This is where 'test.sh' entrypoint script download the application requirements
VOLUME /build

# Add test entrypoint script
COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

# Set defaults for entrypoint and command string
ENTRYPOINT [ "test.sh" ]
CMD [ "python", "manage.py", "test", "--noinput" ]

# Add application source
COPY src /application
WORKDIR /application



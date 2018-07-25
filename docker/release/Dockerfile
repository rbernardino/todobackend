FROM jmenga/todobackend-base:latest
LABEL Author='Ryan Bernardino <r.bernardino17@gmail.com>'

# Copy application artifacts
COPY target /wheelhouse

# Install application
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse todobackend && \
    rm -rf /wheelhouse

FROM python:3
RUN apt-get install coreutils

COPY . .
RUN pip install pandas

CMD echo "Date and Time $(date)" && \
    echo "User: $(whoami)" && \
    echo "Hello, ${ENV_NAME}"; python app.py

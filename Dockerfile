FROM python:3

RUN pip install tldr

COPY main.py ./
EXPOSE 8000

CMD [ "python","./main.py" ]

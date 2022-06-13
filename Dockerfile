FROM python:3.9
COPY . /drunk_bot
WORKDIR /drunk_bot
RUN pip install -r requirements.txt
CMD python bot_core.py
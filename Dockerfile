FROM python:3.9.18

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY llama-2-7b-chat.Q2_K.gguf llama-2-7b-chat.Q2_K.gguf
COPY main.py main.py

CMD [ "python", "main.py" ]
EXPOSE 5000
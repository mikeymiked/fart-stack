FROM python:3.8-slim-buster
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt && apt update && apt install nodejs -y && apt install npm -y && npm install -g typescript
COPY . .
RUN cd static/js && tsc app.ts
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

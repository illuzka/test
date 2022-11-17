FROM python:3.9.15-slim

COPY reqs.txt reqs.txt
RUN pip3 install -r reqs.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
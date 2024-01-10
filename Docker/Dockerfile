FROM python:3.9
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 3005
CMD ["python", "app.py"] 

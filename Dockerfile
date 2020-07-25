FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV PORT 5000
EXPOSE 5000
CMD [ "python", "data-input.py" ]
ENTRYPOINT [ "python", "app.py"]

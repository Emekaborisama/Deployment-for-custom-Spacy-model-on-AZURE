
FROM python:3.8
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
#RUN python -m spacy download en_core_web_sm
RUN python app/load_model.py
ENTRYPOINT ["./gunicorn.sh"]
# CMD ["python", "main.py"]
EXPOSE 8080


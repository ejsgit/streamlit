FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r ./app/requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "exemple.py"]
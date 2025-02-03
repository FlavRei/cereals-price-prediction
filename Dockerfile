FROM python:3.9

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry install --no-root

COPY . .

EXPOSE 8501
CMD ["poetry", "run", "streamlit", "run", "app_streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]

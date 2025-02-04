FROM python:3.10

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry && poetry install --no-root

COPY . .

EXPOSE 8080
CMD ["poetry", "run", "streamlit", "run", "app_streamlit.py", "--server.port=8080", "--server.address=0.0.0.0"]

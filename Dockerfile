FROM python:3.10

WORKDIR /app

COPY pyproject.toml poetry.lock ./

COPY . .

EXPOSE 8080
CMD ["poetry", "run", "streamlit", "run", "app_streamlit.py", "--server.port=8080", "--server.address=0.0.0.0"]

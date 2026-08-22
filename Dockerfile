FROM python:3.12-slim
WORKDIR /srv
COPY bin/ bin/
COPY app/ app/
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["python", "bin/sync.py", "--root", "app", "--port", "8000"]

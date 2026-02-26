FROM python:3.9-slim

# Копируем скрипт сервера в контейнер
COPY app.py /app/app.py

# Указываем рабочую директорию
WORKDIR /app

# Открываем порт 8080 внутри Docker-сети
EXPOSE 8080

# Запускаем сервер при старте контейнера
CMD ["python", "app.py"]
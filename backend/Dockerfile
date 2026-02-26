FROM python:3.9-slim

# Копируем скрипт сервера в контейнер
COPY server.py /app/server.py

# Указываем рабочую директорию
WORKDIR /app

# Открываем порт 8080 внутри Docker-сети
EXPOSE 8080

# Запускаем сервер при старте контейнера
CMD ["python", "server.py"]

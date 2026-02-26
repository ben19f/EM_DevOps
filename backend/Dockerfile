FROM python:3.9-slim
#add user
RUN groupadd -r efmobile && useradd -r -g efmobile efmobileuser

# Установка curl для healthcheck
RUN apt-get update && apt-get install -y curl

COPY app.py /app/app.py

WORKDIR /app
#смена юзера
USER efmobileuser

EXPOSE 8080

#HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
#  CMD curl -f http://localhost:8080 || exit 1

CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "8080"]
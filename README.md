# тестовое Effective Mobile

простое backend-приложение на Python,
доступное пользователю через Nginx (reverse proxy),
запущенные в Docker-контейнерах.

---
## Структура проекта (по ТЗ)


├── backend/ 

│   ├── Dockerfile

│   └── app.py

├── nginx/

│   ├── Dockerfile

│   └── nginx.conf

├── docker-compose.yml

└── README.md


## Запуск 

### 1. Клонировать репозиторий
````
git clone <repo_url>
cd <repo_name>
````
(если на пк старый докер до разкомментировать номер версии в докеркомпос)
(если сеть уже существует раскомментировать последнийраздел в докеркомпос и закомментировать создание сети)
### 2. Собрать и запустить контейнеры

```
docker compose up --build
````

## ✅ Проверка работоспособности

Выполнить:
````
curl http://localhost
````
Ожидаемый ответ:

Hello from Effective Mobile!

---

## Архитектура

Client
   
↓

Nginx (port 80)

   ↓

Backend (port 8080, доступен только внутри docker-сети)

### Как это работает:

1. Пользователь обращается к http://localhost
2. Запрос попадает в контейнер nginx
3. Nginx проксирует запрос к backend-сервису по имени сервиса внутри Docker-сети
4. Backend возвращает текстовый ответ

---

## Используемые технологии

* Docker
* Docker Compose
* Nginx (official image)
* Python 3 (http.server)
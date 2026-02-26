FROM nginx:alpine

# Удаляем дефолтную конфигурацию
RUN rm /etc/nginx/conf.d/default.conf

# Копируем кастомный конфиг
COPY nginx.conf /etc/nginx/nginx.conf

# Выключаем доступ к логам извне
RUN rm -f /var/log/nginx/access.log /var/log/nginx/error.log

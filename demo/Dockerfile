ARG registry_url=192.168.1.1/ak/base
FROM $registry_url
COPY . /app
WORKDIR /app
CMD ["supervisord","-n", "-c", "/app/supervisord_docker.conf"]

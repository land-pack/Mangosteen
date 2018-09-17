FROM 192.168.1.1:7900/ak/base
COPY . /app
WORKDIR /app
CMD ["supervisord","-n", "-c", "/app/supervisord_docker.conf"]

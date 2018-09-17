FROM 106.75.63.5:7900/ak/base
COPY . /app
WORKDIR /app
CMD ["supervisord","-n", "-c", "/app/supervisord_docker.conf"]

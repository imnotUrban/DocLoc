FROM mariadb:latest

ENV MYSQL_ROOT_PASSWORD=1234
ENV MYSQL_DATABASE=storedb
ENV MYSQL_USER=administrador
ENV MYSQL_PASSWORD=1234

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306


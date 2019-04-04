# SETUP

Build the image
```
docker build . -t morpheus-certificates
```

Run the image in container
```
docker run -d morpheus-certificates \
    -e MYSQL_HOST 127.0.0.1 \
    -e MYSQL_PORT 3306 
    -e MYSQL_USERNAME username \
    -e MYSQL_PASSWORD password \
    -e MYSQL_DATABASE morpheus-certificates \
    -e SECRET_KEY secret \
    -e LOGIN_USERNAME username \
    -e LOGIN_PASSWORD password
```
Default login ist `admin`, `admin` 

## Port
The port where the server gets bind is `5000`

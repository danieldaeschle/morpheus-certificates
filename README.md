# SETUP

Build the image
```
docker build . -t morpheus-certificates
```

Run the image in container
```
docker run -d morpheus-certificates \
    -e MYSQL_HOST 127.0.0.1 \
    -e MYSQL_USERNAME cert \
    -e MYSQL_PASSWORD cert \
    -e MYSQL_DATABASE morpheus-certificates \
    -e SECRET_KEY secret
```

## Port
The port where the server gets bind is `5000`

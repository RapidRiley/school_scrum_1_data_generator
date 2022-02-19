$PORT=4000

docker build -t data_generator `
    --build-arg DATA_DIR="/data" `
    --build-arg SERVER_PORT=${PORT} .

if($?)
{
    docker run --rm -td data_generator
}
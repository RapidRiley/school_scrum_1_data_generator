$PORT=4000

docker build -t generator `
    --build-arg DATA_DIR="/data" `
    --build-arg SERVER_PORT=${PORT} .

if($?)
{
    docker run -td generator
}
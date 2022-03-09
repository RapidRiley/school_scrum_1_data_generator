$PORT=4000

docker volume create --name cern_data

docker build -t school_1_scrum_data_generator `
    --build-arg DATA_DIR="/data" `
    --build-arg SERVER_PORT=${PORT} .

if($?)
{
    docker run -d --mount 'type=volume,src=cern_data,dst=/data' --name school_1_scrum_data_generator -t school_1_scrum_data_generator
}
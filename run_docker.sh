# export $(cat .env | xargs)

if [ "$1" = "start" ]; then
  docker compose up --build -d --remove-orphans
elif 
  [ "$1" = "stop" ]; then
  docker compose down
else
  echo "No option (start, stop) provided!"
  exit 1
fi
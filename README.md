#Containerized tldr HTTP service

1. How to build
docker build -t tldr .

2. How to run
docker run -p 8000:8000 --name tldr tldr
   
3. How to use
curl --location --request GET "http://localhost:8000/rm"

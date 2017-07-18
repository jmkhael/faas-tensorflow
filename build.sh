docker build -t jmkhael/faas-tensorflow .
docker service rm tensorflow
faas-cli -action deploy -f tensorflow.yml
docker service logs -f tensorflow

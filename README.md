This sample [FaaS](https://github.com/alexellis/faas) Python function will perform a tensorflow image recognition.

There is an accompanying blog post here: http://jmkhael.io/kittens-vs-tarsiers-an-introduction-to-serverless-machine-learning/

> Make sure to give it a read!

## TLDR;
[![Try in PWD](https://cdn.rawgit.com/play-with-docker/stacks/cff22438/assets/images/button.png)](http://play-with-docker.com/?stack=https://raw.githubusercontent.com/jmkhael/faas-tensorflow/master/docker-compose.yml&stack_name=func)

wait a while until the Tensorflow Docker image extract. Be patient...

then:

```
curl http://localhost:8080/function/func_tensorflow -d \
       'https://cdn.pixabay.com/photo/2016/07/10/21/47/cat-1508613_960_720.jpg'
```

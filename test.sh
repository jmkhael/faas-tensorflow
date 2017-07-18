#!/bin/bash
#image_url='https://nationalzoo.si.edu/sites/default/files/styles/slide_1400x700/public/animals/africanlion-006_0.jpg'

FAAS_TENSORFLOW='http://localhost:8080/function/tensorflow'
image_url='https://unsplash.it/200/300?image=0'


if [ -n "$1" ]; then
    image_url=$1
fi

for index in {1..100..10}; do
  url=https://unsplash.it/200/300?image=$index
  echo checking $url...
  curl $FAAS_TENSORFLOW -d $url

  eog $url
done

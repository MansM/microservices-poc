#!/bin/bash

kubectl scale -f events.yaml --replicas=0

eval $(minikube docker-env)
docker build -t mans/events:2 event

kubectl scale -f events.yaml --replicas=2
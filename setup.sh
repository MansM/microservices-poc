#!/bin/bash

#setting up mariadb
kubectl apply -f mariadb.yml

#setting up env so docker can build
eval $(minikube docker-env)

#building event image
docker build -t mans/events:2 event

#starting event application
kubectl apply -f events.yaml
kubectl apply -f events-service.yaml

#sleep for 10 sec because kube needs time
sleep 10

#creating database
kubectl exec -it $(kubectl get pods |grep events-|head -1 |awk {' print $1 '}) python db_create.py

#opening dashboard
open http://$(minikube ip):30000
# full-stack-demo

## Overview
<img src="https://github.com/Swwwt/full-stack-demo/blob/master/Overview.png" width="480">

## Accomplish 
- [x] Create and connect to mongodb on `mongoDB Atlas`
- [x] Deploy business service and data service on k8s
- [x] Expose `Restful API` to frontend with `Nodeport` service

## Usage
- Setup business service and data service:
  - kubectl apply -f data-service.yaml
  - kubectl apply -f business-service.yaml
- Setup frontend:
  - yarn start

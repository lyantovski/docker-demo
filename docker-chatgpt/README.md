# Docker for ChatGPT

Reference: 
https://collabnix.com/running-chatgpt-locally-on-kubernetes-cluster-using-docker-desktop/


## Getting Started

If you wish to run the tutorial, you can use the following command after installing Docker Desktop (for example):

```bash
docker build -t lyacrpoc.azurecr.io/openaii-k8s:1.0.0 .
docker run -d -p 8080:8080 lyacrpoc.azurecr.io/openai-k8s:1.0.0
docker push lyacrpoc.azurecr.io/openaii-k8s:1.0.0
```


## Use Kubernetes

If you wish to run the docker image on Kubernetes, you can use following commands:

Edit in k8s/deployment.yaml image name with your image created before.

```bash
   kubectl apply -f k8s/
```




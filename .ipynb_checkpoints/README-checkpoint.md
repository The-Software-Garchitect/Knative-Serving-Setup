# Knative-Serving-Setup

### Install Knative Serving
- https://knative.dev/docs/install/yaml-install/serving/install-serving-with-yaml/
- Autoscaling Configurations
    - https://knative.dev/docs/serving/autoscaling/autoscaling-metrics/
    
- If you want to run this with an external end point (with DNS sslip.io), you have to open a terminal window and run ```sudo minikube tunnel``` and keep this open
    - Then run the ```kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.10.0/serving-default-domain.yaml``` command


### Minikube
- Run ```uname -m``` to check whether Arm or X86
- https://minikube.sigs.k8s.io/docs/start/
- ```alias k=kubectl```
    - just nice to not have to run kubectl every time


### Pip3 Installs
- pip3 install fastapi==0.95.1
- pip3 install uvicorn==0.22.0


### FastAPI Docker Commands
- docker build -t samgarvis/fast-api-test:latest .
- docker push samgarvis/fast-api-test:latest


### Test API with Curl
- curl -X POST -H "Content-Type: application/json" -d '{"name": "apple", "description": "a fruit", "price": 1.99, "tax": 0.1}' http://localhost:8000/items/


## Vegeta
### Install Vegeta
- https://github.com/tsenart/vegeta
- brew update && brew install vegeta

### Vegeta Attack
- vegeta attack --targets=targets.txt -rate=2 -duration=2s | vegeta report
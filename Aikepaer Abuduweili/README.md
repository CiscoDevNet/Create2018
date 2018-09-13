# DevNet React Web App boilerplate

Boilerplate for DevNet React Web App
https://github.com/CiscoDevNet/React-Web-App-Boilerplate

### Dependencies:
* [Nodejs](https://nodejs.org/en/)
* [Docker](https://www.docker.com/get-docker)
* [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* [VSCode](https://code.visualstudio.com/)
* [Github](https://github.com/) account and [DockerHub](https://hub.docker.com/) account



## Exercise 1 : Create a React web application from boilerplate. 

Make sure you have installed the latest [Node.js](https://nodejs.org/en/) installed.

1. `Fork` this repo to your github account : `https://github.com/CiscoDevNet/React-Web-App-Boilerplate`
1. `git clone` your repo to local. `git clone https://github.com/[YOUR_GITHUB_ACCOUNT]/React-Web-App-Boilerplate`
2. Run `npm install`
3. Start the dev server using `npm start`
3. Open [http://localhost:8080](http://localhost:8080)


## Exercise 2 : Add a route and content 

Modify `/app/Router.js`

1. Import new page at the top : `import Album from './pages/Album';`
2. Add routing in between `<Switch>` tag : `<Route path="/album" component={Album}/>`
3. Click `Album` link at the top



## Exercise 3 : Dockerize it and push to DockerHub 

### Build production code:

Run `npm run production`

### Build docker image:

Run : `docker build -t webapp .`

### Run container image:

Run : `docker run --name webapp -p 8080:80 -it --rm webapp`  

### Stop container: 

Run `docker rm -f webapp`

### Tag your image:

1. Login to [dockerhub.com](https://hub.docker.com/)
2. Create a [repository](https://hub.docker.com/add/repository/) with the name : webapp.
3. Run `docker tag webapp [YOUR_DOCKERHUB_ACCOUNT]/webapp:latest` at your local.


### Push your image:
1. login to dockerhub. run `docker login`
2. Run `docker push [YOUR_DOCKERHUB_ACCOUNT]/webapp:latest`


## Exercise 4 : Deploy to Google Kubernetes Engine (GKE)


### Set the config file to use :
Run `export KUBECONFIG=config/kubeconfig-trial.yaml`


### Test it 
Run `kubectl get nodes`

You will see something like this :
```
NAME                                        STATUS    ROLES     AGE       VERSION
gke-workshop-1-default-pool-500fed5f-1rp2   Ready     <none>    1d        v1.8.8-gke.0
gke-workshop-1-default-pool-500fed5f-83hl   Ready     <none>    1d        v1.8.8-gke.0
gke-workshop-1-default-pool-500fed5f-szj7   Ready     <none>    1d        v1.8.8-gke.0
```

### Deploy app to k8s

Run `kubectl run webapp-[YOUR_DOCKERHUB_ACCOUNT] --image [YOUR_DOCKERHUB_ACCOUNT]/webapp:latest --port 80`

### check deploy status

Run `kubectl get deployment`

### Expose you app
[PROTNUMBER] is a number between 1000 and 10000.

Run `kubectl expose deployment webapp-[YOUR_DOCKERHUB_ACCOUNT] --type "LoadBalancer" --target-port=80 --port=[PROTNUMBER]`

### Check service status

Run `kubectl get service webapp-[YOUR_DOCKERHUB_ACCOUNT]`

When the `EXTERNAL-IP` become available, access that page : `http://[EXTERNAL-IP]:[PROTNUMBER]/`

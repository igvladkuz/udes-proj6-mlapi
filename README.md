# Overview

Building a CI/CD Pipeline using Github Actions and Azure DevOps
The project demonstrates how to set up a CI/CD pipeline for a web service implementing an online inference of a ML model (ML API). The model used for the project is a pre-trained Scikit-learn model for predicting house prices in Boston

## Project Plan

Trello board:
https://trello.com/b/2qCDDDQJ/udacity-cicd-demo-project

Spreadsheet with project plan:
https://docs.google.com/spreadsheets/d/1Xmz1K1wm1weUYH9r0ylpOTM7_h-G_x2nS0wN6I9tojY/edit?usp=sharing

## Instructions

* Architectural Diagram of the CI/CD Pipeline
![CICD Pipeline](https://github.com/igvladkuz/udes-proj6-mlapi/blob/main/images/architecture.png)

### To run the service locally follow these steps
Prerequisites:
 - Bash shell (available in WSL, MacOS X terminal or Linux)
 - Python 3.7

```
python3 --version # should return 3.7.X
```
1. Create virtual environment and activate
```
python3 -m venv venv
source venv/bin/activate
```
2. Install dependencies
```
make install
```
3. Start the inference service locally
```
python3 app.py
```
4. Send a test request to the inference service, running locally
```
source make_prediction.sh
```

### To run the service on Azure follow these steps
Prerequisites: 
- Bash shell
- Azure subscription with a resource group YourResourceGroup allowing to create App Services
- Azure CLI
1. From the project directory execute the command
```
az webapp up --name <your-app-name> --resource-group <YourResourceGroup> --runtime "PYTHON:3.7"
```
2. Send a test request to the inference service, running in Azure
```
source make_predict_azure_app.sh <your-app-name>
```
3. Stream application logs
```
az webapp log tail --name <your-app-name> --resource-group <YourResourceGroup>
```

* Project running on Azure App Service [App service up and running](https://github.com/igvladkuz/udes-proj6-mlapi/blob/main/screenshots/Azure_App_Service.png)

* Project cloned into Azure Cloud Shell [see screenshot]()
![Azure Cloud Shell](https://github.com/igvladkuz/udes-proj6-mlapi/blob/main/screenshots/Repo_in_Azure_Cloud_Shell.png)

* Passing tests that are displayed after running the `make all` command from the `Makefile`
![Pylint test](https://github.com/igvladkuz/udes-proj6-mlapi/blob/main/screenshots/Pylint.png)

* Gihtub Actions
![Build job](https://github.com/igvladkuz/udes-proj6-mlapi/blob/main/screenshots/Github_Actions_build)

* Successful deploy of the project in Azure Pipelines.
  Refer to [official documentation](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).
![Successful Devops Pipeline Run](https://github.com/igvladkuz/udes-proj6-mlapi/blob/main/screenshots/Azure_DevOps_Pipeline.png)

* Running Azure App Service from Azure Pipelines automatic deployment
![App Service up and running](https://github.com/igvladkuz/udes-proj6-mlapi/blob/main/screenshots/Azure_App_Service.png)

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](make_predict_azure_app.sh).
![Successful Service Call](https://github.com/igvladkuz/udes-proj6-mlapi/blob/main/screenshots/Azure_App_service_w_predict_response.png)

* Output of streamed log files from deployed application
[logs/azure_webapp_log.txt](logs/azure_webapp_log.txt)

* Output of the load test
![Locust load test](https://github.com/igvladkuz/udes-proj6-mlapi/blob/main/screenshots/Load_test_w_Locust.png)

## Enhancements

1. Write unit tests
2. Add authentication
3. Log requests by users
4. Improve performance

## Demo 



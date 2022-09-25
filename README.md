# Overview

Building a CI/CD Pipeline using Github Actions and Azure DevOps

## Project Plan

Trello board:
https://trello.com/b/2qCDDDQJ/udacity-cicd-demo-project

Spreadsheet with project plan:
https://docs.google.com/spreadsheets/d/1Xmz1K1wm1weUYH9r0ylpOTM7_h-G_x2nS0wN6I9tojY/edit?usp=sharing

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> see file logs/azure_webapp_log.txt

## Enhancements

1. Write unit tests
2. Add authentication
3. Log requests by users
4. Improve performance

## Demo 

<TODO: Add link Screencast on YouTube>



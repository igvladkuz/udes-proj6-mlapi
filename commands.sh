# Manually (re)deploy project as Azure Webapp
az webapp up --name ik-udes-proj6 --resource-group Learn --runtime "PYTHON:3.7"

# Stream application logs
az webapp log tail --name ik-udes-proj6 --resource-group Azuredevops

# Request prediction
curl -d '{"CHAS":{"0":0},"RM":{"0":6.575},"TAX":{"0":296.0},"PTRATIO":{"0":15.3},"B":{"0":396.9},"LSTAT":{"0":4.98}}' \
 -H "Content-Type: application/json" \
 -X POST https://ik-udes-proj6.azurewebsites.net/predict


#!/usr/bin/env bash
APPNAME="ik-udes-proj6"
PORT=443
echo "Port: $PORT"

# POST method predict
curl -d '{
   "CHAS":{
      "0":0
   },
   "RM":{
      "0":6.575
   },
   "TAX":{
      "0":296.0
   },
   "PTRATIO":{
      "0":15.3
   },
   "B":{
      "0":396.9
   },
   "LSTAT":{
      "0":4.98
   }
}'\
     -H "Content-Type: application/json" \
     -X POST https://$APPNAME.azurewebsites.net:$PORT/predict 
     #your application name <yourappname>goes here
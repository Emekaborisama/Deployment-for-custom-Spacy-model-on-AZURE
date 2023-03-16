#!/bin/sh
#sample web server shell script  
gunicorn --chdir app main:app -w 3 --threads 5 -b 0.0.0.0:8080
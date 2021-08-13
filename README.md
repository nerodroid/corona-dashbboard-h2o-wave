# Corona Dashboard using H2o and NovelCOVID API

Easy Realtime Corona Analytic Dashboard using h2o_wave. 
View the most recent corona stat updates of any country in the world.

Fetching Data from [Novel Covid API](https://github.com/disease-sh/API)

![corona dash2](https://user-images.githubusercontent.com/42380130/129351308-b2806810-c91f-4b19-89b7-095e6f193d55.PNG)

# How to Run the app locally

## Requirments

1. Python 3.9+ 
2. pip3

# Steps

## 1. Wave Server

to Run the app we need install and run the wave server. https://wave.h2o.ai/docs/installation
Extract the wave sdk and run waved to start the server.
IMPORTANT : keep this server running throughout the process ! 


## 2. Clone the Project 
```
git clone https://github.com/nerodroid/corona-dashbboard-w2o-wave.git
```
extract the project to a location of your choice and go inside the folder.
```
cd corona-dashbboard-w2o-wave-main
```
## 3. Virtual Enviornment

Next we need to set the environment for the app to function in.
```
python3 -m venv venv  or py -m venv venv
source venv/bin/activate or venv/scripts/activate
pip install -r requirements.txt
```
## 4. Run it!

if everything went well so far , it's now ready to run
Run the app with ANOTHER terminal
```
wave run CoronaDashboard.py
```
## 5. See it

Open http://localhost:10101/CoronaDashboard with any browser


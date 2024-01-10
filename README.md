# Simple Similarity Checker
-------
### By Abilash Ramesh
--------
### File Structure:
```bash
.
├── COLLABORATORS
├── LICENSE
├── Docker
│   ├──  dockerfile
│   ├──  app.py
│   ├── requirements.txt
│   └── utilities
│       ├── abbreviations.py
│       ├── scoreutils.py
│       └── stopwords.py
├── README.md
├── setup.py
└── testcases
    └── pytest.py

```
----------
### Contents:

* Introduction
* How to run?
* Available flags
* Workings of scoring system
* Future optimizations

---------
## Introduction:
This Similarity checker is built as a part of a take-home assignment for the position of Machine learning engineer at Fetch. The similarity checker is designed to take in 2 sentences, remove stopwords and expand abbreviations, get the count of unique words within the given sentence and derive a score based on that. 

--------
## How to run:
###prerequisites to run container:
* MacOS Terminal
* Docker desktop
* Github repo should be cloned into system
* Postman or any API testing service

Assuming the above steps have been followed and Docker desktop as well as the github repo are in the system, we need to head into the folder Docker within the cloned repo. Once within the folder, please use the following command:
```bash
sudo docker build -t scorer .
```
The above command brings up one image. The below command is used to build the container which will be deploying the flask-app in Kubernetes pods and EC2 environments. 
```bash
sudo docker run scorer
```
This container is a flask app system that is designed to take API calls via tools such as postman. Once the container is up and running, it is ready to recieve API calls via postman. 

----------
## Available flags:
There are only 2 available flags as of now. These are 
1. ```abbreviate```to ignore expansion of concatenated words and
2. ```stopwords```to ignore stopwords
Both of the above flags are set to ```True``` by default

---------
## Workings of scoring system
We have utilized Jaccard Index to measure ther similarity of sentences. This involves

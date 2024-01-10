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
└── README.md

```
----------
### Contents:

* Introduction
* Assumptions
* How to run?
* Workings of scoring system
* Future optimizations

---------
## Introduction:
This Similarity checker is built as a part of a take-home assignment for the position of Machine learning engineer at Fetch. The similarity checker is designed to take in 2 sentences, remove stopwords and expand abbreviations (both of which are not derived using NLTK, SpaCy or any other extra packages), get the count of unique words within the given sentence and derive a score based on that. 

--------
## Assumptions:
In the creation of the program, here are a number of conscious assumptions that were made to support the project:
1. Punctuations need to be removed as they do not provide much value in the current use case.
2. We only take into account the count of common words between the two sentences to understand the similarity. To improve the model further, we will need to utilize word embeddings/word vectors to represent the meanings and thus classify words based on the meaning. 
3. In case of not using any of the NLP libraries, we will not be able to implement context-based awareness as the words have no numerical representation. Even if we utilize one-hot encoding, we will be utilizing large amounts of time and space to calculate the values.
4. Since context is not taken into consideration in our case, we will be using Jaccard's similarity index which is independent of use of word embeddings.
5. We can utilize dictionaries and sets to keep track of words per sentence and sentence related stats as well.

--------
## How to run:
### Prerequisites to run container:
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
docker run -p 3005:3005 -d scorer 
```
This container is a flask app system that is designed to take API calls via tools such as postman. Once the container is up and running, it is ready to recieve API calls via postman. 

### Available flags:
There are only 2 available flags as of now. These are 
1. ```abbreviate```to ignore expansion of concatenated words and
2. ```stopwords```to ignore stopwords
Both of the above flags are set to ```True``` by default

---------
## Workings of scoring system
We have utilized Jaccard Index to measure ther similarity of sentences. This involves utilizing the common words in both the sentences and calculate the frequency of common words vs all words in the sentence. The formula for this is: 

$` {C\over T} `$ 

Where:
* C is the total number of unique words and
* T is the total number of words from both the sentences.

--------
## API calls:
To test the microservice, the following URL needs to be used:
```bash
http://0.0.0.0:3005/similarity-scores
```
The payload to be provided is as follows
```json
{
    "sentences": [<Sentence 1>, <Sentence 2>]
}
```
After testing the example sentences using the above method, we were able to get scores as follows:
|Sentences |Similarity Score |
|---------------  |---------------|
|Sentence 1 and 2 |  0.63        |
|Sentence 1 and 3 |  0.19        |
--------
## Future Optimizations:
1. Utilizing word embeddings to club similar words together. This allows us to utilize other scoring mechanisms such as cosine distance and TF-IDF.
2. Handling large-scale loads by using Gunicorn for multi-threading since Flask app allows only for one request at a time.
3. Utilizing server-side caching for better performance monitoring and logging.

from utilities.scoreutils import _get_bow, _get_scores
from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/')
def home():
    return 

@app.post("/similarity-scores")
def compare_sents():
  request_data = request.get_json()
  sentences = request_data.get("sentences")
  stw = request_data.get("stopwords")
  abbs = request_data.get("abbreviations")
  try:
    if len(sentences) < 2:
        return Response("Please provide 2 sentences to continue", 400)
    # Default number of sentences is 2 as of now
    # separate BOW fn to facilitate changes
    bow = _get_bow(sentences, stw = False, abbs = False) 
    # Separate fn for scoring to change mechanism later
    score = _get_scores(bow) 
    return Response(f"Score is {round(score, 2)}", 201)
  except Exception as e:
     return Response(f"Failed due to error {e}", 500)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 3005)


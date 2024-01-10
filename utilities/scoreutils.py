from abbreviations import CONTS
from stopwords import stopwords

def _get_bow(sentences, stw = True, abbs = True):

  res = {}
  s = 1

  for j in sentences:
    st = set()
    for k in (j.lower().split()):
      if stw:
        if k in stopwords:
          continue
      if abbs:
        if k in CONTS.keys():
          k = CONTS[k]
      st.add(k)

    res[s] = st
    s += 1
  return res

def _get_scores(bow, mechanism = None):
    """Get scores for the 2 sentences

    Args:
        bow (dict): dict containing set of unique words in 2 sentences
        mechanism (str, optional): Scoring mechanism (future use). Defaults to None.

    Returns:
        score: _description_
    """  

    if mechanism == 'TFIDF':
        """
        TFIDF Scoring mechanism here
        """
    else:
        score = len(bow[1].intersection(bow[2])) / len(bow[1].union(bow[2]))
    return score


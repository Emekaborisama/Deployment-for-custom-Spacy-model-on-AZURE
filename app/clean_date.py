import spacy
import string
from nltk.corpus import stopwords
import pandas as pd

import re
regex = re.compile('[%s]' % re.escape("""!"#$%&'()*+,-.:;<=>?@[\]^_`{|}~"""))




def remove_puntucations_from_text(s):
  """remove puntucations from text

  Args:
      _type: str

  Returns:
      _type_: str
      return clean text without punctuations
  """
  return regex.sub('', s)



def remove_bigram(text):
  """remove bigrams cause spacy model work perfectly without bigrams 

  Args:
      _type_: str

  Returns:
      _type_: str
      return clean text without bigrams
  """
  return re.sub('to|is]$', ",", text)


def filter_stopwords_n_remove_puntuc(text):
  """apply remove puntucations from text function and remove bigram

  Args:
    type: str
    

  Returns:
      _type_: str
      return clean text
  """
  clean_text = remove_puntucations_from_text(text)
  #print(clean_text)
  stopword_text = remove_bigram(clean_text)
  #print(stopword_text)
  return stopword_text


def remove_prefix(text):
  """ remove suffix from date values e.b st, nd etc

  Args:
      _type_:datetime

  Returns:
      _type_:str
      return clean date value
  """
  try:
    return [re.sub("st|nd|rd|th]$",'',x) for x in text]
  except:
    pass






def reformat_date(date):
  """apply remove prefix function, convert string to datetime and reformat date to %d/%m/%Y

  Args:
      _type_: datetime
      date: datetime

  Returns:
      _type_: list
      return datetime value  
  """
  date_clean = remove_prefix(date)
  #print(date_clean)
  date_reformat = pd.to_datetime(date_clean)
  return date_reformat.strftime('%d/%m/%Y')

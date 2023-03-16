import os
from app.load_model import load_model
import re
from app.clean_date import filter_stopwords_n_remove_puntuc, reformat_date

#load this model once in the using flask before request function
nlp = load_model("nlp_sm")



def extract_date(text, nlp):
  """extract date from text using spacy ner, validate if the entity recognition return any date and apply text cleaning function 

  Args:
      _type_: str
      text: inference data

  Returns:
      _type_: list
      date: dates extracted
      
      
  """
  if len(text) >=1:
    text = filter_stopwords_n_remove_puntuc(text)

    doc = nlp(text)
    result= [t.text for t in doc.ents if t.label_ == 'DATE']

    if len(result) <=0:
      return False
    else:
      return result
  else:
    return None





def extract_date_inference(text,nlp):
  """apply date extraction function for inference and  validate if the entity recognition return any date

  Args:
      _type_: str
      text: inference data

  Returns:
      _type_: dict
      date: dates extracted
      message: if the extraction process was sucessfully or not
      
  """
  result = {}
  try:
    result_date = extract_date(text,nlp)
    
    if result_date == False or result_date == None:
      result['dates'] = []
      result['message'] = "Warning, dates not extracted correctly"
      return result
      
    else:

      result['dates'] = reformat_date(result_date)
      result['message'] = "Successful"
      return result
  except:
    #always return none when there is an error. setup sentry log or monitoring for those error so it wouldnt break the api or pipeline
    result['data'] = None
    



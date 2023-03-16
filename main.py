from app.dates_extraction import extract_date_inference
from app.load_model import load_model
# api code should be here



#load this model once in the using flask before request function
nlp = load_model("nlp_sm")

# call the extract_date_inference function and pass the text and the nlp loaded model
### e.g extract_date_inference("The policy provides cover from 21 June 2019 to 1 July 2022 inclusive",nlp)




####### sample print statement to test
#print(extract_date_inference("The policy provides cover from 21 June 2019 to 1 July 2022 inclusive",nlp))


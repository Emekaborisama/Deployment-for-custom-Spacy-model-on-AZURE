
import nltk
nltk.download('stopwords')
import pickle

def load_model(text):
    """load pickle spacy model

    Args:
        _type_: str

    Returns:
        _type_: object
        return deseriselized pickle model object
    """
    if "nlp_sm":
        try:
            nlp = pickle.load(open("model/nlp_sm.p", 'rb'))
        except:
            nlp = pickle.load(open("app/model/nlp_sm.p", 'rb'))
        return nlp
    else:
        print("you didn't identify the model properly")
        pass

    
load_model("nlp_sm")

import spacy
#import en_core_web_trf
import en_core_web_sm
import pickle 

nlp = en_core_web_sm.load()

#seriselize the model so we dont have to load it everytime we make changes to the service
pickle.dump(nlp, open( "/model/nlp_sm.p", "wb" ))





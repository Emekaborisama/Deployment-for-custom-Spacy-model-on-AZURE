import pytest


# importing the sys module
import sys        
from app.load_model import load_model
import re
nlp = load_model("nlp_sm")




from app import dates_extraction


def test_extract_inf():
    """ test for extracting data formated text"""

    text = "Policy terms from 1/1/2021 to 31/12/2022"
    res = dates_extraction.extract_date_inference(text,nlp) 
    assert len(res['dates']) >=1
    assert len(res['message']) == 10

    
    

def test_extract_inf2():
    """test for extracting text formated date"""
    text2 = 'The policy provides cover from 21 June 2019 to 1 July 2022 inclusive' 
    res2 = dates_extraction.extract_date_inference(text2,nlp) 
    assert len(res2['dates']) >=1
    assert len(res2['message']) == 10
     

def test_handle_error():
    """test for handling errors"""
    text2 = 'The policy provides cover from 31 June 2019 1 July 2022 inclusive' 
    res2 = dates_extraction.extract_date_inference(text2,nlp) 
    assert res2 ==None
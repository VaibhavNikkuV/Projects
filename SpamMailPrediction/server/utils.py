import joblib
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)

def input_mail_feature_extraction(input_mail):
    

    
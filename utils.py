# spacy
import warnings
import spacy
from spacy.pipeline import EntityRuler
from spacy.lang.en import English
from spacy.tokens import Doc

# gensim
import gensim
from gensim import corpora

# Visualization
from spacy import displacy
import pyLDAvis.gensim_models
from wordcloud import WordCloud
import plotly.express as px
import matplotlib.pyplot as plt

# Data loading/ Data manipulation
import pandas as pd
import numpy as np
import jsonlines

# nltk
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download(['stopwords', 'wordnet'])

# warning
warnings.filterwarnings('ignore')


def clean_resume(text):
    clean_text = re.sub(
        '(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?"',
        " ",
        text,
    )

    clean_text = clean_text.lower()
    clean_text = clean_text.split()
    lm = WordNetLemmatizer()
    clean_text = [
        lm.lemmatize(word)
        for word in clean_text
        if not word in set(stopwords.words("english"))
    ]
    clean_text = " ".join(clean_text)
    return clean_text


def get_skills(nlp, clean_text):
    skills = set()
    doc = nlp(clean_text)
    ents = doc.ents
    for token in ents:
        if token.label_ == "SKILL":
            skills.add(str(token))
    return skills


# Pie chart, where the slices will be ordered and plotted counter-clockwise:


def plot_pie(required_skills, skills):
    count = 0
    for x in required_skills:
        if x in skills:
            count += 1

    labels = 'Requirement', 'Skills'
    score = count/len(required_skills)*100
    sizes = [100 - score, score]
    fig1, ax1 = plt.subplots(figsize=(2, 2))
    ax1.pie(sizes,  labels=labels, autopct='%1.1f%%',
            shadow=False, startangle=90)
    ax1.axis('equal')

    return fig1


def get_matching_skills(required_skills, skills):
    matching = []
    missing = []
    for x in required_skills:
        if x in skills:
            matching.append(x)
        else:
            missing.append(x)
    return matching, missing

# -*- coding: utf-8 -*-
"""
Created on Sun May 31 12:45:32 2020

@author: Lucas
"""

from urllib.request import Request, urlopen

link = Request('https://hypescience.com/as-surpresas-nao-acabam-em-2020-novo-surto-de-ebola-e-declarado-no-congo/',
               headers={'User-Agent': 'Mozilla/5.0'})
pagina = urlopen(link).read().decode('utf-8', 'ignore')

from bs4 import BeautifulSoup

soup = BeautifulSoup(pagina, "lxml")
texto = soup.find(id="ezoic-pub-ad-placeholder-156t").text

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

sentencas = sent_tokenize(texto)
palavras = word_tokenize(texto.lower())

from nltk.corpus import stopwords
from string import punctuation

stopwords = set(stopwords.words('portuguese') + list(punctuation))
palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]

from nltk.probability import FreqDist

frequencia = FreqDist(palavras_sem_stopwords)

from collections import defaultdict

sentencas_importantes = defaultdict(int)

for i, sentenca in enumerate(sentencas):
    for palavra in word_tokenize(sentenca.lower()):
        if palavra in frequencia:
            sentencas_importantes[i] += frequencia[palavra]

from heapq import nlargest

idx_sentencas_importantes = nlargest(4, sentencas_importantes, sentencas_importantes.get)

for i in sorted(idx_sentencas_importantes):
    print(sentencas[i])
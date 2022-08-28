# -*- coding: utf-8 -*-
"""Resume Parser.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DnE--u0d8y1xc66qFeFhwmHYVOwhfuws
"""

import PyPDF2

import nltk

files = '/content/Fazil Resume.pdf'

pdfreader = PyPDF2.PdfReader(files)

page = pdfreader.getPage(0)
page1 = page.extractText()

from nltk import word_tokenize

tokenized = word_tokenize(page1)

#page11 = [x.replace('\n','') for x in tokenized]

import re

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", page1)

#print(emails)

phone = re.findall(r'\d\d\d\d\d\d\d\d\d\d\d\d', page1)
if len(phone)<1:
  phone = re.findall(r'\d\d\d\d\d\d\d\d\d\d', page1)

#print(phone)

new = page1[0:250]
#new

import spacy

nlp = spacy.load("en_core_web_lg")
doc = nlp(new)

for ent in doc.ents:
  if ent.label_ == 'PERSON' or ent.label_ == 'ORG':
    fullname = ent.text
    break
  #print(ent.text,ent.start_char,ent.end_char,ent.label_)

skilldata = ['Python','Spark','Hive','Sql','Pig','Bigdata','Big data','Machine learning','Deep Learning','AI','Artificial Intelligence','C','PHP','C++','C#','C Shark','Shell Script','HTML','CSS','JavaScript','Java','Angular','Django','Flask','Laravel','MySQL','SQLite','MongoDB','Git','NLP','Scikit','OpenCV','Cloud','GCP','Azure','DigitalOcean','AWS','Tableau','sqoop','Scala','R']
skilldatas = [x.lower() for x in skilldata]

skills = []
for i in tokenized:
  if i.lower() in skilldatas:
    skills.append(i)

readpdf = PyPDF2.PdfFileReader(files)
if readpdf.numPages>1:
  page02 = pdfreader.getPage(1)
  page2 = page02.extractText()
  tokenizedp2 = word_tokenize(page2)
  for i in tokenizedp2:
    if i.lower() in skilldatas:
      skills.append(i)
if readpdf.numPages>2:
  page03 = pdfreader.getPage(2)
  page3 = page03.extractText()
  tokenizedp2 = word_tokenize(page3)
  for i in tokenizedp2:
    if i.lower() in skilldatas:
      skills.append(i)

#skills

details = {'Name':fullname,'EmailID':emails,'ContactNo':phone}

print(details,"Skill=",skills)


# -*- coding: utf-8 -*-
from nltk.corpus import wordnet as wn

#%%
dog_synsets = wn.synsets(r'dog') # ищем все синсеты, в которых есть подстрока "dog"
print (dog_synsets)

#%%
dog_noun_synsets = wn.synsets(r'dog', pos=wn.NOUN) # Другие части речи: VERB, ADJ, ADV
print (dog_noun_synsets)

#%%
dog_exemplar = wn.synset('frank.n.02')
print (dog_exemplar.name(), dog_exemplar.definition(),
       dog_exemplar.lemma_names())

#%%
dog_synset = wn.synset('dog.n.01')
print (dog_synset.lemma_names('fra'))
#%%
print (dog_exemplar.hyponyms(), dog_exemplar.hypernyms())
print(wn.synset('heavy.a.1').similar_tos())

#%%
old_lemmas = wn.lemmas('old') #ищем все вхождения (=значения) леммы old
print (old_lemmas)

#%%
old_lemma = wn.lemma('old.a.02.old')
print (old_lemma.antonyms())

#%%
print(wn.synset('person.n.01').lowest_common_hypernyms(wn.synset('dog.n.01')))
print(wn.synset('dog.n.01').path_similarity(wn.synset('cat.n.01')))
print(wn.synset('person.n.01').path_similarity(wn.synset('cat.n.01')))

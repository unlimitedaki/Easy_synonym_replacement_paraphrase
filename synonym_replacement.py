import nltk
import json
import argparser
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import sent_tokenize
from nltk.corpus import wordnet 
from nltk.corpus import stopwords
import random 


def load_data(file_name):
    sentence_data = []
    with open(file_name,'r',encoding='utf8') as f:
        data = f.readlines()
    sentence_data = [sent_tokenize(line) for line in data] 
    return sentence_data

# def find_

def get_synonyms_and_antonyms(word):
    '''
    get synonyms and antonyms of given word from wordnet
    '''
	synonyms = set()
    antonyms = set()
	for syn in wordnet.synsets(word): 
		for l in syn.lemmas(): 
			synonym = l.name().replace("_", " ").replace("-", " ").lower()
			synonym = "".join([char for char in synonym if char in ' qwertyuiopasdfghjklzxcvbnm'])
			synonyms.add(synonym)
            if l.antonyms():
                antonym = l.name().replace("_", " ").replace("-", " ").lower()
                antonym  = "".join([char for char in antonym if char in ' qwertyuiopasdfghjklzxcvbnm'])
                antonyms.add(antonym)
	if word in synonyms:
		synonyms.remove(word)
	return list(synonyms),list(antonyms)

def synonym_antonym_replacement(args):
    sentence_data = load_data(args.file_name)
    result_json = {}
    for doc_index,document in enumerate(sentence_data):
        result_json[doc_index] = []
        for sentence in document:
            sentence_json = {}

            # just simplely use nltk tools to tokenize and pos_tagging
            words = nltk.word_tokenize(sentence)
            sy_words = words.copy()
            an_words = words.copy()
            pos_list = nltk.pos_tag(words)
            for i in range(len(words)):
                if words[i] not in nltk.stopwords and pos_list[i] in ["JJ","RB"]:
                    synonyms,antonyms = get_synonyms_and_antonyms(words[i])
                    # random pick one synonym and one antonym
                    if len(synonyms)>0:
                        synonym = random.sample(synonyms,1)[0]
                        sy_words[i] = synonym
                    if len(antonyms)>0:
                        antonym = random.sample(antonyms,1)[0]
                        an_words[i] = antonym
            sy_sentence = " ".join(sy_words)
            an_sentence = " ".join(an_words)
            sentence_json['raw'] = sentence
            sentence_json['synonyms'] = sy_sentence
            sentence_json['antonyms'] = an_sentence
            result_json.append(sentence_json)
    return result_json


def synonym_antonym_replacement_api(
    file_name,
    mode = "Both"
):
    args.file_name = file_name
    args.mode = mode
    synonym_antonym_replacement(args)


parser = argparse.ArgumentParser()
parser.add_argument("--file_name",type = str,default = "CompreOE-passage.txt")
parser.add_argument("--mode",type = str,default = "Both")
try:
    # shell
    args = parser.parse_args()
except:
    # on notebook
    args = parser.parse_args(args = [])

if __name__ == "main":
    synonym_antonym_replacement(args)
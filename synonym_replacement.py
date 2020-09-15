import random
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import nltk
import json
import argparse
import pdb
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


def load_data(file_name):
    sentence_data = []
    with open(file_name, 'r', encoding='utf8') as f:
        data = f.readlines()
    sentence_data = [sent_tokenize(line) for line in data]
    return sentence_data


def get_synonyms_and_antonyms(word):
    ''' 
    获取当前词的 同义词 & 反义词
    '''
    synonyms = set()
    antonyms = set()
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonym = l.name().replace("_", " ").replace("-", " ").lower()
            synonym = "".join(
                [char for char in synonym if char in ' qwertyuiopasdfghjklzxcvbnm'])
            synonyms.add(synonym)
            if l.antonyms():
                antonym = l.antonyms()[0].name().replace("_", " ").replace("-", " ").lower()
                antonym = "".join(
                    [char for char in antonym if char in ' qwertyuiopasdfghjklzxcvbnm'])
                antonyms.add(antonym)
    if word in synonyms:
        synonyms.remove(word)
    return list(synonyms), list(antonyms)


def synonym_antonym_replacement(args):
    sentence_data = load_data(args.file_name)
    result_json = {}
    sw_en = stopwords.words("english")
    for doc_index, document in enumerate(sentence_data):
        result_json[doc_index] = []
        for sentence in document:
            sentence_json = {}
            # just simplely use nltk tools to tokenize and pos_tagging
            words = nltk.word_tokenize(sentence)
            sy_words = words.copy()
            an_words = words.copy()
            pos_list = nltk.pos_tag(words)
            # only output sentence with at least one synonym or antonym
            sy_flag = False
            an_flag = False
            for i in range(len(words)):
                if words[i] not in sw_en and pos_list[i][1] in ["JJ", "RB"]:
                    synonyms, antonyms = get_synonyms_and_antonyms(words[i])
                    # just random pick one synonym and one antonym
                    if len(synonyms) > 0:
                        sy_flag = True
                        synonym = random.sample(synonyms, 1)[0]
                        sy_words[i] = synonym
                    if len(antonyms) > 0:
                        an_flag = True
                        antonym = random.sample(antonyms, 1)[0]
                        an_words[i] = antonym
            sy_sentence = " ".join(sy_words)
            an_sentence = " ".join(an_words)
            if sy_flag:
                sentence_json['synonyms'] = sy_sentence
            if an_flag:
                sentence_json['antonyms'] = an_sentence
            if sy_flag or an_flag:
                sentence_json['raw'] = sentence
                result_json[doc_index].append(sentence_json)
    with open("result.json",'w',encoding = "utf8") as f:
        json.dump(result_json,f,indent = 2,ensure_ascii = False)
    return result_json


def synonym_antonym_replacement_api(
    file_name,
    mode="Both"
):
    args.file_name = file_name
    args.mode = mode
    synonym_antonym_replacement(args)


parser = argparse.ArgumentParser()
parser.add_argument("--file_name", type=str, default="CompreOE-passage.txt")
parser.add_argument("--mode", type=str, default="Both")
try:
    # shell
    args = parser.parse_args()
except:
    # on notebook
    args = parser.parse_args(args=[])

if __name__ == "__main__":
    print("main")
    synonym_antonym_replacement(args)

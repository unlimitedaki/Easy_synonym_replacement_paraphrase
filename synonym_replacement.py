import nltk
import json
from nltk.tokenize import sent_tokenize
import argparser



def load_data(file_name):
    sentence_data = []
    with open(file_name,'r',encoding='utf8') as f:
        data = f.readlines()
    sentence_data = [sent_tokenize(line) for line in data] 
    return sentence_data

def synonym_antonym_replacement(args):
    sentence_data = load_data(args.file_name)
    result_json = {}
    for doc_index,document in enumerate(sentence_data):
        result_json[doc_index] = []
        for sentence in document:
            sentence_json = 
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
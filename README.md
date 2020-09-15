# Easy_synonym_replacement_paragraph

replace words from raw sentence with synonym or antonym

## Current Setting

```
INPUT = “filename”
	example_file = CompreOE-passage.txt
OUTPUT = result.json
	"0": [ # document index
    {
      "synonyms": "It became the firstly National Park in 1872 .",
      "antonyms": "It became the last National Park in 1872 .",
      "raw": "It became the first National Park in 1872."
    },]
```



## Target format

```
INPUT = raw_sentence, replace_word , FLAG(synonym or antonym)
OUTPUT = replaced_sentence(paragraph)
```


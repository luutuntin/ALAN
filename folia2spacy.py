#! /usr/bin python3

from pynlpl.formats import folia
import sys
import spacy

def build_spacy_doc(folia_file):
    try:
        folia_doc = folia.Document(file=folia_file)
        nlp = spacy.load('en')
        doc = nlp(folia_doc.text())
        return(doc)
    except:
        print("Error occurred while processing " + folia_file)

def main():
    doc = build_spacy_doc(sys.argv[1])

if __name__ == '__main__':
    main()

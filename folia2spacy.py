#! /usr/bin python3

from pynlpl.formats import folia
import os
import sys
import spacy
import getopt

def usage():
    print("This script converts a FOLIA XML file into a SpaCy Doc object")
    print("Usage: python3 folia2spacy.py folia-file")

def build_spacy_doc(folia_file):
    try:
        folia_doc = folia.Document(file=folia_file)
        nlp = spacy.load('en')
        doc = nlp(folia_doc.text())
        return(doc)
    except:
        print("Error occurred while processing " + folia_file)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "-h", ["help"])
    except getopt.GetoptError as err:
        print(str(err),file=sys.stderr)
        usage()
        sys.exit(2)

    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()
            sys.exit(0)
        else:
            raise Exception("No such option: " + o)

    if len(args) == 1:
        fn = sys.argv[1]
        if os.path.exists(fn):
            doc = build_spacy_doc(fn)
        else:
            print("ERROR: File or directory not found: " + fn, file=sys.stderr)
            sys.exit(3)
    else:
        usage()
        sys.exit(2)

if __name__ == '__main__':
    main()

#! /usr/bin python3

from pynlpl.formats import folia
import sys
import spacy

def spacy2folia(spacy_doc):
    #TODO: add sets
    #TODO: populate xml tree
    folia_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="folia2html.xsl"?>
<FoLiA xmlns="http://ilk.uvt.nl/folia" xmlns:xlink="http://www.w3.org/1999/xlink" xml:id="untitled" version="0.12.0" generator="manual">
<metadata type="native">
<annotations>
</annotations>
</metadata>
<text xml:id="untitled.text">
    <t>{spacy_doc.rstrip()}</t>
</text>
</FoLiA>"""
    return folia_template

def main():
    fh = open(sys.argv[1], 'r')
    infile = fh.read()
    nlp = spacy.load('en')
    doc = nlp(infile)
    out = open(sys.argv[2], 'w')
    out.write(spacy2folia(doc.text))

if __name__ == '__main__':
    main()

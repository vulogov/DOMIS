from textx import metamodel_from_str
import textx.exceptions

DOMIS_GRAMMAR = r"""
Model: s*=Word;
Word[noskipws]:
    /\s*/-
    prefix*=Prefix
    root*=Root
    suffix*=Suffix
    notation*=Notation
    /\s*/-
;
Prefix:
    a=VOWEL
    b=PCONSONANT
;
Suffix:
    a=VOWEL
    b=SCONSONANT
;
Root:
    a=PCONSONANT
    b=VOWEL
    c=SCONSONANT
;
Notation:
    "." | "," | "!" | "?"
;

PURECONS:
    "B" | "C" | "D" | "F" | "G" | "K" | "L" | "R" | "T"
;

PCONSONANT:

;
SCONSONANT:
    "B" | "C" | "BH"
;
VOWEL:
    "A" | "E"
;
"""

def dGrammar():
    mm = metamodel_from_str(DOMIS_GRAMMAR, memoization=True, ignore_case=True)
    return mm

def dModel(mm, _model):
    model = mm.model_from_str(_model)
    return model

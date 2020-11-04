import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from DOMIS import *

def test_GRAMMAR_1():
    m = DOMIS("BAB BEB")
    assert len(m.s) == 2

def test_GRAMMAR_2():
    m = DOMIS("Bab beb")
    assert len(m.s) == 2

def test_GRAMMAR_3():
    m = DOMIS("Bab? beb! !")
    assert len(m.s) == 3

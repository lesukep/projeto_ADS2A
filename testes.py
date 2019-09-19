import pytest
from principal import somar
from principal import subtrair 

def test_Somar():
    assert somar(2,4)==6

def test_Subtrair():
    assert subtrair(9,5)==4

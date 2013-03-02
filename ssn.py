#
#  This should contain SSN info that should be found by Clouseau
#
#

from os import *
import sys
from validate import SSNValidator


def validate_ssn(ssn):
    return SSNValidator().validate(ssn)





#let's run a few quick testa
if __name__ == "__main__":
    ssn = '632-11-1234'
    print validate_ssn(ssn)
    ssn = '970.00.0123'
    print validate(ssn)






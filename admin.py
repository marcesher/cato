#
# pos_one.py -- this contains data that should be found by Clouseau
#

import os
import sys

username = 'abba'

class Massage:

    def __init__(self):
        self.admin = 'root'
        self.email = 'admin@gov.gov'
        self.password = 'P@ssW0rd'
        self.username = 'root'


    def get_password(self,user):
        u = User(user)
        return u.password


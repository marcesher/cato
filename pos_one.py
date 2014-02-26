#
# pos_one.py -- this contains data that should be found by Clouseau
#

import os
import sys


class Massage:

    def __init__(self):
        pass


    def __unicode__(self):
        return "I want from you the massagem, you idiot!"



 


class Minkey:    
    def __init__(self):
        self.admin = 'root'
        self.email = 'admin@gov.gov'
        self.password = 'P@ssW0rd'
        self.username = 'root'


    def change_password(self,user):
        u = User(user)
        pwd = u.change_password('rand')
        return pwd 


# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 19:34:24 2016

@author: Muneeb ul Hassan
"""

import csv
import shutil
from tempfile import NamedTemporaryFile

def read_data(user_id=None, email=None):
    filename = "Users.csv"
    with open(filename,"r") as csvfile:
        reader = csv.DictReader(csvfile)
        items = []
        unknown_user_id= None
        unknown_email = None
        for row in reader:
            if user_id is not None:
                if int(user_id) == int(row.get("id")):
                    return row
                else:
                    unknown_user_id = user_id
            if email is not None:
                if email == row.get("email"):
                    return row
                else:
                    unknown_email = email
        if unknown_user_id is not None:
            return "User id {user_id} not found".format(user_id=user_id)
        if unknown_email is not None:
            return "email {email} not found".format(email=email)
    return None
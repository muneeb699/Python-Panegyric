# -*- coding: utf-8 -*-
"""
Created on Sat Dec 03 20:31:31 2016

@author: Muneeb ul Hassan
"""

import csv
import shutil
from tempfile import NamedTemporaryFile
def edit_Data(id=None,email=None, sent=None):
    filename = "Users.csv"
    temp_file = NamedTemporaryFile(delete = False)
    with open(filename,"rb") as csvfile, temp_file:
        redaer = csv.DictReader(csvfile)
        fieldnames = ["id","Names","Emails","Status"]
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in redaer:
            if id is not None:
                if int(row["id"])==int(id):
                    row["Status"] = sent
            elif email is not None:
                if str(row["email"])==str(email):
                    row["Status"] = sent
            else:
                pass
            writer.writerow(row)
        shutil.move(temp_file, filename)
        return True
    return False
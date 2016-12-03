# -*- coding: utf-8 -*-
"""
Created on Sat Dec 03 19:40:33 2016

@author: Muneeb ul Hassan
"""

import csv

def get_length(file_path):
    with open("Users.csv") as csvfile:
        reader = csv.reader(csvfile)
        list_reader = list(reader)
        return len(list_reader)
def append_data(file_path,name,email):
    fields = ["id", "name", "email"]
    next_id = get_length(file_path)
    with open(file_path,"a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writerow({
                "id":next_id,
                "name":name,
                "email":email,
                })
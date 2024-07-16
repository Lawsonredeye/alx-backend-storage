#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB:
"""

# use pymongo library for getting access to the data
# create a client connection to connect to the database and the collection
# using the method .count() to get the total count
# .count({filter})

import pymongo

client = pymongo.MongoClient()
db = client.logs

total_logs: int = db.nginx.count()
mthd = {
    "GET": db.nginx.count({"method": "GET"}),
    "POST": db.nginx.count({"method": "POST"}),
    "PUT": db.nginx.count({"method": "PUT"}),
    "PATCH": db.nginx.count({"method": "PATCH"}),
    "DELETE": db.nginx.count({"method": "DELETE"})
}

status_path = db.nginx.count({"path": "/status"})

print(f"{total_logs} logs\nMethods:")
print(f"\tmethod GET: {mthd['GET']}\n\tmethod POST: {mthd['POST']}", end="")
print(f"\n\tmethod PUT: {mthd['PUT']}\n\tmethod PATCH: {mthd['PATCH']}", end="")
print(f"\n\tmethod DELETE: {mthd['DELETE']}")
print(f"{status_path} status check")

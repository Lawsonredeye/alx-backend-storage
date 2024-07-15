#!/usr/bin/env python3
"""
Interact with the Mongodb with the pymongo Lib
"""


def list_all(mongo_collection):
    document_object = mongo_collection.find()
    if document_object:
        return list(document_object)
    else:
        return []

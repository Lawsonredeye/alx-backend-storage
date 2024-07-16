#!/usr/bin/env python3
"""
inserts data into a document using python from a mongodb object
"""

def insert_school(mongo_collection, **kwargs: dict):
    """
    parameter:
        mongo_collection: object
            a connecion instance to the mongo database
        kwargs: dict
            key-value data passed as a parameter
    
    Returns: int
        insertReturn id when value has been passed into the database collection
    """
    result_id = mongo_collection.insert_one(kwargs)
    return result_id.inserted_id

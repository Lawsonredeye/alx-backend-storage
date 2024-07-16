#!/usr/bin/env python3
"""
Module which handles the update part of C.R.U.D operations for mongo collection
"""


def update_topics(mongo_collection: object, name: str, topics: list[str]):
    """
    Parameters:
        mongo_collection: object
            collection object instance connected to a database
        name: str
            filter query based on what is to be updated
        topics: list[str]
            value to be added to the new found document on mongodb

    Returns:
        nothing
    """
    mongo_collection.update_one(
        {"name": name},
        {'$set': {"topics": topics}},
        upsert=True
        )

#!/usr/bin/env python3
"""
Module which handles the update part of C.R.U.D operations for mongo collection
"""


def update_topics(mongo_collection, name: str, topics):
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
    mongo_collection.update_many(
        {"name": name},
        {'$set': {"topics": topics}}
        )

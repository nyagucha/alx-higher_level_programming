#!/usr/bin/python3
"""function that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """define json representation of a string"""
    return json.dumps(my_obj)

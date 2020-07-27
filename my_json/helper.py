"""
serialization : dumps()
deserialization : loads()
"""

import json
def stringify(obj):
    return json.dumps(obj)

def JSONParse(json_str):
    return json.loads(json_str)
import os, json

def get():
    """ """
    with open(os.path.join(os.getcwd(), 'framework', 'test.json'), 'r') as f:
        data = json.load(f)
    return data
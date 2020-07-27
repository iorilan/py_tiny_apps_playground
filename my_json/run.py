import helper as h
import os
import pprint

def save_json(obj):
    json_str = h.stringify(obj)
    path = os.path.join("sample_data","json_str.txt")
    if os.path.exists(path):
        os.unlink(path)

    with open(path, 'w') as f :
        f.write(json_str)
        f.close()

    print("obj saved to file === >")
    print(json_str)

def load_json():
    path = os.path.join("sample_data","json_str.txt")
    with open(path, 'rb') as f:
        json = f.read()
        return h.JSONParse(json)

if __name__ == "__main__":
    obj = {
            "this":"is",
            "a":
                {
                    "sample":
                            {
                                "json":["obj","with",{"nested":{"json":"obj"}}]
                            }
                }
            }
    save_json(obj)

    print("json string to obj ==>")
    obj2 = load_json()
    pprint.pprint(obj2)
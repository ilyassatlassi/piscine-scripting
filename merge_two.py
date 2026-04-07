import json

def merge_two(first_dict):
    new_dict = {}
    
    while True:
        print("Add a new entry:")
        key = input("key: ")
        
        if key.lower() == 'exit':
            break
            
        value = input("value: ")
        new_dict[key] = int(value)
        
    merged_result = first_dict | new_dict
    
    return json.dumps(merged_result)

import json

def sqlalc_obj_to_json(result):
    lst = []
    
    for row in result:
        result_dict = row.__dict__
        del result_dict['_sa_instance_state']
        lst.append(result_dict)

    return lst
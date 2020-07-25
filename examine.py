import re
import datetime
from bson import ObjectId
def examine_list(x):
    count = 0
    for i in x:
        x[count] = examine(count,i)
        count = count + 1     

def examine_dictionary(x):
    for key, value in x.items():
        x[key] = examine(key,value)

def examine(key,value):
    if(type(value) is list):
        examine_list(value)
        return value
    elif(type(value) is dict):
        examine_dictionary(value)
        return value
    key_pat = re.sub(r"^[\w/+_-]+[=]$", "key" , str(value))
    word_pat = re.sub(r"[Ww]ord","words",str(key))
    text_pat = re.sub(r"[Tt]ext","texts",str(key))
    sentence_pat = re.sub(r"^([\w'_-]+[\s]{1}){1,14}[\w]+$", "sentence", str(value))
    para_pat = re.sub(r"^([\w'_-]+[\s]{1}){15,}[\w]+$", "paragraph", str(value))
    id_pat = re.sub(r"^[A-Z0-9]+[@]\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}$", "id", str(value)) 
    date_time_pat = re.sub(r"^\d{4}[-](0?[1-9]|1[0-2])[-](0?[1-9]|[1-2][0-9]|3[0-1])[\s]*(0?[1-9]|[1][0-9]|2[0-4])[:](0?[1-9]|[1-5][0-9]|60)[:](0?[1-9]|[1-5][0-9]|60)$", "date-time", str(value)) 
    sha_pat = re.sub(r"^\w{64}$", "sha256", str(value)) 
    filename_pat = re.sub(r"^([^./]+[.][a-zA-Z][\w]{1,4})$", "filename", str(value))
    phone_pat = re.sub(r"^[4-9]\d{9}$", "phone", str(value))  
    filepath_pat = re.sub(r"^((/[\w_-]+)+[.][a-zA-Z][\w]{1,4})|([\w_-]+/)+[\w_-]+[.][a-zA-Z][\w]{1,4}$", "filepath", str(value))
    _id_pat = re.sub(r"^[\w]{8}[-][\w]{4}[-][\w]{4}[-][\w]{4}[-][\w]{12}$", "_id", str(value)) 
    agent_id_pat = re.sub(r"^A\d{4}$", "agent_id", str(value)) 
    borrower_id_pat = re.sub(r"^B\d{6}$", "borrower_id", str(value)) 
    name_pat = re.sub(r"[Nn]ame","names",str(key))
    if(value is None ):
        return value	
    elif(_id_pat != str(value)):
        return _id_pat
    elif('ObjectId' in  str(type(value))):
        return "ObjectId"
    elif(sha_pat != str(value)):
        return sha_pat
    elif(phone_pat != str(value)):
        return phone_pat
    elif(filepath_pat != str(value)):
        return filepath_pat
    elif(date_time_pat != str(value)):
        return date_time_pat
    elif(id_pat != str(value)):
        return id_pat
    elif(filename_pat != str(value)):
        return filename_pat
    elif(agent_id_pat != str(value)):
        return agent_id_pat
    elif(borrower_id_pat != str(value)):
        return borrower_id_pat
    elif(text_pat !=str(key)):
        return "sentence"
    elif(word_pat !=str(key)):
        return "word"
    elif(para_pat != str(value)):
        return para_pat
    elif(name_pat !=str(key)):
        if(len(value) != 0):
            return "name"
        else:
            return value
    elif(sentence_pat != str(value)):
        return sentence_pat
    elif(key_pat != str(value)):
        return key_pat
    elif(type(value) is int):
        count = 0
        for i in str(value):
            if(i.isdigit()):
                count = count + 1
        return "int-{}".format(int(count))
    elif(str(value).isdecimal()):
        count = 0
        for i in str(value):
            if(i.isdigit()):
                count = count + 1
        return "int_quotes-{}".format(int(count))
    elif(type(value) is bool):
        return "bool"
    elif(type(value) is float):
        return "float"
    elif(type(value) is str):
        if(len(value) != 0):
            return "str"
        else:
            return value
    elif(type(value) is datetime.datetime):
        return "datetime"
    else:
        return type(value)
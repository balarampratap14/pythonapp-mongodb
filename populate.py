from faker import Faker
from myobjectid import ObjectID
fake = Faker()
''' Number signs (‘#’) are replaced with a random digit (0 to 9).
    Question marks (‘?’) are replaced with a random character from letters.
    By default, letters contains all ASCII letters, uppercase and lowercase.
'''
def fake_id():
    ''' ########-####-####-####-############ '''
    x = [str(fake.random_number(fix_len=True,digits=8)),str(fake.random_number(fix_len=True,digits=4)),str(fake.random_number(fix_len=True,digits=4)),str(fake.random_number(fix_len=True,digits=4)),str(fake.random_number(fix_len=True,digits=12))]
    y = "-"
    fake_id = y.join(x)
    return fake_id
def fakeid():
    ''' '''
    x = fake.random_choices(elements=('A', 'B', 'C', 'D','E','F','G','H','I','J','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9'), length=16)
    x.append('@')
    y=""
    x.append(str(fake.ipv4()))
    fake_id = y.join(x)
    return fake_id
def fakeagentid():
    ''' A#### '''
    x = ['A']
    y=""
    x.append(str(fake.random_number(fix_len=True,digits=4)))
    fake_agentid = y.join(x)
    return fake_agentid
def fakeborrowerid():
    ''' B###### '''
    x = ['B']
    y=""
    x.append(str(fake.random_number(fix_len=True,digits=6)))
    fake_agentid = y.join(x)
    return fake_agentid
def fakekey():
    ''' ? or / or + of length=3123 and ening with = '''
    x = fake.random_choices(elements=('A', 'B', 'C', 'D','E','F','G','H','I','J','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','+','/'), length=3123)
    x.append('=')
    y=""
    fake_key = y.join(x)
    return fake_key
def fakenumeric(len):
    x = fake.random_choices(elements=('1','2','3','4','5','6','7','8','9'), length=int(len))
    y=""
    fake_key = y.join(x)
    return int(fake_key)
def fake_objects(data):
    if("int_quotes" in data):
        y = data.split('-')
        c = fakenumeric(y[-1])
        return str(c)
    elif("int" in data):
        y = data.split('-')
        c = fakenumeric(y[-1])
        return int(c)
    fake_data = {'_id': fake_id(),'ObjectId': ObjectID(), 'sha256': fake.sha256(raw_output=False) , 'phone': fake.phone_number() ,'filepath': fake.file_path(), 'filename': fake.file_name(), 'date-time': fake.iso8601(), 'datetime': fake.date_time_this_century(), 'id': fakeid(), 'agent_id': fakeagentid(), 'borrower_id': fakeborrowerid() ,'sentence': fake.sentence() ,'key': fakekey(), 'word': fake.word(),'text': fake.text(),'paragraph': fake.paragraph(), 'name': fake.name(), 'bool': fake.pybool(), 'float': fake.pyfloat(left_digits=2,positive=True), 'str': fake.pystr(min_chars=3, max_chars=20)}
    if str(data) in fake_data.keys():
        return fake_data[str(data)]
    elif str(data) == "":
        return data
    elif str(data) == 'None':
        return "None"
    else:
        return "NOT-FOUND"
		
def populate_list(x):
    count = 0
    for i in x:
        x[count] = populate(i)
        count = count+1     

def populate_dictionary(x):
    for key, value in x.items():
        x[key] = populate(value)

def populate(value):
    if(type(value) is list):
        populate_list(value)
        return value
    elif(type(value) is dict):
        populate_dictionary(value)
        return value
    res = fake_objects(str(value))
    return res
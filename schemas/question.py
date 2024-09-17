# Normal way
def questionEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "question":item["question"],
        "answer":item["email"],
        "category":item["category"],
        "difficulty":item["difficulty"],
        "role":item["role"]
    }

def questionsEntity(entity) -> list:
    return [questionEntity(item) for item in entity]
#Best way

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
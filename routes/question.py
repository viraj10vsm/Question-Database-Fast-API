# from fastapi import APIRouter, File, UploadFile
# from models.question import Question
# from config.db import conn
# from schemas.question import serializeDict, serializeList
# from bson import ObjectId
# import pandas as pd
# import io

# question = APIRouter()

# @question.get('/')
# async def find_all_questions():
#     return serializeList(conn.Interview_prep.question.find())

# # @question.get('/{id}')
# # async def find_one_question(id):
# #     return serializeDict(conn.Interview_prep.question.find_one({"_id":ObjectId(id)}))

# @question.post('/')
# async def create_question(question: Question):
#     conn.Interview_prep.question.insert_one(dict(question))
#     return serializeList(conn.Interview_prep.question.find())

# @question.put('/{id}')
# async def update_question(id, question: Question):
#     conn.Interview_prep.question.find_one_and_update({"_id": ObjectId(id)}, {
#         "$set": dict(question)
#     })
#     return serializeDict(conn.Interview_prep.question.find_one({"_id": ObjectId(id)}))

# @question.delete('/{id}')
# async def delete_question(id, question: Question):
#     return serializeDict(conn.Interview_prep.question.find_one_and_delete({"_id": ObjectId(id)}))

# # New endpoint to upload CSV and insert all rows into MongoDB
# @question.post('/upload_csv/')
# async def upload_csv(file: UploadFile = File(...)):
#     try:
#         # Read the file contents into a Pandas DataFrame
#         contents = await file.read()
#         df = pd.read_csv(io.StringIO(contents.decode('ISO-8859-1')))  # Adjust encoding if needed
        
#         # Ensure the DataFrame has the required columns
#         required_columns = ['question', 'answer', 'category', 'difficulty', 'role']
#         if not all(col in df.columns for col in required_columns):
#             return {"error": "CSV file must contain the following columns: 'question', 'answer', 'category', 'difficulty', 'role'."}
        
#         # Convert DataFrame to a list of dictionaries (for MongoDB insertion)
#         questions_list = df[required_columns].to_dict(orient='records')

#         # Insert the data into MongoDB in bulk
#         conn.Interview_prep.question.insert_many(questions_list)

#         return {"message": f"Successfully inserted {len(questions_list)} questions into the database."}
    
#     except Exception as e:
#         return {"error": str(e)}
from fastapi import APIRouter, File, UploadFile
from models.question import Question
from config.db import conn
from schemas.question import serializeDict, serializeList
from bson import ObjectId
import pandas as pd
import io

question = APIRouter()

@question.get('/')
async def find_all_questions():
    return serializeList(conn.Interview_prep.question.find())

# @question.get('/{id}')
# async def find_one_question(id):
#     return serializeDict(conn.Interview_prep.question.find_one({"_id":ObjectId(id)}))

@question.post('/')
async def create_question(question: Question):
    conn.Interview_prep.question.insert_one(dict(question))
    return serializeList(conn.Interview_prep.question.find())

@question.put('/{id}')
async def update_question(id, question: Question):
    conn.Interview_prep.question.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(question)
    })
    return serializeDict(conn.Interview_prep.question.find_one({"_id": ObjectId(id)}))

@question.delete('/{id}')
async def delete_question(id, question: Question):
    return serializeDict(conn.Interview_prep.question.find_one_and_delete({"_id": ObjectId(id)}))

# New endpoint to upload CSV and insert all rows into MongoDB
@question.post('/upload_csv/')
async def upload_csv(file: UploadFile = File(...)):
    try:
        # Read the file contents into a Pandas DataFrame
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode('ISO-8859-1')))  # Adjust encoding if needed
        
        # Ensure the DataFrame has the required columns
        required_columns = ['question', 'answer', 'category', 'difficulty', 'role']
        if not all(col in df.columns for col in required_columns):
            return {"error": "CSV file must contain the following columns: 'question', 'answer', 'category', 'difficulty', 'role'."}
        
        # Convert DataFrame to a list of dictionaries (for MongoDB insertion)
        questions_list = df[required_columns].to_dict(orient='records')

        # Insert the data into MongoDB in bulk
        conn.Interview_prep.question.insert_many(questions_list)

        return {"message": f"Successfully inserted {len(questions_list)} questions into the database."}
    
    except Exception as e:
        return {"error": str(e)}

from django.shortcuts import render
import pyrebase

from firebase_admin import firestore
from django.conf import settings

# def read_data_from_firestore():
#     db = firestore.client()
#     collection_ref = db.collection('test-project-01')
#     document_ref = collection_ref.document('doc01')
#     document_data = document_ref.get().to_dict()
#     # 데이터 처리 작업 수행

# def write_data_to_firestore():
#     db = firestore.client()
#     collection_ref = db.collection('collection_name')
#     document_ref = collection_ref.document('document_name')
#     data = {
#         'field1': 'value1',
#         'field2': 'value2',
#     }
#     document_ref.set(data)
#     # 데이터 작성 완료


def post_list(request):
    # read_data_from_firestore()
    # write_data_to_firestore()

    firebase_config = settings.FIREBASE_CONFIG
    firebase=pyrebase.initialize_app(firebase_config)
    #authe = firebase.auth()
    database = firestore.client()
    collection_ref = database.collection('test-project-01')  # 컬렉션 이름을 수정하세요
    doc_ref = collection_ref.document("doc01")
    #doc_ref = database.collection("test-project-01").document("doc01")
    doc = doc_ref.get().to_dict()


    # print(doc.to_dict())
    # doc = doc.to_dict()

    author = doc['author']
    title = doc['title']
    text = doc['text']





    return render(request,'maketeam/post_list.html',{"author":author,"title":title,"text":text }) 
    #return render(request,'maketeam/post_list.html',{}) 
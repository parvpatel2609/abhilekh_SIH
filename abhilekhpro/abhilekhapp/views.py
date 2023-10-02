from django.shortcuts import render
from django.http import HttpResponse
import pymongo
from pymongo import *


url = "mongodb+srv://intelkid:liberatedBlood_7@cluster0.npkyabd.mongodb.net/"
client = MongoClient(url)
db= client['']
collection = db['']




def index(request):
  return HttpResponse("Hello Geeks")
from flask import Flask,render_template,request
from dotenv import load_dotenv
import json





# instantiate Slack client
load_dotenv()



App=Flask(__name__)

@App.route('/data')
def GetData():
    val =open("data.json")
    jInter = json.load(val)
    val.close()
    return jInter

@App.route('/SetFalse',methods = ['GET'])
def PostData3():
    FileOpener = open('data.json')
    json_dict = request.get_json()
    data = json.load(FileOpener)
    setTo = False
    FileOpener.close()
    FileEditer = open('data.json','w')
    data['Results'] = setTo
    json.dump(data, FileEditer)
    FileEditer.close()
    return "Success"
    

@App.route('/SetRes',methods = ['POST'])
def PostData():
    FileOpener = open('data.json')
    json_dict = request.get_json()
    data = json.load(FileOpener)
    setTo = json_dict['res']
    FileOpener.close()
    if(setTo == True or setTo ==False):
        FileEditer = open('data.json','w')
        data['Results'] = setTo
        json.dump(data, FileEditer)
        FileEditer.close()
        return "Success"
    return "Failure"

@App.route('/SetSender',methods = ['POST'])
def PostData1():
    FileOpener = open('data.json')
    json_dict = request.get_json()
    data = json.load(FileOpener)
    setTo = json_dict['Sender']
    FileOpener.close()
    FileEditer = open('data.json','w')
    data['Sender'] = setTo
    json.dump(data, FileEditer)
    FileEditer.close()
    return "Success"


@App.route('/SetText',methods = ['POST'])
def PostData2():
    FileOpener = open('data.json')
    json_dict = request.get_json()
    data = json.load(FileOpener)
    setTo = json_dict['Text']
    FileOpener.close()
    FileEditer = open('data.json','w')
    data['Text'] = setTo
    json.dump(data, FileEditer)
    FileEditer.close()
    return "Success"
    

    

@App.route('/GetRes')
def GetDataFromFile():
    FileOpener = open('data.json')
    text = json.load(FileOpener)
    return str(text['Results'])



@App.route('/GetSender')
def GetDataFromFile1():
    FileOpener = open('data.json')
    text = json.load(FileOpener)
    return str(text['Sender'])



@App.route('/GetText')
def GetDataFromFile2():
    FileOpener = open('data.json')
    text = json.load(FileOpener)
    return str(text['Text'])




@App.route('/')
def index():
    
    return render_template('home.html')



if __name__ == "__main__":
    
    App.run(port=3000)
    

    
from flask import Flask, request,jsonify
app = Flask(__name__)
student=[
    {'name':'Rakesh','feedback':'5'},
    {'name':'Raghav','feedback':'5'},
    {'name':'Rahul','feedback':'5'}]
@app.route('/')
def hello_world():
    return 'Hello World'

#@app.route('/students',methods=['GET'])
#def get_students():
#    return student

@app.route('/students/<name>')
def get_students(name):
    return request.param.name

@app.route('/calculate/<numbera>/<sign>/<numberb>')
def calculator(numbera,sign,numberb):
    numberb=int(numberb)
    numbera=int(numbera)
    if (sign == '\'+\''):
        numbera=numbera+numberb
    elif (sign == '\'-\''):
        numbera=numbera-numberb
    elif (sign == '\' \ \''):
        numbera=numbera/numberb
    else:
        numbera=numbera*numberb
    return str(numbera)

if __name__== '__main__':
    app.run(debug=True)


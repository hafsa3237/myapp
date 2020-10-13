from flask import Flask,request,jsonify
app= Flask(__name__)
app.config["DEBUG"] = True

name = str(input("Enter a word:"))

@app.route('/', methods=['GET'])
def test():

    return jsonify('http://www.google.com')

if __name__ =='__main__':
    app.run()
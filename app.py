from flask import Flask, jsonify, request 
  
app = Flask(__name__) 
  
  
@app.route('/hello', methods=['GET']) 
def helloworld(): 
    if(request.method == 'GET'): 
        data = {"data": "AVJ Labs"} 
        return jsonify(data) 
  
  
if __name__ == '__main__': 
    app.run(debug=True)

from flask import Flask , request , jsonify
from PythonAlgos import is_prime , check_is_palindromic

app = Flask(__name__)

@app.route('/is_prime', methods=['GET'])
def check_prime():
    try:
        number = int(request.args.get('number'))
        if is_prime(number):
            return jsonify({"message": f"{number} is a prime number"})
        else:
            return jsonify({"message": f"{number} is not a prime number"})
    
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400



@app.route("/is_palindromic" , methods=['GET']) 
def check_is_palindromic() :
    try :
        number = int( request.args.get('number') )
        
        if  check_is_palindromic(n) : 
            return jsonify({"message": f"{number} is a palindromiic number"})
        else : 
             return jsonify({"message": f"{number} is Not a palindromiic number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400



# Start the server
if __name__ == '__main__':
    app.run(debug=True , port=8000)

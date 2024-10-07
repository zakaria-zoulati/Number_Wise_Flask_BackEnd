from flask import Flask , request , jsonify
from PythonAlgos import is_prime , is_palindromic , is_fibonacci , is_Lucas , is_triangular , is_pronic , is_polite , is_perfect , is_pentatope , is_pentagonal , is_octagonal , is_icosahedral , is_harshad , is_fermat , is_even,  is_deficient , is_cullen , is_catalan , is_automorphic
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
def check_palindrom() :
    try :
        number = int( request.args.get('number') )
        
        if is_palindromic(number) : 
            return jsonify({"message": f"{number} is a palindromiic number"})
        else : 
             return jsonify({"message": f"{number} is Not a palindromiic number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400



@app.route("/is_fibonacci" , methods=['GET']) 
def check_fibo() :
    try :
        number = int( request.args.get('number') )
        
        if is_fibonacci(number) : 
            return jsonify({"message": f"{number} is a Fibonacci number"})
        else : 
             return jsonify({"message": f"{number} is Not a Fibonacci number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    

@app.route("/is_lucas" , methods=['GET']) 
def check_is_lucas() :
    try :
        number = int( request.args.get('number') )
        
        if is_Lucas(number) : 
            return jsonify({"message": f"{number} is a Lucas number"})
        else : 
             return jsonify({"message": f"{number} is Not a Lucas number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    

@app.route("/is_triangular" , methods=['GET']) 
def check_triangular() :
    try :
        number = int( request.args.get('number') )
        if is_triangular(number) : 
            return jsonify({"message": f"{number} is a Triangular number"})
        else : 
             return jsonify({"message": f"{number} is Not a Traingular number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    


@app.route("/is_pronic" , methods=['GET']) 
def check_pronic() :
    try :
        number = int( request.args.get('number') )
        if is_pronic(number) : 
            return jsonify({"message": f"{number} is a Pronic number"})
        else : 
             return jsonify({"message": f"{number} is Not a Pronic number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    


@app.route("/is_polite" , methods=['GET']) 
def check_polite() :
    try :
        number = int( request.args.get('number') )
        if is_polite(number) : 
            return jsonify({"message": f"{number} is a Polite number"})
        else : 
             return jsonify({"message": f"{number} is Not a Polite number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    


    
@app.route("/is_perfect" , methods=['GET']) 
def check_perefct() :
    try :
        number = int( request.args.get('number') )
        if is_perfect(number) : 
            return jsonify({"message": f"{number} is a Perfect number"})
        else : 
             return jsonify({"message": f"{number} is Not a Perfect number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    



@app.route("/is_pentatope" , methods=['GET']) 
def check_pentatope() :
    try :
        number = int( request.args.get('number') )
        if is_pentatope(number) : 
            return jsonify({"message": f"{number} is a Pentatope number"})
        else : 
             return jsonify({"message": f"{number} is Not a Pentatope number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400


@app.route("/is_pentagonal" , methods=['GET']) 
def check_pentagonal() :
    try :
        number = int( request.args.get('number') )
        if is_pentagonal(number) : 
            return jsonify({"message": f"{number} is a Pentagonal number"})
        else : 
             return jsonify({"message": f"{number} is Not a Penatgonal number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400


@app.route("/is_ocatgonal" , methods=['GET']) 
def check_octagonal() :
    try :
        number = int( request.args.get('number') )
        if is_octagonal(number) : 
            return jsonify({"message": f"{number} is a Octagonal number"})
        else : 
             return jsonify({"message": f"{number} is Not an Octagonal number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400



@app.route("/is_icosahedral" , methods=['GET']) 
def check_icosahedral() :
    try :
        number = int( request.args.get('number') )
        if is_icosahedral(number) : 
            return jsonify({"message": f"{number} is a Icosahedral number"})
        else : 
             return jsonify({"message": f"{number} is Not an Icosahedral number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400


@app.route("/is_harshad" , methods=['GET']) 
def check_harshad() :
    try :
        number = int( request.args.get('number') )
        if is_harshad(number) : 
            return jsonify({"message": f"{number} is a Harshad number"})
        else : 
             return jsonify({"message": f"{number} is Not a Harshad number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400


@app.route("/is_fermat" , methods=['GET']) 
def check_fermat() :
    try :
        number = int( request.args.get('number') )
        if is_fermat(number) : 
            return jsonify({"message": f"{number} is a Fermat number"})
        else : 
             return jsonify({"message": f"{number} is Not a Fermat number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400


@app.route("/is_even" , methods=['GET']) 
def check_even() :
    try :
        number = int( request.args.get('number') )
        if is_even(number) : 
            return jsonify({"message": f"{number} is a Even number"})
        else : 
             return jsonify({"message": f"{number} is an Odd number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    
@app.route("/is_deficient" , methods=['GET']) 
def check_deficient() :
    try :
        number = int( request.args.get('number') )
        if is_deficient(number) : 
            return jsonify({"message": f"{number} is a Deficient number"})
        else : 
             return jsonify({"message": f"{number} is a Abundant number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400



@app.route("/is_cullen" , methods=['GET']) 
def check_cullen() :
    try :
        number = int( request.args.get('number') )
        if is_cullen(number) : 
            return jsonify({"message": f"{number} is a Cullen number"})
        else : 
             return jsonify({"message": f"{number} is not a Cullen number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400


@app.route("/is_catalan" , methods=['GET']) 
def check_catalan() :
    try :
        number = int( request.args.get('number') )
        if is_catalan(number) : 
            return jsonify({"message": f"{number} is a Catalan number"})
        else : 
             return jsonify({"message": f"{number} is not a Catalan number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400

@app.route("/is_automorphic" , methods=['GET']) 
def check_automorphic() :
    try :
        number = int( request.args.get('number') )
        if is_automorphic(number) : 
            return jsonify({"message": f"{number} is an Automorphic number"})
        else : 
             return jsonify({"message": f"{number} is not an Automorphic number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400


# Start the server
if __name__ == '__main__':
    app.run(debug=True , port=8000)

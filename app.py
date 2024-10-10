from flask import Flask , request , jsonify
from PythonAlgos import is_prime , is_palindromic , is_fibonacci , is_Lucas , is_triangular , is_pronic , is_polite , is_perfect , is_pentatope , is_pentagonal , is_octagonal , is_icosahedral , is_harshad , is_fermat , is_even,  is_deficient , is_cullen , is_catalan , is_automorphic , is_sphenic
app = Flask(__name__)

@app.route('/isPrime', methods=['GET'])
def check_prime():
    try:
        number = int(request.args.get('number'))
        if is_prime(number):
            return jsonify({"message": f"{number} is a prime number"})
        else:
            return jsonify({"message": f"{number} is not a prime number"})
    
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400



@app.route("/isPalindromic" , methods=['GET']) 
def check_palindrom() :
    try :
        number = int( request.args.get('number') )
        
        if is_palindromic(number) : 
            return jsonify({"message": f"{number} is a palindromiic number"})
        else : 
             return jsonify({"message": f"{number} is Not a palindromiic number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400



@app.route("/isFibonacci" , methods=['GET']) 
def check_fibo() :
    try :
        number = int( request.args.get('number') )
        
        if is_fibonacci(number) : 
            return jsonify({"message": f"{number} is a Fibonacci number"})
        else : 
             return jsonify({"message": f"{number} is Not a Fibonacci number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    

@app.route("/isLucas" , methods=['GET']) 
def check_is_lucas() :
    try :
        number = int( request.args.get('number') )
        
        if is_Lucas(number) : 
            return jsonify({"message": f"{number} is a Lucas number"})
        else : 
             return jsonify({"message": f"{number} is Not a Lucas number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    

@app.route("/isTriangular" , methods=['GET']) 
def check_triangular() :
    try :
        number = int( request.args.get('number') )
        if is_triangular(number) : 
            return jsonify({"message": f"{number} is a Triangular number"})
        else : 
             return jsonify({"message": f"{number} is Not a Traingular number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    


@app.route("/isPronic" , methods=['GET']) 
def check_pronic() :
    try :
        number = int( request.args.get('number') )
        if is_pronic(number) : 
            return jsonify({"message": f"{number} is a Pronic number"})
        else : 
             return jsonify({"message": f"{number} is Not a Pronic number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    


@app.route("/isPolite" , methods=['GET']) 
def check_polite() :
    try :
        number = int( request.args.get('number') )
        if is_polite(number) : 
            return jsonify({"message": f"{number} is a Polite number"})
        else : 
             return jsonify({"message": f"{number} is Not a Polite number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    


    
@app.route("/isPerfect" , methods=['GET']) 
def check_perefct() :
    try :
        number = int( request.args.get('number') )
        if is_perfect(number) : 
            return jsonify({"message": f"{number} is a Perfect number"})
        else : 
             return jsonify({"message": f"{number} is Not a Perfect number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    



@app.route("/isPentatope" , methods=['GET']) 
def check_pentatope() :
    try :
        number = int( request.args.get('number') )
        if is_pentatope(number) : 
            return jsonify({"message": f"{number} is a Pentatope number"})
        else : 
             return jsonify({"message": f"{number} is Not a Pentatope number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400


@app.route("/isPentagonal" , methods=['GET']) 
def check_pentagonal() :
    try :
        number = int( request.args.get('number') )
        if is_pentagonal(number) : 
            return jsonify({"message": f"{number} is a Pentagonal number"})
        else : 
             return jsonify({"message": f"{number} is Not a Pentagonal number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400


@app.route("/isOctagonal" , methods=['GET']) 
def check_octagonal() :
    try :
        number = int( request.args.get('number') )
        if is_octagonal(number) : 
            return jsonify({"message": f"{number} is a Octagonal number"})
        else : 
             return jsonify({"message": f"{number} is Not an Octagonal number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400



@app.route("/isIcosahedral" , methods=['GET']) 
def check_icosahedral() :
    try :
        number = int( request.args.get('number') )
        if is_icosahedral(number) : 
            return jsonify({"message": f"{number} is a Icosahedral number"})
        else : 
             return jsonify({"message": f"{number} is Not an Icosahedral number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400


@app.route("/isHarshad" , methods=['GET']) 
def check_harshad() :
    try :
        number = int( request.args.get('number') )
        if is_harshad(number) : 
            return jsonify({"message": f"{number} is a Harshad number"})
        else : 
             return jsonify({"message": f"{number} is Not a Harshad number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400


@app.route("/isFermat" , methods=['GET']) 
def check_fermat() :
    try :
        number = int( request.args.get('number') )
        if is_fermat(number) : 
            return jsonify({"message": f"{number} is a Fermat number"})
        else : 
             return jsonify({"message": f"{number} is Not a Fermat number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400


@app.route("/isEven" , methods=['GET']) 
def check_even() :
    try :
        number = int( request.args.get('number') )
        if is_even(number) : 
            return jsonify({"message": f"{number} is a Even number"})
        else : 
             return jsonify({"message": f"{number} is an Odd number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    
@app.route("/isDeficient" , methods=['GET']) 
def check_deficient() :
    try :
        number = int( request.args.get('number') )
        if is_deficient(number) : 
            return jsonify({"message": f"{number} is a Deficient number"})
        else : 
             return jsonify({"message": f"{number} is a Abundant number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400



@app.route("/isCullen" , methods=['GET']) 
def check_cullen() :
    try :
        number = int( request.args.get('number') )
        if is_cullen(number) : 
            return jsonify({"message": f"{number} is a Cullen number"})
        else : 
             return jsonify({"message": f"{number} is not a Cullen number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400


@app.route("/isCatalan" , methods=['GET']) 
def check_catalan() :
    try :
        number = int( request.args.get('number') )
        if is_catalan(number) : 
            return jsonify({"message": f"{number} is a Catalan number"})
        else : 
             return jsonify({"message": f"{number} is not a Catalan number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400

@app.route("/isAutomorphic" , methods=['GET']) 
def check_automorphic() :
    try :
        number = int( request.args.get('number') )
        if is_automorphic(number) : 
            return jsonify({"message": f"{number} is an Automorphic number"})
        else : 
             return jsonify({"message": f"{number} is not an Automorphic number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400
    
@app.route("/isSphenic" , methods=['GET']) 
def check_sphenic() :
    try :
        number = int( request.args.get('number') )
        if is_sphenic(number) : 
            return jsonify({"message": f"{number} is a Sphenic number"})
        else : 
             return jsonify({"message": f"{number} is not a Sphenic number"})
            
    except ValueError :
        return jsonify({"error": "Invalid input. Please provide an integer."}), 400


# Start the server
if __name__ == '__main__':
    app.run(debug=True , port=8000)

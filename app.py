from flask import Flask,render_template,request,jsonify
import math

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template('index.html')
 
@app.route('/math',methods = ['GET','POST'])
def math_operation():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        
        if(ops == 'add'):
            result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 + num2)
        
        if(ops == 'subtract'):
            result = 'the suntraction of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 - num2)
        
        if(ops == 'multiply'):
            result = 'the multiply of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 * num2)
        
        if(ops == 'divide'):
            result = 'the dividation of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 / num2)
        
        if(ops == 'log'):
            result = 'the log of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(math.log(num1,num2))

        return render_template('result.html',result = result)

@app.route('/postman_math',methods = ['POST'])
def math_operation1():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        
        if(ops == 'add'):
            result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 + num2)
        
        if(ops == 'subtract'):
            result = 'the suntraction of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 - num2)
        
        if(ops == 'multiply'):
            result = 'the multiply of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 * num2)
        
        if(ops == 'divide'):
            result = 'the dividation of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(num1 / num2)
        
        if(ops == 'log'):
            result = 'the log of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(math.log(num1,num2))

        return jsonify(result)

if __name__=="__main__":
    app.run(host="0.0.0.0")

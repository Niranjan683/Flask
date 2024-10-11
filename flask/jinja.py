from flask import Flask,render_template,request, redirect,url_for

'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application,
'''
#jinja 2 template engine
'''
{{ }} expressions to print output in html
{%....%} contions , and for loops
{#...#} this is for comments

'''





app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to home page.</h1><html>"

@app.route('/index',methods= ['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name = request.form['name']
        return f'Hello {name}!!'
    return render_template('form.html')

##Variable rule
#@app.route('/success/<int:score>')
#def success(score):
#    return "The marks you got is "+str(score)


#Building dynamic URL
@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res='PASS'
    else:
        res="FAIL"
    return render_template('result.html',results=res)


@app.route('/successres/<int:score>')
def successres(score):
    res=''
    if score>=50:   
        res='PASS'
    else:
        res="FAIL"
    exp={'score':score, "res":res}
    
    return render_template('result1.html',results=exp)

## if condition
'''@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html',results=score)
'''
@app.route('/fail/<int:score>')
def successif(score):
    return render_template('result.html',results=score)


@app.route('/getresults',methods=['POST','GET'])
def get_result():
    avg_mark=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        avg_mark = (science+c+maths+data_science)/4
    else:
        return render_template('getresult.html')

    return redirect(url_for("successres",score= avg_mark))




if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)


item1 = "colorful shoes"
item2 = "cargo pants"
item3 = "long sleeve shirt"
item4 = "short sleeve shirt"
item5 = "black and white socks"
item6 = "stylish hat"
item7 = "necklace"
item8 = "gold earrings"
item9 = "silver ring" 



@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    first = request.args['fname']
    last = request.args['lname']
    username = request.args['uname']
    password = request.args['psw']
    return render_template('page1.html',uname = username,psw = password)

@app.route("/p2")
def render_page2():
    return render_template('page2.html')
    
if __name__=="__main__":
    app.run(debug=False)

from flask import Flask,render_template,redirect,request
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<page_name>')
def service(page_name):
    return render_template(page_name)

def data_base(data):
    with open("../database.txt", mode="a") as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file_write=database.write(f"email={email} sub={subject} content={message}\n ")

def base_csv(data):
    with open("store.csv", newline='', mode="a") as db2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(db2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=="POST":
        data=request.form.to_dict()
        base_csv(data)
        return redirect("/thankyou.html")
    else:
        return "try again"

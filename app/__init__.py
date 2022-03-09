from flask import Flask

app = Flask(__name__)

@app.route("/")
def about_me():
    me = {
        "first_name": "Miles",
        "last_name": "Inada",
        "hobbies": "Building/Fixing Things",
        "active": True
    }
    return me

@app.route("/greet/<name>/")
def greet_user(fname, lname):
        return "<h1>Hello, %s</h1>" % (fname, lname)


@app.route("/square/<int:num>")
def square_num(num):
    return "<h1>%s square is: %s </h1>" % (num, num*num)

    
@app.route("/products")
def products():
    product_list = ["Apples", "Oranges", "Bananas"]
    bullet_list = "".join(
        "<li>%s</li>" % product for product in product_list
    )
    return "<ul>%s</ul>" % bullet_list
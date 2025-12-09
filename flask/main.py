from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    link = url_for("printTables")
    return f"<a href='{link}'> Tables Page </a>"

@app.route("/tablespage")
def printTables():
    inputStart = 1
    inputEnd = 11
    printTable = ""
    while inputStart <= inputEnd:
        for i in range(1, 11):
            printTable += f" {inputStart} x {i} = {inputStart * i}<br>"
        else: 
            printTable += "<br>"

        inputStart += 1
    return printTable

app.run()
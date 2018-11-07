from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('2.html', my_variable="test")


def get_state_options():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    list=[]
    for each county in counties:
        if !(county["state"] in list):
            list+=county["state"]
    a=""
    option=""
    for each state in list:
        option = option + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return option
        

if __name__=="__main__":
    app.run(debug=True, port=54321)

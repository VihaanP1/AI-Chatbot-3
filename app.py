import flask
from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__, template_folder="templates")

openai.api_key = "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"

@app.route("/", methods=["GET", "POST"])
def chat():
    response = ""
    if request.method == "POST":
        # Check if the clear button was clicked
        if request.form.get("clear") is not None:
            response = ""  # Clear the response
        else:
            question = request.form.get("question")  # Get the question if it's present
            if question:
                response = ask_ai(question)
    return render_template("index.html", response=response)

def ask_ai(question):
    ai_response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}]
    )
    return ai_response["choices"][0]["message"]["content"]
    

if __name__ == "__main__":
    app.run(debug=True)




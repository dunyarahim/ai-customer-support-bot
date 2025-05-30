from flask import Flask, request, render_template
import openai
import os

app = Flask(__name__)

#Not able to add my own API key to a public repository on Github
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_input = request.form["query"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful customer support agent for a small e-commerce business. Keep responses concise and professional."},
                {"role": "user", "content": user_input}
            ]
        )
        response_text = response["choices"][0]["message"]["content"]
    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

# ✅ Configure Gemini API Key
genai.configure(api_key=os.getenv("AIzaSyDwvGmfQNLfc7eIhUooI8IGSUbidckEeQE"))

model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""
    if request.method == "POST":
        text = request.form.get("input_text", "")
        if text.strip():
            try:
                response = model.generate_content(f"Summarize this:\n{text}")
                summary = response.text
            except Exception as e:
                summary = f"⚠️ Error: {str(e)}"
    return render_template("index.html", summary=summary)

# Required by Vercel
def handler(request):
    return app(request)


# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return jsonify({"message": "Hello from Flask on Vercel!"})
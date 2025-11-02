from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

# ✅ Use environment variable (don’t hardcode key)
genai.configure(api_key=os.getenv("AIzaSyDwvGmfQNLfc7eIhUooI8IGSUbidckEeQE"))

model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""
    if request.method == "POST":
        input_text = request.form.get("input_text", "")
        if input_text.strip():
            try:
                response = model.generate_content(f"Summarize this:\n{input_text}")
                summary = response.text
            except Exception as e:
                summary = f"⚠️ Error generating summary: {e}"
    return render_template("index.html", summary=summary)

# ✅ Required by Vercel for routing
def handler(request):
    return app(request)

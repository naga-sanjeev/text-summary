from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyDwvGmfQNLfc7eIhUooI8IGSUbidckEeQE")

model = genai.GenerativeModel("models/gemini-2.5-flash")

@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""
    if request.method == "POST":
        # ✅ Safely get form data
        input_text = request.form.get("input_text", "")
        if input_text.strip():
            try:
                response = model.generate_content(f"Summarize this:\n{input_text}")
                summary = response.text
            except Exception as e:
                summary = f"⚠️ Error generating summary: {e}"
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)

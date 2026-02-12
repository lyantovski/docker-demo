import os
from flask import Flask, request, render_template_string
import google.generativeai as genai

app = Flask(__name__)

# Gemini configuration via environment variables
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel(os.environ.get("MODEL_ENGINE", "gemini-2.0-flash"))

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Gemini AI Chat</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
               background: #0f0f23; color: #e0e0e0; min-height: 100vh;
               display: flex; justify-content: center; padding: 40px 20px; }
        .container { max-width: 800px; width: 100%; }
        h1 { text-align: center; margin-bottom: 30px; color: #58a6ff; }
        form { display: flex; gap: 10px; margin-bottom: 30px; }
        textarea { flex: 1; padding: 12px; border: 1px solid #333; border-radius: 8px;
                   background: #1a1a2e; color: #e0e0e0; font-size: 15px;
                   resize: vertical; min-height: 50px; }
        button { padding: 12px 24px; background: #238636; color: #fff; border: none;
                 border-radius: 8px; cursor: pointer; font-size: 15px; font-weight: 600; }
        button:hover { background: #2ea043; }
        .response { background: #1a1a2e; border: 1px solid #333; border-radius: 8px;
                    padding: 20px; white-space: pre-wrap; line-height: 1.6; }
        .label { font-size: 13px; color: #8b949e; margin-bottom: 8px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Gemini AI Chat</h1>
        <form method="POST">
            <textarea name="prompt" placeholder="Enter your prompt..."
                      rows="2">{{ prompt or '' }}</textarea>
            <button type="submit">Send</button>
        </form>
        {% if response %}
        <div class="label">Response:</div>
        <div class="response">{{ response }}</div>
        {% endif %}
    </div>
</body>
</html>
"""


def generate_text(prompt):
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            max_output_tokens=1024,
            temperature=0.7,
        ),
    )
    return response.text.strip()


@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    prompt = None
    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        if prompt:
            try:
                response = generate_text(prompt)
            except Exception as e:
                response = f"Error: {e}"
    return render_template_string(HTML, prompt=prompt, response=response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

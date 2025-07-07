from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # Get the port from environment variable or default to 5000
    port = int(os.environ.get("PORT", 5000))
    
    # Run the Flask app, listening on 0.0.0.0 for external access
    app.run(debug=False, host="0.0.0.0", port=port)

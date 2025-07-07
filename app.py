from flask import Flask, render_template  # Import Flask and render_template function

app = Flask(__name__)  # Create a Flask app instance

@app.route("/")  # Define a route for the homepage ("/")
def home():
    # Render the "index.html" template located in the "templates" folder
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

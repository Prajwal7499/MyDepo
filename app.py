from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Flask PaaS Web App</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f4; padding: 50px; }
                h1 { color: #007bff; }
                p { font-size: 18px; color: #333; }
            </style>
        </head>
        <body>
            <h1>Welcome to My PaaS Web App</h1>
            <p>Hello, this is a PaaS deployed web app! by <b>Ajinkya, 22510030</b></p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    # Let's return some basic HTML!
    return """
    <html>
    <head>
        <title>My AWS Project</title>
        <style>
            body { 
                background-color: #2C3E50; 
                color: #ECF0F1; 
                font-family: Arial, sans-serif; 
                text-align: center; 
                padding-top: 100px;
            }
            h1 { 
                color: #3498DB; 
                font-size: 48px;
            }
            p {
                font-size: 24px;
            }
        </style>
    </head>
    <body>
        <h1>It Worked!</h1>
        <p>This page was deployed by my CI/CD pipeline!</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
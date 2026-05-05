from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    text = "Cloud Computing"

    reversed_text = text[::-1]

    a, b = 20, 5
    subtraction = a - b
    multiplication = a * b

    return f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial;
                background: linear-gradient(to right, #ff9a9e, #fad0c4);
                text-align: center;
                padding: 50px;
            }}

            .box {{
                background: white;
                padding: 30px;
                border-radius: 15px;
                width: 50%;
                margin: auto;
                box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            }}

            h2 {{
                color: #333;
            }}

            p {{
                font-size: 18px;
            }}
        </style>
    </head>

    <body>
        <div class="box">
            <h2>✨ Operations App</h2>

            <p><b>Original String:</b> {text}</p>
            <p><b>Reversed String:</b> {reversed_text}</p>

            <p><b>Numbers:</b> {a}, {b}</p>
            <p><b>Subtraction:</b> {subtraction}</p>
            <p><b>Multiplication:</b> {multiplication}</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <style>
            body {
                font-family: Arial;
                background: linear-gradient(to right, #a1c4fd, #c2e9fb);
                text-align: center;
                padding: 50px;
            }

            .box {
                background: white;
                padding: 30px;
                border-radius: 15px;
                width: 50%;
                margin: auto;
                box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            }

            input {
                padding: 10px;
                margin: 10px;
                width: 80%;
            }

            button {
                padding: 10px 20px;
                background: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h2>✨ Operations App</h2>

            <form action="/result" method="post">
                <input type="text" name="text" placeholder="Enter a string" required><br>
                <input type="number" name="num1" placeholder="Enter first number" required><br>
                <input type="number" name="num2" placeholder="Enter second number" required><br>

                <button type="submit">Calculate</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.route('/result', methods=['POST'])
def result():
    text = request.form['text']
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])

    reversed_text = text[::-1]
    subtraction = num1 - num2
    multiplication = num1 * num2

    return f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial;
                background: linear-gradient(to right, #fbc2eb, #a6c1ee);
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
        </style>
    </head>

    <body>
        <div class="box">
            <h2>✅ Results</h2>

            <p><b>Original String:</b> {text}</p>
            <p><b>Reversed String:</b> {reversed_text}</p>

            <p><b>Subtraction:</b> {subtraction}</p>
            <p><b>Multiplication:</b> {multiplication}</p>

            <br>
            <a href="/">Go Back</a>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

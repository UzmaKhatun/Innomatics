from flask import Flask, request, render_template_string
import random
import datetime

app = Flask(__name__)

# HTML Template with some CSS for a "cool" look
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Creative Flask App</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            text-align: center;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 3rem;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            border: 1px solid rgba(255, 255, 255, 0.18);
            max-width: 500px;
        }
        h1 { font-size: 3rem; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 2px; }
        .original { font-style: italic; opacity: 0.8; margin-bottom: 2rem; }
        .feature-box {
            margin-top: 2rem;
            padding: 1rem;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            font-size: 1.1rem;
        }
        .footer { margin-top: 2rem; font-size: 0.8rem; opacity: 0.6; }
        .accent { color: #00f2fe; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        {% if name %}
            <p class="original">Hello, {{ original_name }}</p>
            <h1>{{ name }}</h1>
            
            <div class="feature-box">
                <p>✨ <span class="accent">Fortune:</span> {{ fortune }}</p>
                <p>🎨 <span class="accent">Vibe Color:</span> <span style="color: {{ color }}; text-shadow: 1px 1px 2px black;">{{ color }}</span></p>
                <p>🔢 <span class="accent">Lucky Number:</span> {{ lucky_number }}</p>
            </div>
        {% else %}
            <h1>Welcome!</h1>
            <p>Please provide a name in the URL,</p>
            <p>e.g., <code>/?name=Innominion</code></p>
        {% endif %}
        
        <div class="footer">
            Generated at {{ timestamp }}
        </div>
    </div>
</body>
</html>
"""

def get_fortune(name):
    fortunes = [
        "A thrilling time is in your immediate future.",
        "Your creative energy will lead to great success.",
        "A bold move will bring you unexpected rewards.",
        "Your kindness will open doors you never knew existed.",
        "Today is a great day to start something new!",
        "You will find what you are looking for in the most unexpected place."
    ]
    # Use name length as a seed for consistent "fortunes" for the same name
    random.seed(len(name))
    return random.choice(fortunes)

def get_vibe_color(name):
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F333FF", "#FF33A1", "#33FFF5", "#F5FF33"]
    random.seed(sum(ord(c) for c in name))
    return random.choice(colors)

@app.route('/')
def hello():
    name = request.args.get('name', '')
    if name:
        upper_name = name.upper()
        fortune = get_fortune(name)
        vibe_color = get_vibe_color(name)
        lucky_number = (sum(ord(c) for c in name) % 100) + 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return render_template_string(
            HTML_TEMPLATE, 
            name=upper_name, 
            original_name=name,
            fortune=fortune,
            color=vibe_color,
            lucky_number=lucky_number,
            timestamp=timestamp
        )
    else:
        return render_template_string(HTML_TEMPLATE, name=None, timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Alert log file path
ALERT_FILE = os.path.expanduser("~/SOC_Project/logs/alerts.log")

# Dashboard HTML
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>SOC Dashboard</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body {
            background-color: #0b0b0b;
            color: #00ff00;
            font-family: Arial;
            padding: 20px;
        }
        h1 {
            color: red;
        }
        .alert {
            border: 1px solid red;
            padding: 10px;
            margin: 10px;
            background-color: #1a1a1a;
        }
    </style>
</head>
<body>

<h1>🛡️ SOC Threat Detection Dashboard</h1>
<h3>Real-Time Alerts:</h3>

{% for alert in alerts %}
<div class="alert">
    {{ alert }}
</div>
{% endfor %}

</body>
</html>
"""

@app.route("/")
def home():
    if os.path.exists(ALERT_FILE):
        with open(ALERT_FILE, "r") as f:
            alerts = f.readlines()
    else:
        alerts = ["No alerts detected"]

    alerts.reverse()
    return render_template_string(HTML, alerts=alerts)

if __name__ == "__main__":
    app.run(debug=True)


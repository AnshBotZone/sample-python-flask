import os
import psutil
import datetime
from flask import Flask
from flask import render_template

app = Flask(__name__)

def get_stats():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    cpu_cores = psutil.cpu_count()
    cpu_frequency = psutil.cpu_freq().current
    cpu_usage = psutil.cpu_percent(interval=1)
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()
    disk = psutil.disk_usage('/')
    net_io = psutil.net_io_counters()

    html_report = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Server Statistics Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
        }}
        .report-container {{
            width: 80%;
            margin: auto;
        }}
        .section {{
            margin-bottom: 20px;
        }}
        h1 {{
            text-align: center;
        }}
        .section-title {{
            font-size: 1.5em;
            margin-bottom: 10px;
        }}
        .stat {{
            margin-bottom: 5px;
        }}
    </style>
</head>
<body>
    <div class="report-container">
        <h1>Server Statistics Report</h1>

        <div class="section">
            <div class="section-title">Boot Time</div>
            <div class="stat">Boot Time: {boot_time}</div>
        </div>

        <div class="section">
            <div class="section-title">CPU</div>
            <div class="stat">Cores: {cpu_cores}</div>
            <div class="stat">Frequency: {cpu_frequency:.2f} MHz</div>
            <div class="stat">Usage: {cpu_usage}%</div>
        </div>

        <div class="section">
            <div class="section-title">Memory</div>
            <div class="stat">Total: {virtual_mem.total / (1024**3):.2f} GB</div>
            <div class="stat">Available: {virtual_mem.available / (1024**3):.2f} GB</div>
            <div class="stat">Used: {virtual_mem.used / (1024**3):.2f} GB</div>
            <div class="stat">Percentage: {virtual_mem.percent}%</div>
        </div>

        <div class="section">
            <div class="section-title">Swap Memory</div>
            <div class="stat">Total: {swap_mem.total / (1024**3):.2f} GB</div>
            <div class="stat">Used: {swap_mem.used / (1024**3):.2f} GB</div>
            <div class="stat">Free: {swap_mem.free / (1024**3):.2f} GB</div>
            <div class="stat">Percentage: {swap_mem.percent}%</div>
        </div>

        <div class="section">
            <div class="section-title">Disk</div>
            <div class="stat">Total: {disk.total / (1024**3):.2f} GB</div>
            <div class="stat">Used: {disk.used / (1024**3):.2f} GB</div>
            <div class="stat">Free: {disk.free / (1024**3):.2f} GB</div>
            <div class="stat">Percentage: {disk.percent}%</div>
        </div>

        <div class="section">
            <div class="section-title">Network I/O</div>
            <div class="stat">Bytes Sent: {net_io.bytes_sent / (1024**2):.2f} MB</div>
            <div class="stat">Bytes Received: {net_io.bytes_recv / (1024**2):.2f} MB</div>
        </div>
    </div>
</body>
</html>
"""
    return html_report

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/stats")
def stats():
    stats_report = get_stats()
    return stats_report

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

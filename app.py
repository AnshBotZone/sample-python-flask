from flask import Flask

from helper import get_speed_test, get_stats

app = Flask(__name__)


@app.route("/")
def hello():
    return "Server Running!"


@app.route("/stats")
def stats():
    stats_report = get_stats()
    return stats_report


@app.route("/speedtest")
def speedtest():
    speed_test = get_speed_test()
    return speed_test


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

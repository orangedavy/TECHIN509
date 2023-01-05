from flask import Flask, render_template, request, redirect
# from logic import *

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template('Home.html')

@app.route("/play")
def play():
    mode = request.args.get('mode')
    player_x = request.args.get('name_x')
    player_o = request.args.get('name_o')
    return render_template('Play.html', mode=mode, player_x=player_x, player_o=player_o)

@app.route("/stats")
def stats():
    return render_template('Leaderboard.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5001)

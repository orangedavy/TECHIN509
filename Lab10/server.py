from flask import Flask, render_template, request, redirect
# from logic import *

app = Flask(__name__)

# renders index template for both original and home routes
@app.route("/")
@app.route("/home")
def index():
    return render_template('Home.html')

# renders play template for main game and extracts parameters from url
@app.route("/play")
def play():
    mode = request.args.get('mode')
    player_x = request.args.get('name_x')
    player_o = request.args.get('name_o')
    return render_template('Play.html', mode=mode, player_x=player_x, player_o=player_o)

# renders html template for leaderboard
@app.route("/stats")
def stats():
    return render_template('Leaderboard.html')

# redirects 400 error
@app.errorhandler(400)
def bad_request(e):
    return redirect("/home")

# redirects 404 error
@app.errorhandler(404)
def bad_request(e):
    return redirect("/home")

# redirects 500 error
@app.errorhandler(500)
def bad_request(e):
    return redirect("/")

if __name__ == '__main__':
    app.debug = True  # debug mode
    app.run(host='0.0.0.0', port=5001)  # different port

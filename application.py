from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp
from tictactoe import TicTacToe
from MiniMax import minimax
import copy

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

game = TicTacToe(3)

@app.route("/")
def index():

    if "board" not in session:
        session["board"] = game.board
        session["turn"] = "X"

    return render_template("game.html", game=session["board"], turn=session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    game.move(row, col, session['turn'])
    session["board"] = game.board

    if(game.check()):
        return redirect(url_for("gamewon"))
    else:
        if session["turn"] == "X":
            session["turn"] = "O"
        else:
            session["turn"] = "X"
        return redirect(url_for("index"))

@app.route("/gamewon")
def gamewon():
    return render_template("gamewon.html", winner=session['turn'], game = game.board)

@app.route("/reset")
def reset():
    game.clear()
    session["board"] = game.board
    session["turn"] = "X"
    return redirect(url_for('index'))

@app.route('/compmove')
def compmove():
    moves = []
    for i in range(3):
        for j in range(3):
            if game.board[i][j]=="":
                moves.append((i, j))
    values = []
    for move in moves:
        testboard = copy.deepcopy(game.board)
        testboard[move[0]][move[1]] = session['turn']
        if session["turn"] == "X":
            newturn = "O"
        else:
            newturn = "X"
        values.append(minimax(testboard, newturn))
    
    if(session['turn'] == "X"):
        bestmove = max(values)
    else:
        bestmove = min(values)

    try:
        move = moves[values.index(bestmove)]
    except:
        print('SOMETHINGS GONE AWFULLY AWRY')
        print(moves)
        print(values)
        print(bestmove)

    game.move(move[0], move[1], session['turn'])
    session["board"] = game.board

    if(game.check()):
        return redirect(url_for("gamewon"))
    else:
        if session["turn"] == "X":
            session["turn"] = "O"
        else:
            session["turn"] = "X"
        return redirect(url_for("index"))

def check():
    for row in session['board']:
        if row.count('X') == 3:
            return redirect(url_for("Xwon"))
        if row.count('O') == 3:
            return redirect(url_for("Owon"))

  
    return redirect(url_for("index"))
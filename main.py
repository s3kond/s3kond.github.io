from flask import Flask, render_template, request, jsonify, g
import sqlite3

app = Flask(__name__)
DATABASE = 'coins.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT username, coins, profit_per_tap, energy FROM users WHERE id=1")
    user = cursor.fetchone()
    username, coins, profit_per_tap, energy = user
    return render_template('index.html', username=username, coins=coins, profit_per_tap=profit_per_tap, energy=energy)

@app.route('/update_coins', methods=['POST'])
def update_coins():
    data = request.get_json()
    coins = data.get('coins')
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE users SET coins = ? WHERE id = 1", (coins,))
    db.commit()
    return jsonify(success=True)

@app.route('/upgrade', methods=['POST'])
def upgrade():
    data = request.get_json()
    upgrade_type = data.get('type')
    db = get_db()
    cursor = db.cursor()
    if upgrade_type == 'profit':
        cursor.execute("UPDATE users SET profit_per_tap = profit_per_tap + 1 WHERE id = 1")
    elif upgrade_type == 'energy':
        cursor.execute("UPDATE users SET energy = energy + 500 WHERE id = 1")
    db.commit()
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)

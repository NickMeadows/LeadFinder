from flask import Blueprint, render_template, request, redirect, url_for
from app.db import get_db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    db = get_db()
    articles = db.execute('SELECT * FROM articles ORDER BY published_at DESC').fetchall()
    return render_template('index.html', articles=articles)

@main.route('/note/<int:article_id>', methods=['POST'])
def update_note(article_id):
    note = request.form['note']
    db = get_db()
    db.execute('UPDATE articles SET notes = ? WHERE id = ?', (note, article_id))
    db.commit()
    return redirect(url_for('main.index'))

from flask import Flask, request, render_template
from utils import *

app = Flask(__name__)
candidates = load_candidates_from_json()


@app.route('/')
def get_all_candidates():
    """представление для списка всех кандидатов"""
    return render_template('list.html', items=candidates)


@app.route('/candidate/<int:uid>')
def get_candidate_form(uid):
    """представление для карточки кандидата по номеру"""
    user = get_candidate(candidates, uid)
    return render_template('card.html', user=user)


@app.route('/search/<search_name>')
def get_search_by_name(search_name):
    """представление для списка кандидатов по имени"""
    users = get_candidates_by_name(candidates, search_name)
    return render_template('search.html', items=users, count=len(users))


@app.route('/skill/<skill_name>')
def get_search_by_skill(skill_name):
    """представление для списка кандидатов по навыку"""
    users = get_candidates_by_skill(candidates, skill_name)
    return render_template('search.html', items=users, count=len(users), skill=skill_name)


app.run()

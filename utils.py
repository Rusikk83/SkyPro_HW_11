import json


def load_candidates_from_json(path="candidates.json"):
    with open(path, encoding='utf-8') as file:
        data = file.read()
    candidates = json.loads(data)
    return candidates


def get_candidate(candidates, candidate_id):
    """возвращает одного кандидата по его id"""
    for el in candidates:
        if el["id"] == candidate_id:
            return el


def get_candidates_by_name(candidates, candidate_name):
    """возвращает кандидатов по имени"""
    candidates_by_name = []
    for el in candidates:
        if candidate_name.lower() in el["name"].lower():
            candidates_by_name.append(el)
    return candidates_by_name


def get_candidates_by_skill(candidates, skill_name):
    """возвращает кандидатов по навыку"""
    candidates_by_skill = []
    for el in candidates:
        if skill_name.lower() in el["skills"].lower().split(", "):
            candidates_by_skill.append(el)
    return candidates_by_skill






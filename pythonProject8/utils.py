import json

from pip._internal.resolution.resolvelib import candidates


def load_candidates(path):
    """загрузка кандидатов"""

    with open(path, "r", encoding="UTF-8") as candidates:
        return json.load(candidates)


def format_candidates(candidates_list):
    """ вывод всех кандидатов по имени,позиции, навыкам"""
    result = "<pre>"
    for candidate in candidates_list:
        result += (
            "<pre>"
            f"Имя кандидата - {candidate['name']}\n"
            f"Позиция кандидата - {candidate['position']}\n"
            f"Навыки через запятую - {candidate['skills']}\n\n"
        )
    result += "<pre>"
    return result


def load_candidate_by_id(candidates_list, candidate_id):
    """ загрузка кандидатов по номеру идентификатора"""
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate


def load_candidate_by_skill(candidates_list, candidate_skill):
    """ загрузка кандидата по определенному навыку"""
    result = []
    for candidate in candidates_list:
        candidate_skills = candidate['skills'].lower().split(", ")
        if candidate_skill.lower() in candidate_skills:
            result.append(candidate)
    return result

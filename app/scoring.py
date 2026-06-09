DANGER_KEYWORDS = { 
    "haven't started": 25,
    "overdue": 30,
    "failing": 25,
    "deadline": 20,
    "tomorrow": 15,
    "exam": 15,
    "3am": 15,
    "panic": 15,
    "due": 10,
}

CHILL_KEYWORDS = {
    "plenty of time": 30,
    "finished": 25,
    "prepared": 20,
    "relaxed": 20,
    "ready": 15,
    "early": 15,
    "done": 15,
}

BASE_SCORE = 30


def score_situation(text: str) -> int:
    text = text.lower()
    score = BASE_SCORE

    for keyword, points in DANGER_KEYWORDS.items():
        if keyword in text:
            score += points

    for keyword, points in CHILL_KEYWORDS.items():
        if keyword in text:
            score -= points

    if score < 0:
        score = 0
    if score > 100:
        score = 100

    return score


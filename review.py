def clean_scores(scores):
    valid = []
    for s in scores:
        if s is not None and (type(s) == float or type(s) == int) and 0 <= s <= 100:
            valid.append(s)
    return valid
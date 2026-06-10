def format_output(value):
    return f"[OUTPUT]: {value}"

def clamp(value, min_val, max_val):
    return max(min_val, min(max_val, value))

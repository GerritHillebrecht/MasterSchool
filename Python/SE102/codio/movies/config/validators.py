def is_float(string_to_check: str) -> bool:
    try:
        float(string_to_check)
        return True
    except ValueError:
        return False

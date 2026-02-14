def analyze_code_logic(code: str) -> str:
    suggestions = []

    if "print(" in code:
        suggestions.append("Avoid using print statements in production code. Use logging instead.")

    if "==" in code and "is" not in code:
        suggestions.append("Consider using 'is' for None comparisons.")

    if "import *" in code:
        suggestions.append("Avoid wildcard imports to improve readability and maintainability.")

    if len(code.splitlines()) > 50:
        suggestions.append("Consider breaking this function into smaller units for readability.")

    if not suggestions:
        suggestions.append("Code looks good. Consider adding type hints and docstrings for maintainability.")

    return "\n".join(suggestions)
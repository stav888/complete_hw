"""Small guarded tool-using agent without requiring an API key."""
import ast
import csv
import json
import operator
from datetime import datetime, timezone
from urllib.parse import quote
from urllib.request import Request, urlopen
import re
from pathlib import Path

_ALLOWED_OPERATORS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv, ast.Pow: operator.pow}


def calculator(expression):
    tree = ast.parse(expression, mode="eval")

    def evaluate(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_OPERATORS:
            return _ALLOWED_OPERATORS[type(node.op)](evaluate(node.left), evaluate(node.right))
        raise ValueError("only basic arithmetic is allowed")

    return evaluate(tree.body)


def read_csv_summary(path, allowed_root=None):
    file_path = Path(path).resolve()
    root = Path(allowed_root or Path.cwd()).resolve()
    if root not in file_path.parents:
        raise PermissionError("CSV path is outside the allowed directory")
    with file_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return {"path": str(file_path), "rows": len(rows), "columns": list(rows[0]) if rows else []}


def search_web(query):
    if not query or len(query) > 300:
        raise ValueError("query must contain 1-300 characters")
    try:
        request = Request(f"https://html.duckduckgo.com/html/?q={quote(query)}", headers={"User-Agent": "course-agent/1.0"})
        html = urlopen(request, timeout=5).read().decode("utf-8", errors="ignore")
        text = re.sub(r"<[^>]+>", " ", html)
        text = re.sub(r"\s+", " ", text).strip()
        return {"query": query, "evidence": text[:1200], "limitations": "Search snippets require source verification."}
    except OSError as error:
        return {"query": query, "evidence": [], "limitations": f"Search unavailable: {error}"}


def run_agent(request, max_steps=3, log_path="agent_steps.jsonl"):
    if max_steps < 1 or max_steps > 10:
        raise ValueError("max_steps must be between 1 and 10")
    lower = request.lower()
    selected_tool = "none"
    tool_args = {}
    status = "ok"
    if any(term in lower for term in ("ignore previous", "reveal system prompt", "exfiltrate")):
        result = {"answer": "Request rejected by prompt-injection defense.", "evidence": [], "limitations": []}
    elif lower.startswith("calculate "):
        expression = request[len("calculate "):].strip()
        selected_tool = "calculator"
        tool_args = {"expression": expression}
        try:
            result = {"answer": calculator(expression), "evidence": ["local calculator"], "limitations": []}
        except (SyntaxError, ValueError, ZeroDivisionError) as error:
            status = "error"
            result = {"answer": f"Calculator error: {error}", "evidence": [], "limitations": []}
    else:
        result = {"answer": "Use 'calculate <expression>' for the offline demo.", "evidence": [], "limitations": ["No live search provider is configured."]}
    with Path(log_path).open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({"timestamp": datetime.now(timezone.utc).isoformat(), "user_query": request, "selected_tool": selected_tool, "tool_args": tool_args, "tool_result_status": status, "total_step_count": 1, "result": result}) + "\n")
    return result


if __name__ == "__main__":
    print(run_agent("calculate 2 + 3 * 4"))

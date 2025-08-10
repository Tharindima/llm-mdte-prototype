"""
generator.py

Provides:
- generate_tests_using_llm(module_path, prompt, mode="demo"|"real")
"""

import os
import textwrap
from typing import List, Optional

# If using OpenAI in real mode:
try:
    from openai import OpenAI  # new official client
except Exception:
    OpenAI = None

def _mock_llm_generate(module_name: str, functions: List[str]):
    """Return a string with pytest tests (mock LLM)."""
    tests = f"""
import pytest
from {module_name} import *

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_divide_basic():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
"""
    return textwrap.dedent(tests)

def generate_tests_using_llm(module_name: str,
                             functions: List[str],
                             prompt: Optional[str] = None,
                             mode: str = "demo",
                             model: str = "gpt-4o-mini"):
    """
    mode: "demo" uses mock content (no network)
          "real" uses OpenAI API (requires OPENAI_API_KEY env var).
    Returns generated test code as string.
    """
    if mode == "demo":
        return _mock_llm_generate(module_name, functions)

    # --------- real mode (calls OpenAI) ----------
    if OpenAI is None:
        raise RuntimeError("OpenAI library not installed. pip install openai-client or use demo mode")

    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise RuntimeError("Set OPENAI_API_KEY environment variable for real mode")

    client = OpenAI(api_key=api_key)
    # Build a helpful prompt (you should refine and iterate)
    system_msg = {
        "role": "system",
        "content": "You are an expert test engineer that writes clear, runnable pytest tests. Output only Python test code."
    }
    #user_prompt = prompt or f"Generate pytest tests for module `{module_name}`. Functions: {functions}. Include edge cases."
    user_prompt = prompt or f"""
Generate pytest tests for module `{module_name}` covering functions {functions}.
- Use equivalence partitioning.
- Include positive, negative, and edge case inputs.
- Assert correct outputs and handle exceptions.
"""

    messages = [
        system_msg,
        {"role":"user","content": user_prompt}
    ]

    resp = client.chat.completions.create(model=model, messages=messages, max_tokens=800)
    # response extraction depends on client library; adjust if necessary
    text = resp.choices[0].message.content
    text = clean_generated_code(text)
    return text

def clean_generated_code(code):
    # Remove Markdown code fences if present
    code = code.strip()
    if code.startswith("```"):
        code = "\n".join(line for line in code.splitlines() if not line.strip().startswith("```"))
    return code

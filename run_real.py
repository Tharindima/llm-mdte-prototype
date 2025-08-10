from generator import generate_tests_using_llm
from runner import write_tests_and_run

# Tell it which module to test
module_name = "sample_app.sample_app"
functions_to_test = ["add", "divide"]

# Ask the real LLM to write pytest tests
generated = generate_tests_using_llm(
    module_name,
    functions_to_test,
    mode="real",              
    model="gpt-4o-mini"       
)

# Save and run them
rc, out, err = write_tests_and_run(".", generated)

print("Generated tests:\n", generated)
print("\nPytest output:\n", out)
if err:
    print("\nPytest errors:\n", err)

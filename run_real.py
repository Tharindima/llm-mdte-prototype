import argparse
from generator import generate_tests_using_llm
from runner import write_tests_and_run

def main():
    parser = argparse.ArgumentParser(description="LLM Test Generator and Runner")
    parser.add_argument(
        "-m", "--module", required=True, help="Module name to test (e.g., sample_app.sample_app)"
    )
    parser.add_argument(
        "-f", "--functions", required=True, nargs="+",
        help="List of function names to generate tests for (space separated)"
    )
    parser.add_argument(
        "--mode", default="demo", choices=["demo", "real"],
        help="Mode to run test generation: demo (default) or real (OpenAI)"
    )
    parser.add_argument(
        "--model", default="gpt-4o-mini",
        help="OpenAI model name to use (default: gpt-4o-mini)"
    )

    args = parser.parse_args()

    # Generate tests using provided inputs
    generated_tests = generate_tests_using_llm(
        args.module,
        args.functions,
        mode=args.mode,
        model=args.model
    )

    # Write tests to file and run pytest
    rc, out, err = write_tests_and_run(".", generated_tests)

    print("Generated tests:\n", generated_tests)
    print("\nPytest output:\n", out)
    if err:
        print("\nPytest errors:\n", err)

if __name__ == "__main__":
    main()

from flask import Flask, render_template, request
from generator import generate_tests_using_llm
from runner import write_tests_and_run

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    generated = ""
    pytest_out = ""
    pytest_err = ""
    if request.method == "POST":
        module_name = request.form.get("module_name")
        functions = request.form.get("functions").split(",")
        mode = request.form.get("mode", "demo")

        generated = generate_tests_using_llm(module_name, functions, mode=mode)
        rc, pytest_out, pytest_err = write_tests_and_run(".", generated)

    return render_template("index.html",
                           generated=generated,
                           pytest_out=pytest_out,
                           pytest_err=pytest_err)

if __name__ == "__main__":
   # app.run(debug=True)
   #app.run(debug=True, extra_files=[], use_reloader=True)
   app.run(debug=False)


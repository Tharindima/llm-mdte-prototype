# LLM-Powered Model Driven Test Engineering Prototype

## Overview
This project demonstrates a prototype for automated software test generation using Large Language Models (LLMs), specifically OpenAI’s GPT models. Given a target module and function names, the system generates Python test cases using the OpenAI API and executes them with pytest. This approach illustrates how LLMs can assist Model Driven Test Engineering (MDTE) by automating test design and execution.

## Features
- Generate unit and integration test cases automatically from function names.
- Supports demo mode (local, fixed samples) and real mode (OpenAI GPT-4o-mini or similar).
- Writes generated tests to a dedicated folder to avoid conflicts.
- Runs tests with pytest and reports results.
- Simple Flask web UI for input and real-time generation/execution feedback.

## Requirements
- Python 3.8+
- Packages listed in `requirements.txt` (e.g., `openai`, `pytest`, `flask`)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/llm-mdte-prototype.git
   cd llm-mdte-prototype
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Obtain an OpenAI API key from OpenAI.

4. Set your API key as an environment variable:

   On Linux/macOS:

   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

   On Windows (PowerShell):

   ```powershell
   setx OPENAI_API_KEY "your_api_key_here"
   ```

5. (Optional) Prepare your target Python module to test.

## Usage

### Command Line

Generate and run tests in real mode:

```bash
python run_real.py
```

### Web UI

Start the Flask app:

```bash
python app.py
```

Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).
Input your module name, functions, and select mode (demo or real), then generate and run tests interactively.


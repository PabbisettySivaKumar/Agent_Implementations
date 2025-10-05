import subprocess

def query_ollama(prompt: str, model: str = "wizard-math:7b"):
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output = result.stdout.decode("utf-8").strip() or "No Response from Ollama"
        return {"output": output}
    except Exception as e:
        return {"output": f"Ollama error: {e}"}

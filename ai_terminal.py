
from gc import get_referents
import os
import subprocess
import sys


def get_command(model: str, user_request: str) -> str:
	instruction = (
		"You are a helpful assistant. Output ONLY a single Windows PowerShell command on one line. "
		"No explanations, no code fences, no quotes, no comments."
	)
	prompt = f"System:\n{instruction}\n\nUser:\n{user_request}\n\nAssistant:"

	proc = subprocess.run(
		["ollama", "run", model, prompt],
		capture_output=True,
		text=True,
		check=False,
		encoding="utf-8",
		errors="replace",
	)
	output = (proc.stdout or "").strip()
	# Take first non-empty line
	for line in output.splitlines():
		cmd = line.strip()
		if not cmd:
			continue
		# Strip common wrappers
		if cmd.startswith("PS "):
			cmd = cmd[3:].strip()
		cmd = cmd.strip('`')
		cmd = cmd.replace("```", "").strip()
		return cmd
	return ""


def run_powershell(command: str) -> int:
	if not command:
		print("No command produced.")
		return 1
	print("\nProposed command:")
	print(command)
	choice = input("Approve and run? [Enter]=yes / [e]dit / [n]o: ").strip().lower()
	if choice in ("e", "edit"):
		edited = input("Edit command: ").strip()
		if not edited:
			print("No command entered. Skipping.")
			return 0
		command = edited
	elif choice in ("", "y", "yes"):
		pass  # proceed
	else:
		print("Skipped.")
		return 0

	print("\nRunning...")
	# Force PowerShell to emit UTF-8 and capture output with UTF-8 decoding
	ps_prelude = (
		"[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; "
		"$OutputEncoding = [System.Text.UTF8Encoding]::new(); "
	)
	# Pipe combined stdout+stderr to Tee-Object to overwrite output.log each run
	wrapped = "& { " + command + " } 2>&1 | Tee-Object -FilePath 'output.log'"
	ps_command = ps_prelude + wrapped
	proc = subprocess.run(
		[
			"powershell",
			"-NoProfile",
			"-ExecutionPolicy",
			"Bypass",
			"-Command",
			ps_command,
		],
		capture_output=True,
		text=True,
		encoding="utf-8",
		errors="replace",
	)
	if proc.stdout:
		print(proc.stdout, end="")
	if proc.stderr:
		print(proc.stderr, file=sys.stderr, end="")
	return proc.returncode


def main() -> int:
	model = "deepseek-coder-v2:16b-lite-instruct-q4_K_M"
	print(f"AI Terminal (Ollama) — model: {model}")
	print("Type your request (or 'exit' to quit).")
	while True:
		try:
			print(f"\033[92m{os.getcwd()}\033[0m")
			user_req = input("\nRequest: ").strip()
		except (EOFError, KeyboardInterrupt):
			print()
			break
		if not user_req:
			continue
		if user_req.lower() == "exit":
			break

		cmd = get_command(model, user_req)
		code = run_powershell(cmd)
		if code != 0:
			print(f"Command exited with code {code}")

	print("Goodbye.")
	return 0


if __name__ == "__main__":
	sys.exit(main())

import subprocess
import time
import json
from typing import List, Optional, TypedDict


class Command(TypedDict):
    label: str
    compile: Optional[str]
    command: str
    cwd: str

class Config(TypedDict):
    num_runs: int
    commands: List[Command]


def execute_command(label, command, cwd=None, num_runs=5):
    times = []

    for _ in range(num_runs):
        start_time = time.time()
        try:
            result = subprocess.run(command, shell=True, cwd=cwd, text=True, capture_output=True)
            if result.returncode == 0:
                end_time = time.time()
                elapsed_time = end_time - start_time
                times.append(elapsed_time)
            else:
                print(f"Error '{command}':\n{result.stderr}")
        except Exception as e:
            print(f"Error '{command}': {e}")

    if times:
        avg_time = sum(times) / len(times)
        print(f"{label}: Avg time {avg_time:.6f} seconds.")
    else:
        print(f"{label}: Error.")

def compile(command, cwd=None):
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, text=True, capture_output=True)
    except Exception as e:
        print(f"Error '{command}': {e}")

def load_commands_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data


config: Config = load_commands_from_json('config.json')
commands = config['commands']
num_runs = config['num_runs']

for command in commands:
    if 'compile' in command:
        compile(command.get('compile'), cwd=command['cwd'])
    execute_command(command['label'], command['command'], cwd=command['cwd'], num_runs=num_runs)

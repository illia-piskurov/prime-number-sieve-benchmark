import subprocess
import os
import time

def run_command(command, cwd=None, label="Unknown", num_runs=5):
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

base_dir = "./"
cpp_dir = os.path.join(base_dir, "C++")
go_dir = os.path.join(base_dir, "Go")
csharp_dir = os.path.join(base_dir, "C#", "PrimeSieveApp")
java_dir = os.path.join(base_dir, "Java")
python_dir = os.path.join(base_dir, "Python")

compile("clang++ -o main.exe main.cpp -O3", cwd=cpp_dir)
compile("dotnet publish -c Release -r win-x64", cwd=csharp_dir)
compile("javac PrimeSieve.java", cwd=java_dir)

run_command("main.exe", cwd=cpp_dir, label="C++")
run_command("go run main.go", cwd=go_dir, label="Go")
run_command("dotnet run", cwd=csharp_dir, label="C# (Simple)")
run_command(".\\bin\\Release\\net8.0\\win-x64\\PrimeSieveApp.exe", cwd=csharp_dir, label="C# (NativeAOT)")
run_command("java PrimeSieve", cwd=java_dir, label="Java")
run_command("python main_numpy.py", cwd=python_dir, label="Python (Numpy)")
run_command("python main_simple.py", cwd=python_dir, label="Python (Simple)")

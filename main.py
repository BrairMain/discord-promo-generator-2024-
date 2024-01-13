import subprocess
import os

def run_script(script_path, output_file):
    # Check if the script exists and is executable
    if not os.path.isfile(script_path) or not os.access(script_path, os.X_OK):
        print(f"Error: The script {script_path} does not exist or is not executable.")
        return

    # Check if the output file is writable
    if os.path.isfile(output_file) and not os.access(output_file, os.W_OK):
        print(f"Error: The output file {output_file} is not writable.")
        return

    while True:
        result = subprocess.run(['C:\\Users\\goomb\\PycharmProjects\\pythonProject2\\venv\\Scripts\\python.exe', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Remove {"token":" at the beginning and "} at the end
        modified_result = result.stdout[10:-2]
        # Replace {"token":" at the beginning with the URL
        modified_result = 'https://discord.com/billing/partner-promotions/1180231712274387115/' + modified_result
        with open(output_file, 'a') as file:
            file.write(modified_result + '\n')
        print("Error (if any): ", result.stderr)

run_script('curlscript.py', 'outputdiscord.txt')
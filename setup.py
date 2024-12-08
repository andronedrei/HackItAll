import os
import subprocess
import sys

def create_virtual_environment(env_name="venv"):
    """Create a virtual environment."""
    print(f"Creating virtual environment: {env_name}...")
    subprocess.check_call([sys.executable, "-m", "venv", env_name])

def activate_virtual_environment(env_name="venv"):
    """Activate the virtual environment."""
    if os.name == 'nt':  # For Windows
        activate_script = os.path.join(env_name, "Scripts", "activate")
    else:  # For Unix/MacOS
        activate_script = os.path.join(env_name, "bin", "activate")
    return activate_script

def install_requirements(env_name="venv", requirements_file="requirements.txt"):
    """Install requirements from the requirements.txt file."""
    pip_path = os.path.join(env_name, "bin" if os.name != 'nt' else "Scripts", "pip")
    if not os.path.exists(requirements_file):
        print(f"{requirements_file} not found. Skipping installation.")
        return
    print(f"Installing dependencies from {requirements_file}...")
    subprocess.check_call([pip_path, "install", "-r", requirements_file])

if __name__ == "__main__":
    env_name = "venv"  # You can change this to your desired virtual environment name
    requirements_file = "requirements.txt"

    try:
        create_virtual_environment(env_name)
        activate_path = activate_virtual_environment(env_name)
        print(f"Virtual environment created. To activate it, run:\nsource {activate_path} (Unix/MacOS) or {activate_path}.bat (Windows)")
        install_requirements(env_name, requirements_file)
        print("Setup complete.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while setting up the environment: {e}")

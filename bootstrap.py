import venv
import subprocess

venv.create("uv_venv", with_pip=True)
subprocess.run(["uv_venv/Scripts/pip", "install", "uv"])
subprocess.run(["uv_venv/Scripts/uv", "sync", "-p", "3.12"])
subprocess.run([".venv/Scripts/jupyter-lab", "seads2024.ipynb"])

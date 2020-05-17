import subprocess
import os
def run_rad(cmd_rad, working_folder):
    if os.name == 'nt':
        process = subprocess.Popen('cmd', cwd = working_folder, shell = True, universal_newlines=True,stdin =subprocess.PIPE, stdout =subprocess.PIPE)
        out, err = process.communicate(cmd_rad)
    else:
        process = subprocess.Popen('bash', cwd = working_folder, shell = True, universal_newlines=True,stdin =subprocess.PIPE, stdout =subprocess.PIPE)
        out, err = process.communicate(cmd_rad)


import subprocess
import os
import honeybeeradiance.config as config

def run_rad(cmd_rad, working_folder):
    if os.name == 'nt':
        os.environ['RAYPATH'] += ';%s' % os.path.normpath(config.radlib_path)
        process = subprocess.Popen('cmd', cwd = working_folder, shell = True, universal_newlines=True,stdin =subprocess.PIPE, stdout =subprocess.PIPE)
        out, err = process.communicate(cmd_rad)
    else:
        process = subprocess.Popen('bash', cwd = working_folder, shell = True, universal_newlines=True,stdin =subprocess.PIPE, stdout =subprocess.PIPE)
        out, err = process.communicate(cmd_rad)


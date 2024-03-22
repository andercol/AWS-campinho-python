
# 128- [PF] -Lab - Administração do sistema com Python

import os
import subprocess

os.system("ls")

subprocess.run(["ls"])

subprocess.run(["ls", "-l"])

subprocess.run(["ls","-l","Lab01-06"])

print("\n ---------- recuperação de informações do sistema -----------\n")

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

print("\n ---------- recuperação de informações sobre o espaço em disco -----------\n")

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])



# pip install mcrcon

from mcrcon import MCRcon as r
with r('localhost', 'insertyourpasswordhere') as mcr:
    resp = mcr.command('/list')
print(resp) #there are 0/20 players online: - This will be different for you.

# -----------------------

# import subprocess, os

# def server_command(cmd):
#     process.stdin.write(cmd+"\n") #just write the command to the input stream

# process = None
# executable = '"C:\Program Files\Java\jre1.8.0_111\bin\java.exe" -Xms4G -Xmx4G -jar craftbukkit-1.10.2.jar nogui java'

# while True:
#     command=input()
#     command=command.lower()
#     if process is not None:
#         if command==("start"):
#             os.chdir(minecraft_dir)
#             process = subprocess.Popen(executable, stdin=subprocess.PIPE)
#             print("Server started.")
#     else:
#         server_command(command)

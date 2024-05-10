local_files = [
  # The route to Protein PDB file
  'files_PIK3CA/PIK3CA.pdb',
  # The route to Mutation List
  'files_PIK3CA/position.txt',
  # The route to Email List
  'files_PIK3CA/email.txt'
]


import paramiko
import os
import time

# Server Settings
hostname = 'Your Server IP'
port = 22
username = 'Your Username'
password = input("Please input your password: ")

# Your toute to APMA/data
remote_folder = '/route/to/APMA/data'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Upload Files
client.connect(hostname, port, username, password)
sftp = client.open_sftp()
for local_file in local_files:
    filename = os.path.basename(local_file)
    remote_path = os.path.join(remote_folder, filename)
    sftp.put(local_file, remote_path)
time.sleep(5)
sftp.close()

# Run APMA
remote_command = "nohup /home/wangjingran/.virtualenvs/DeepLearning/bin/python /home/wangjingran/APMA/Run.py > /home/wangjingran/APMA/run.log &"
stdin, stdout, stderr = client.exec_command(remote_command)
client.close()
print("Your files have submitted successfully\n...APMA is running now...")

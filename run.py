import os
import subprocess

# Change directory to the client folder
os.chdir("./client")

# Start npm run dev in the background
npm_process = subprocess.Popen(["npm", "run", "dev"])

# Change directory back to the server folder
os.chdir("../server")

# Run python app.py
os.system("python app.py")

# Optionally, wait for npm run dev to finish (if needed)
npm_process.wait()


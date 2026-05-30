import subprocess
import os

# Get the stored GitHub credentials
result = subprocess.run(['git', 'credential', 'fill'], 
                       input=b'protocol=https\nhost=github.com\n\n',
                       capture_output=True, text=True)

print("Credential output:", result.stdout)
print("Credential error:", result.stderr)

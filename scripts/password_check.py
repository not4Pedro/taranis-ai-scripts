import subprocess
from werkzeug.security import check_password_hash

cmd = [
    "docker", "compose", "exec", "database",
    "/bin/bash", "-c",
    'psql -U taranis -t -A -c "SELECT password FROM public.user WHERE username=\'admin\';"'
]

try:
    admin_hash_output = subprocess.check_output(cmd).decode('utf-8').strip()
except subprocess.CalledProcessError as e:
    print("Command failed with error:")
    print(e.stderr.decode() if e.stderr else e)
    raise

input_password = "admin"  

if check_password_hash(admin_hash_output, input_password):
    print("Password matches.")
else:
    print("Password does not match.")

print("Captured hash:", admin_hash_output)


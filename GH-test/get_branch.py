import subprocess

# Run the git command to get a list of branches
try:
    result = subprocess.check_output(["git", "branch"], stderr=subprocess.STDOUT, text=True)
    branches = result.split('\n')
except subprocess.CalledProcessError as e:
    print("Error:", e)
    branches = []

# Check if 'main' or 'master' branch exists
main_exists = any(branch.strip() == 'main' for branch in branches)
master_exists = any(branch.strip() == 'master' for branch in branches)

# Save the result in a variable
if main_exists:
    current_branch = 'main'
elif master_exists:
    current_branch = 'master'
else:
    current_branch = None

print("Current branch:", current_branch)

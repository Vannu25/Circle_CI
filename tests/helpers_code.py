import subprocess


def install_scripts():

    # PowerShell command to execute
    command = 'Get-Process'

    # Run PowerShell command and get the output
    process = subprocess.Popen(['powershell', '-Command', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Decode the output and error messages
    output = output.decode('utf-8')
    error = error.decode('utf-8')

    # Display the output and error messages
    print("Output:")
    print(output)
    print("Error:")
    print(error)


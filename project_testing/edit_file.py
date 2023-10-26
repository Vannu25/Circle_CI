import json
import os


def edit_file_lacework_vars(file_path, region, ami_name, instance_type):
    # Read the file content
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Edit the values
    for i in range(len(lines)):
        if lines[i].startswith('region='):
            lines[i] = f'region="{region}"\n'
        elif lines[i].startswith('ami_name='):
            lines[i] = f'ami_name="{ami_name}"\n'
        elif lines[i].startswith('instance_type='):
            lines[i] = f'instance_type="{instance_type}"\n'

    # Write the updated content to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

    print(f"File '{file_path}' has been edited and saved successfully.")


# Call the function to edit the file
edit_file_lacework_vars(file_path='C:\\packer\config-json\\lacework-vars.pkrvars.hcl',
                        region='us-west-2', ami_name='test-ami', instance_type='t2.large')

""" Editing the aws key and secret """


def edit_file_vars(file_path, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY):
    # Read the file content
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Edit the values
    for i in range(len(lines)):
        if lines[i].startswith('AWS_ACCESS_KEY_ID='):
            lines[i] = f'AWS_ACCESS_KEY_ID="{AWS_ACCESS_KEY_ID}"\n'
        elif lines[i].startswith('AWS_SECRET_ACCESS_KEY='):
            lines[i] = f'AWS_SECRET_ACCESS_KEY="{AWS_SECRET_ACCESS_KEY}"\n'

    # Write the updated content to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

    print(f"File '{file_path}' has been edited and saved successfully.")


key_id = os.environ.get(WINDOWS_CICD_KEYID_QA9)
secret_key = os.environ.get(WINDOWS_CICD_SECRET_QA9)

edit_file_vars(file_path="C:\\packer\\config-json\\variables.pkr.hcl",
               AWS_ACCESS_KEY_ID=key_id,
               AWS_SECRET_ACCESS_KEY=secret_key)

# Read the JSON file
""" Editing the config file with access token and server url"""

with open('C:\packer\config-json\config.json', 'r') as file:
    data = json.load(file)

# Modify the access token and server URL
access_token = os.environ.get(ACCESSTOKEN_QA9)
data['tokens']['accesstoken'] = access_token
data['serverurl'] = 'win-beta.qa9.corp.lacework.net'

# Write the updated data back to the JSON file
with open('C:\packer\config-json\config.json', 'w') as file:
    json.dump(data, file)

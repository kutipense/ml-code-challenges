import requests

user_token = "USER_TOKEN_HERE"

url = "https://www.deep-ml.com/submit"
headers = {
    "accept": "*/*",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-requested-with": "XMLHttpRequest",
    "cookie": f"user_token={user_token}",
}


import os

parent_folder = "problems"

g_success = True
for filename in os.listdir(parent_folder):
    if filename.endswith(".py"):
        problem_id = os.path.splitext(filename)[0]  # Get problem ID from the file name
        file_path = os.path.join(parent_folder, filename)
        with open(file_path, "r") as file:
            code = file.read().replace("\n", "%0A").replace(" ", "+")
            body = f"code={code}&problem_id={problem_id}"

        response = requests.post(url, headers=headers, data=body).json()
        success = all(i["passed"] for i in response["results"])
        g_success = success and success
        status = "✅" if success else "❌"
        print(f"Problem {int(problem_id):02d}: {status}")

# Print nicely formatted emoji text about each problem
if g_success:
    print("✅ All problems passed")

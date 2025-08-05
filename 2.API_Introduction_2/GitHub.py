import requests

print("GitHub user information:")
username= "Faezehazadi"
url = f"https://api.github.com/users/Faezehazadi"
response = requests.get(url)
data = response.json()
print("UserName: ", username)
print("Followers: ", data.get("followers"))
print("Following: ", data.get("following"))
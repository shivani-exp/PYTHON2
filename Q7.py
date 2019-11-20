import re

email = "shivani@datagrokr.com  sam@company.com "
pattern = "\w+@(\w+).com"
ans = re.findall(pattern , email)
print(ans)

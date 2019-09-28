import sys
#username = raw_input("Please enter a Github username: ")
#password = raw_input("Please enter the account password: ")
username ="diruhjhjhnit"
password="dabg" 
gh = Github(login="username" , password ="passwrd" )
get_user = gh.users.get()
user_repos = gh.repos.list().all()
count =0
for repo in user_repos:
    count=count+1
    print repo.language
print("number of repois:"+str(count))

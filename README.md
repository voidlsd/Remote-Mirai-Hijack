<p align=center>
  <img width="30%" src="https://image.flaticon.com/icons/png/512/2808/2808265.png">
</p>

# Remote Mirai Hijack
Remote Mirai Hijack was made to hijack mirais using a vulnerability that is often overlooked by DDoS script kiddies.

#### How did you find the vulnerability?
After looking through multiple mirai variants, I have found that most of the tables are always 'users' and that the instructions to compile the mirai is always the same as "root" and "root" for the SQL username and password, which most DDoS script kiddies overlook as nothing, so they never have changed the SQL username or password. I also noticed most of the DDoS script kiddies don't know that you can remotely connect to the SQL server they are hosting it on.

#### How does the exploit work?
The "vulnerability" exploits an attack vector commonly found in IOT devices (The Mirai Target), default credentials. The exploit tests a list of credentials on the SQL server powering the Mirai authentication and when successful, inserts a new user account into the database. This script can be easily modified to also dump the usernames and password of all users in the database.

## Install
```
1. Clone repository, Then CD into the directory.
2. $ pip install -r requirements.txt
3. python3 main.py
```

## Legal
Though you are attacking malware, this is likely still illegal in your area as you are accessing a system without permission of the owner. Please do not use this outside of lab/testing environments.

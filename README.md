# Remote Mirai Hijack
Remote Mirai Hijack was made to hijack mirais using a vulnerability that is often overlooked by DDoS script kiddies.

# How did you find the vulnerability?
After looking through multiply mirai variants, I have found that most of the tables are always 'users' and that the instructions to compile the mirai is always the same as "root" and "root" for the SQL username and password, which most DDoS script kiddies overlook as nothing, so they never have changed the SQL username or password. I also noticed most of the DDoS script kiddies don't know that you can remotely connect to the SQL server they are hosting it on.

# How does the exploit work?
From the vulnerability, I wrote this script that goes into the "users" tables and then inserts the username and password you provided in the script.

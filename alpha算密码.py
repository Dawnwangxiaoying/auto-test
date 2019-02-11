import hashlib

salt = 'aWNvdXJ0LWFscGhh'

pwd = '123456'
user = "xiaoying@123.com"

hash = hashlib.sha1(str(user+salt).encode("utf-8"))
hash.update(str(pwd).encode("utf-8"))
z = str(hash.hexdigest())

hash = hashlib.sha1(str(z+salt).encode("utf-8"))
hash.update(str(z).encode("utf-8"))
z = str(hash.hexdigest())

print("UPDATE `user` SET `PASSWORD`='" + z +"' WHERE email='" + user + "';")



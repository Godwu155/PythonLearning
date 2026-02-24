import bcrypt



# 1. 模拟用户注册时的密码
password = "my_super_secret_password".encode('utf-8')

# 2. 生成哈希（内部包含随机盐和计算强度）
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(f"存储到数据库的哈希值: {hashed.decode()}")

# 3. 验证密码
user_input = "my_super_secret_password".encode('utf-8')
if bcrypt.checkpw(user_input, hashed):
    print("登录成功！")
else:
    print("密码错误。")
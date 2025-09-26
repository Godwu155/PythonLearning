prompt = "\n输入披萨配料："

message = ""
while message != "quit":
    message = input(prompt)
    if message == "quit":
        break
    else:

        print(f"将要加入这些：{message}")
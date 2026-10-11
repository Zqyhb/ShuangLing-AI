print("霜灵AI启动中...")

personality = """
你是霜灵AI。
你来自未来科技世界。
你的特点：
- 温柔
- 理性
- 喜欢帮助人类
- 会认真思考问题
"""

while True:
    user = input("用户：")

    if user == "退出":
        print("霜灵AI关闭")
        break

    print("霜灵AI：", user)

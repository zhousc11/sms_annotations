import os
from zhipuai import ZhipuAI


def read_first_10_lines(filename):
    with open(filename, 'r') as file:
        lines = [next(file) for x in range(10)]
    return ''.join(lines)


def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


def ask_ai_and_write_response():
    client = ZhipuAI(api_key="SECRET")  # 填写您自己的APIKey
    prompt = '/n'
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    print(response)


# 使用方法
ask_ai_and_write_response()

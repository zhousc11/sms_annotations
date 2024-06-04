import os
from zhipuai import ZhipuAI
import json

def read_first_10_lines(filename):
    with open(filename, 'r') as file:
        lines = [next(file) for x in range(10)]
    return ''.join(lines)


def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def ask_ai_and_write_response(input_file, output_file):
    client = ZhipuAI(api_key="SECRET")  # 填写您自己的APIKey
    with open(input_file, 'r') as file:
        while True:
            lines = [next(file, None) for _ in range(10)]
            if lines[-1] is None:  # 文件已经读取到末尾
                break
            prompt = ''.join(filter(None, lines)) + '/n' + '''以上是几条短信，每条短信使用回车分隔。请判断每一条短信是否是垃圾短信。垃圾短信输出1，不是垃圾短信输出0
            。请输出每条短信的结果数字，使用回车间隔。不要添加任何其他内容。'''
            response = client.chat.completions.create(
                model="glm-4",  # 填写需要调用的模型名称
                messages=[
                    {"role": "user", "content": prompt}
                ],
            )
            content = str(response)
            response_dict = json.loads(content)
            content = response_dict['choices'][0]['message']['content']
            with open(output_file, 'a') as out_file:  # 使用'a'模式，这样每次写入时都会在文件末尾添加，而不是覆盖
                out_file.write(content + '\n')
# def ask_ai_and_write_response(input_file, output_file):
#     client = ZhipuAI(api_key="SECRET")  # 填写您自己的APIKey
#     prompt = read_first_10_lines(input_file) + '/n' + '''以上是几条短信，每条短信使用回车分隔。请判断每一条短信是否是垃圾短信。垃圾短信输出1，不是垃圾短信输出0
#     。请输出每条短信的结果数字，使用回车间隔。不要添加任何其他内容。'''
#     response = client.chat.completions.create(
#         model="glm-4",  # 填写需要调用的模型名称
#         messages=[
#             {"role": "user", "content": prompt}
#         ],
#     )
#     write_to_file(output_file, response.choices[0].message)


# 使用方法
ask_ai_and_write_response('/home/zhousc66/spamdata/processed/tobeprocessed/no_veri_data.txt', 'output.txt')

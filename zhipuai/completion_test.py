import logging
import threading
import queue
import time
from zhipuai import ZhipuAI
import re


def request_api(line) -> str:
    client = ZhipuAI(api_key='')
    # prompt = line + '\n' + '这是一条垃圾短信吗？是的话请输出1，不是的话请输出0.如果你并不能判断，请输出0.你的回答只能是一个数字1或0，谢谢！'
    prompt =line
    message_list = [
        {
            'role': 'user', 'content': prompt
        }
    ]
    response = client.chat.completions.create(
        model='glm-4',
        messages=message_list
    )
    # print(response)
    response_str = str(response)
    print(response_str)
    pattern = r"content='(.*?)'"
    content_regex = re.search(pattern, response_str)
    # content = content_regex.group(1)
    return content_regex.group(1)
    # print(content)
    # if content is not None:
    #     content = content.group(1)
    # else:
    #     print(content)
    # if content:
    #     if content.isdigit():
    #         # logging.info('Got content: %s', content)
    #         return str(content)
    #     else:
    #         logging.warning('Invalid response: %s', response_str)
    #         further_dicts = [
    #             {
    #                 'role': 'assistant', 'content': content
    #             },
    #             {
    #                 'role': 'user', 'content': '请只输出0或1，谢谢'
    #             }
    #         ]
    #         message_list.extend(further_dicts)
    #         response = client.chat.completions.create(
    #             model='glm-4',
    #             messages=message_list
    #         )
    #         response = str(response)
    #         content = re.search(r"'content='(.*?)'", response)
    #         content = content.group(1)
    #         if content.isdigit():
    #             logging.info('Got content: %s', content)
    #             return str(content)
    #         else:
    #             logging.warning('Invalid response: %s', response)
    #             return '0'
    #
    # else:
    #     logging.warning('Empty response: %s', response_str)
    #     return '0'


def process_line(line_number, step, output_queue):
    filename = "/home/zhousc66/threadtest.txt"  # 输入文件名
    with open(filename, 'r') as file:
        lines = file.readlines()

    while line_number < len(lines):
        line = lines[line_number].strip()
        result = request_api(line)
        output_queue.put((line_number, result))
        line_number += step


def write_results(output_queue, total_lines):
    expected_line = 0
    results = {}

    while expected_line < total_lines:
        if expected_line in results:
            with open("output.txt", "a") as file:
                file.write(results.pop(expected_line) + '\n')
            expected_line += 1
        else:
            line_number, result = output_queue.get()
            if line_number == expected_line:
                with open("output.txt", "a") as file:
                    file.write(result + '\n')
                expected_line += 1
            else:
                results[line_number] = result


def main():
    threads = []
    num_threads = 5  # 最大并发数
    output_queue = queue.Queue()

    # 确定文件中的总行数
    with open("/home/zhousc66/threadtest.txt", 'r') as file:
        lines = file.readlines()
    total_lines = len(lines)

    # 启动线程
    for i in range(num_threads):
        thread = threading.Thread(target=process_line, args=(i, num_threads, output_queue))
        threads.append(thread)
        thread.start()

    # 启动结果写入线程
    writer_thread = threading.Thread(target=write_results, args=(output_queue, total_lines))
    writer_thread.start()

    # 等待所有处理线程完成
    for thread in threads:
        thread.join()

    # 确保结果写入完成
    writer_thread.join()


if __name__ == "__main__":
    main()

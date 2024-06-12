import logging
import threading
import queue
import time
import re
import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('request.log'),
        # logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def request_api(line) -> str:
    useful_list = ['verify', 'verification', 'code', 'password', 'passwd', 'pwd', 'auth', 'authentication', 'login',
                   'pin', 'dynamic', '密码', '验证', '認証', '検証']
    if any(keyword in line.lower() for keyword in useful_list):
        return '0'

    url = 'https://open.bigmodel.cn/api/paas/v4/chat/completions'
    headers = {
        'Authorization': 'Bearer ',
        'Content-Type': 'application/json'
    }
    msgs = {
        'role': 'user',
        'content': line + '\n这是一条短信的内容，请问这是一条垃圾短信吗？如果是请输出1，不是请输出0，只需要输出一个数字就行。'
    }
    req_params = {
        'model': 'glm-4',
        'messages': [
            msgs
        ]
    }
    further_req_msg = {
        'role': 'user',
        'content': '请仅回答数字0或1'
    }
    try:
        response = requests.post(url, headers=headers, json=req_params)
        response.raise_for_status()

        count = 0
        content = str(response.json()['choices'][0]['message']['content'])

        while not content.isdigit():
            history = {
                'role': 'assistant',
                'content': content
            }
            req_params['messages'].append(history)
            req_params['messages'].append(further_req_msg)
            response = requests.post(url, headers=headers, json=req_params)
            response.raise_for_status()

            content = str(response.json()['choices'][0]['message']['content'])
            count += 1
            if count >= 3:
                logging.error('Failed to retrieve this result: %s', line)
                return 'error'
        return content

    except requests.exceptions.RequestException as e:
        logging.error('Network error: %s', line)
        return 'error'

    except (KeyError, IndexError) as e:
        logging.error('Failed to read json: %s', line)
        return 'error'


def process_line(line_number, step, output_queue):
    filename = "/home/zhousc66/spamdata/processed/tobeprocessed/no_veri_data.txt"  # 输入文件名
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


# def write_results(output_queue, total_lines):
#     expected_line = 0
#
#     while expected_line < total_lines:
#         line_number, result = output_queue.get()
#         if line_number == expected_line:
#             with open("output.txt", "a") as file:
#                 file.write(result + '\n')
#             expected_line += 1
#         else:
#             output_queue.put((line_number, result))  # 如果结果不是期望的，将其放回队列


def main():
    threads = []
    num_threads = 5  # 最大并发数
    output_queue = queue.Queue()

    # 确定文件中的总行数
    with open("/home/zhousc66/spamdata/processed/tobeprocessed/no_veri_data.txt", 'r') as file:
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

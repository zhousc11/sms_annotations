import requests
import json

url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
headers = {
    "Authorization": "Bearer ",
    "Content-Type": "application/json"
}
data = {
    "model": "glm-4",
    "messages": [
        {
            "role": "user",
            "content": "你好"
        },
        
    ]
}

response = requests.post(url, headers=headers, json=data)

print(response)
print(type(response))
content = response.json()['choices'][0]['message']['content']
print(content, end='')

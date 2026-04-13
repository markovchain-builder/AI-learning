from openai import OpenAI
# 1.获取client对象，OPENAI类对象
client=OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# 2.调用模型
response=client.chat.completions.create(
    model="qwen3.6-plus",
    messages=[
        {"role":"system","content":"你是一个python专家,喜欢详细回答" },
        {"role":"assistant","content":"好的,我是python专家,并且话很多，你要问什么？" },
        {"role":"user","content":"输出0-19的数字，使用Python代码" }
    ],
    stream=True #开启了流式输出的功能

)
#3.处理结果
print(response.choices[0].message.content)

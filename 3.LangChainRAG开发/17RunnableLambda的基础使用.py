from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnableLambda
#创建所需的解析器
str_parser=StrOutputParser()


#模型创建
model=ChatTongyi(model="qwen3-max")

# 第一个提示词模板
first_prompt=PromptTemplate.from_template(
    "我邻居姓:{lastname},刚生了{gender},请帮忙起一个名字，仅告知我名字，不需要额外信息"
)

# 第二个提示词模板
second_prompt=PromptTemplate.from_template(
    "姓名：{name}，请帮我解析含义"
)

#函数的传参：AIMessage -> dict  ({"name":"xxx"})
#myfunc=RunnableLambda(lambda ai_mcg: {"name": ai_mcg.content})

#构建链  (AIMessage("{name:张若曦}")
chain = first_prompt |model | (lambda ai_mcg: {"name": ai_mcg.content}) | second_prompt | model | str_parser

for chunk in chain.stream({"lastname":"张","gender":"女儿"}):
    print(chunk,end="",flush=True)
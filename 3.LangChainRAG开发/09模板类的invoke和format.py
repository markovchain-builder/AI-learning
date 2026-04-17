from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate

"""
PromptTemplate -> StringPromptTemplate -> BasePromptTemplate -> RunnableSerializable -> Runnable
FewShotPromptTemplate -> StringPromptTemplate -> BasePromptTemplate -> RunnableSerializable -> Runnable
ChatShotPromptTemplate -> BaseChatPromptTemplate -> BasePromptTemplate -> RunnableSerializable -> Runnable
"""
template=PromptTemplate.from_template("我的邻居是{lastname},最喜欢的是{hobby}")
res=template.format(lastname="张大妈",hobby="钓鱼")
print(res,type(res))

res2=template.invoke({"lastname":"ming","hobby":"打球"})
print(res2,type(res2))
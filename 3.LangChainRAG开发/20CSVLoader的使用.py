from langchain_community.document_loaders import CSVLoader


loader=CSVLoader(
    file_path="data\stu.csv",
    encoding="utf-8"             # 指定编码为UTF-8
)
# 批量加载 .load() -> [DOcument,Document,...]
documents=loader.load()

for document in documents:
    print(document,type(document))

# 懒加载  .lazy_load()  迭代器[Document]
for document in loader.lazy_load():
    print(document)
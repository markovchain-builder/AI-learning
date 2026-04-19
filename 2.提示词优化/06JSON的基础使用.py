import json
d={
    "name":"周杰伦",
    "age":11,
    "gender":"男"
}
s=json.dumps(d,ensure_ascii=False)
print(s,type(s))
l=[
    {
    "name":"周杰伦",
    "age":11,
    "gender":"男"
},
    {
    "name":"kkk",
    "age":12,
    "gender":"女"

}
]
print(json.dumps(l,ensure_ascii=False))
json_str='{"name": "周杰伦", "age": 11, "gender": "男"}'
json_array_str='[{"name": "周杰伦", "age": 11, "gender": "男"}, {"name": "kkk", "age": 12, "gender": "女"}]'
res_dict=json.loads(json_str)
print(json_str,type(res_dict))
res_list=json.loads(json_array_str)
print(json_array_str,type(res_list))

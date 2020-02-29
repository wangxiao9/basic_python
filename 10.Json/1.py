'''
1. Json
 - 轻量级的数据交换格式
 - {"key":"value"}
'''
import json

# 反序列化 ： 把json字符串转换成python字典

json_str = '{"name":"wangxiao", "age":"18"}'


new_json = json.loads(json_str)

print(type(new_json))
print(new_json)
print(new_json['name'])


# 序列化 ：把字典转换成字符串

dict_json = {'address':'江苏', 'number':'100'}

new_json_str = json.dumps(dict_json)

print(type(new_json_str))
print(new_json_str)
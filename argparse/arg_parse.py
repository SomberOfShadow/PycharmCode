import argparse

# 创建命令行解析器句柄，并自定义描述信息
parser = argparse.ArgumentParser(description='test the argparse package')
# 定义必选参数 positionArg
parser.add_argument('positionArg')
# 定义可选参数verbosity1
parser.add_argument('--verbosity1', '-v1', help='test the optional arguments')

# 定义可选参数verbosity2，并通过设定store_true表示该选项不需要接收参数，若不设action，则默认是需要接收参数的，否则报错
parser.add_argument('--verbosity2', '-v2', action='store_true', help='test the action arg')
# 指定参数类型（默认是 str）
parser.add_argument('x', type=int, help='test the type')

# 设置参数的可选范围
parser.add_argument('--verbosity3', '-v3', type=str, choices=['one', 'two', 'three', 'four'], help='test choices')
# 设置参数默认值
parser.add_argument('--verbosity4', '-v4', type=str, choices=['one', 'two', 'three'], default=1,
                    help='test default value')

parser.add_argument('--threshold_reply', default=100, type=int)
parser.add_argument('--threshold_topic', default=20, type=int)
parser.add_argument('--threshold_solved', default=20, type=int)

args = parser.parse_args()  # 返回一个命名空间

# print(args)
params = vars(args)  # 返回 args 的属性和属性值的字典
for k, v in params.items():
    print(k, v)

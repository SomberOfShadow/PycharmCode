import sys
import argparse


# 创建命令行解析器句柄，并自定义描述信息
parser = argparse.ArgumentParser(description='The script is to transfer log4j.property to log4j2.xml')
# 定义必选参数 positionArg
parser.add_argument('--old_name', '-p', required=True, help='log4j.property path')
parser.add_argument('--new_name', '-x', required=True, help='log4j2.xml path')

# 返回一个命名空间
args = parser.parse_args()

properties_path = args.old_name

template_name = args.new_name


# 先建立一个模板， 然后插入或者按边读取边建立

# properties_path = sys.argv[1]
# template_name = sys.argv[2]
content = []
level = ""
ref_name = ""

SYSTEM_OUT = "SYSTEM_OUT"
follow = ""
pattern = ""

logger_level_list = []
logger_name_list = []

# print("Start reading " + properties_path + " content：")
with open(properties_path, 'r', encoding="utf-8") as fr:
    # 按行读取放到一个列表里面
    content = fr.readlines()
    fr.close()
# print("Reading " + properties_path + " content finished.")
# print("Start transfering " + properties_path + " to " + template_name + ".")
for line in content:
    if line.startswith("log4j.rootLogger"):
        level = line.split("=")[1].split(",")[0]
        # print("level", level)
        ref_name = line.split("=")[1].split(",")[1].strip().replace("\n", "")
        # print("ref_name", ref_name)
    elif line.startswith("log4j.appender." + ref_name + ".layout.ConversionPattern"):
        pattern = line.split("=")[1].strip().replace("\n", "")
        # print("pattern:", pattern)
    elif line.startswith("log4j.logger"):
        logger_level = line.split("=")[1].strip().replace("\n", "")
        logger_level_list.append(logger_level)
        # print("logger_level:", logger_level)
        logger_name = line.split("=")[0][13:].strip().replace("\n", "")
        logger_name_list.append(logger_name)
        # print("logger_name:", logger_name)
    elif "follow" in line and line.startswith("log4j"):
        follow = line.split("=")[1].strip().replace("\n", "")

with open(template_name, 'w', encoding="utf-8") as fw:

    # 头部
    fw.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    fw.write('<Configuration status="WARN">\n')

    # Appenders
    if follow.strip() == '':
        fw.write('    <Appenders>\n')
        fw.write("        <Console name=" + "\"" + ref_name + "\"" + " target=" + "\"" + SYSTEM_OUT + "\"" + ">\n")
        fw.write("            <PatternLayout pattern=" + "\"" + pattern + "\"" + "/> \n")
        fw.write("        </Console>\n")
        fw.write("    </Appenders>\n")
    else:
        fw.write('    <Appenders>\n')
        fw.write(
            "        <Console name=" + "\"" + ref_name + "\"" + " target=" + "\"" + SYSTEM_OUT + "\"" + " follow=" +
            "\"" + follow + "\"" + ">\n")
        fw.write("            <PatternLayout pattern=" + "\"" + pattern + "\"" + "/> \n")
        fw.write("        </Console>\n")
        fw.write("    </Appenders>\n")

    # Loggers
    fw.write('    <Loggers>\n')
    fw.write("        <Root level=" + "\"" + level + "\"" + ">\n")
    fw.write("            <AppenderRef ref=" + "\"" + ref_name + "\"" + "/>\n")
    fw.write('        </Root>\n')
    length = len(logger_level_list)
    for i in range(length):
        logger_name = logger_name_list[i]
        logger_level = logger_level_list[i]
        fw.write("		<logger name=" + "\"" + logger_name + "\"" + " level=" + "\"" + logger_level + "\"" +"> </logger>\n")
    fw.write('    </Loggers>\n')

    # 尾部
    fw.write("</Configuration>\n")
    fw.close()

# print("Transfering " + properties_path + " to " + template_name + " finished!")
print("Transfer " + properties_path + " to " + template_name + " success!")


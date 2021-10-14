import sys

# 先建立一个模板， 然后插入或者按边读取边建立

# properties_path = sys.argv[1]
properties_path = "C:\MyDocuments\MJE\Log4jToLog4j2\log4j.properties"

# properties_path = "C:\MySoftWare\PycharmTest\\transfer_log4j1_to_log4j2\\log4j_test.properties"
template_name = "test_result.xml"
# template_name = sys.argv[2]
content = []
level = ""
ref_name = ""

SYSTEM_OUT = "SYSTEM_OUT"
follow = ""
pattern = ""

logger_level_list = []
logger_name_list = []

with open(properties_path, 'r', encoding="utf-8") as fr:
    # 按行读取放到一个列表里面
    content = fr.readlines()
    fr.close()
    # print("content:", content)

for line in content:
    if line.startswith("log4j.rootLogger"):
        level = line.split("=")[1].split(",")[0]
        print("level", level)
        ref_name = line.split("=")[1].split(",")[1].strip().replace("\n", "")
        print("ref_name", ref_name)
    elif line.startswith("log4j.appender." + ref_name + ".layout.ConversionPattern"):
        pattern = line.split("=")[1].strip().replace("\n", "")
        print("pattern:", pattern)
    elif line.startswith("log4j.logger"):
        logger_level = line.split("=")[1].strip().replace("\n", "")
        logger_level_list.append(logger_level)
        print("logger_level:", logger_level)
        logger_name = line.split("=")[0][13:].strip().replace("\n", "")
        logger_name_list.append(logger_name)
        print("logger_name:", logger_name)
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



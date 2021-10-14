"""
测试os.path.join()
"""
import os

base_dir = "/repo/gratci/workspace/executor/1/common-grat"
baseline_dir = os.path.join(base_dir + "/", "BUILD/IF/")
print(base_dir)
print(baseline_dir)
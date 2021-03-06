import matplotlib.pyplot as plt

name_list = ['lambda=0', 'lambda=0.05', 'lambda=0.1', 'lambda=0.5']
num_list = [52.4, 57.8, 59.1, 54.6]
rects = plt.bar(range(len(num_list)), num_list, color='rgby')
# X轴标题
index = [0, 1, 2, 3]
index = [float(c) + 0.4 for c in index]
plt.ylim(ymax=80, ymin=0)
plt.xticks(index, name_list)
plt.ylabel("arrucay(%)")  # X轴标签
# for rect in rects:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width() / 2, height, str(height) + '%', ha='center', va='bottom')
plt.show()
import tkinter as tk
import subprocess

# 创建窗口，并设置其大小
root = tk.Tk()
root.title("Choose file to run")
root.geometry("300x150")

# 创建按钮1
button1 = tk.Button(root, text="Run file1.py", command=lambda: run_file("file1.py"))
button1.pack()

# 创建按钮2
button2 = tk.Button(root, text="Run file2.py", command=lambda: run_file("file2.py"))
button2.pack()

# 运行所选文件的函数
def run_file(file):
    cmd = ["python", file]
    output = subprocess.check_output(cmd, universal_newlines=True)
    print(output)

# 进入事件循环
root.mainloop()

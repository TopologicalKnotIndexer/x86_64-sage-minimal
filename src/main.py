# 从标准输入读入一些 sage 的 python 脚本
# 执行，并将 exit_code, 标准输出流，标准错误流的内容输出到屏幕

import sys
from sage_run import sage_run # 运行 sage 中的 python 脚本

def main():
    input_code = sys.stdin.read()
    print(sage_run(input_code))

if __name__ == "__main__":
    main()
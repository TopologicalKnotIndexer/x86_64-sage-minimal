# x86_64-sage-minimal
假设有可用的 sage，在 sage 上执行 python 程序。
- 请自行安装 sage： https://github.com/sagemath/sage



## 前置条件
- `sage>=10.3`
- `python3`



## 运行方式

- `python3 ./src/main.py`
  - 向标准输入中输入一段代码，表示 sage 下的 python 脚本
  - 程序会将 sage 的返回值、标准输出流、标准错误流，输出到程序自身的标准输出流


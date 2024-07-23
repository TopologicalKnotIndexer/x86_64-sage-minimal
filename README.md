# x86_64-sage-minimal
试图封装一个 x86_64 下 sagemath 的二进制版本。
- 本项目并不涉及对 sagemath 源代码的编辑和重分发，仅包含 x86_64 下 sage 的部分二进制，sagemath 的开源协议请参考 https://github.com/sagemath/sage



## 前置条件

- 系统架构必须为 `x86_64`
- `python3`



## 运行方式

- `python3 ./src/main.py`
  - 向标准输入中输入一段代码，表示 sage 下的 python 脚本
  - 程序会将 sage 的返回值、标准输出流、标准错误流，输出到程序自身的标准输出流


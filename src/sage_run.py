# 给出一段 python 代码，要求 sage 执行并获取其执行结果
import os
import tempfile
import subprocess
DIRNOW    = os.path.dirname(os.path.abspath(__file__))
SAGE_PATH = os.path.join(DIRNOW, "bin", "sage")
assert os.path.isfile(SAGE_PATH)

def get_temp_dir_prefix(): # 获取进程、时间、相关的文件名前缀
    return "tmp_sage_run_%07d_" % (os.getpid())

def get_temp_file_path(): # 获取临时文件的文件名
    return tempfile.mktemp("", get_temp_dir_prefix())

# 将一段 python 代码喂给 sage 执行
# 并获取其【exit_code，标准输出，标准错误】
def sage_run(python_code:str) -> tuple[int, str, str]:
    tmp_file = get_temp_file_path()                          # 创建临时文件
    open(tmp_file, "w", encoding="utf-8").write(python_code) # 代码写入临时文件
    ans = (None, "", "")                                     # 当前进程发生异常时，exit_code==None
    try:
        result = subprocess.run([SAGE_PATH, "-python", tmp_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_ans = result.stdout.decode("utf-8") # 获取标准输出
        stdout_err = result.stderr.decode("utf-8") # 获取标准错误
        ret_value  = result.returncode             # 获取返回值
        ans = (ret_value, stdout_ans, stdout_err)
    finally:
        os.remove(tmp_file) # 删除临时文件
    return ans

# sagemath 示例代码
SAMPLE_CODE = """
from sage.all import *
K = Knot([[2, 8, 3, 7], [4, 10, 5, 9], [6, 2, 7, 1], [8, 4, 9, 3], [10, 6, 1, 5]]) # k5a1
K3a1 = Knot([[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]])
if str(K3a1.homfly_polynomial()).strip() == "L^-2*M^2 - 2*L^-2 - L^-4":
    K = K.mirror_image()
print(K.homfly_polynomial())
print(K.connected_sum(K).pd_code())
"""

if __name__ == "__main__":
    print(sage_run(SAMPLE_CODE)) # 运行测试代码
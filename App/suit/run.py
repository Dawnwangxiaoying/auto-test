import pytest,os

rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
loginPath=os.path.join(rootPath, "test_case")
taskPath=os.path.join(rootPath, "test_case")

reportPath=os.path.join(rootPath, "report")
# print(casePath)
if __name__ == '__main__':
    #-s为了显示用例的打印信息 -q只显示结果不显示过程
    pytest.main([loginPath,'-s','-q','--alluredir', reportPath])  # 指定测试目录

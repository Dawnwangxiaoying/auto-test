import unittest,time,os,sys
from  case import test_interface
from HTMLTestRunner import HTMLTestRunner
if __name__ == "__main__":
    # 切换到当前脚本的上级目录
    rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(rootPath)
    # # 切换到根目录
    # rootPath = os.path.abspath(os.path.join(first_dir, ".."))
    # 将项目目录添加到sys.path
    sys.path.append(rootPath)
    # 切换到当前脚本的上级目录
    test_dir=rootPath+"/case"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*')

    # 将localtime()返回的时间转换为由格式指定的字符串参数
    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    # 设置生成结果的文件名
    cases_data_name = '/' + now + '_result.html'
    # 设置结果文件的绝对路径
    filename = rootPath + cases_data_name
    # open:打开file并返回一个相应的文件对象.如果文件不能被打开, 抛出 OSError 异常.

    fp = open(filename, 'wb')
    # 设置html结果的标题、描述、写入的文件

    runner = HTMLTestRunner(stream=fp,
                            title='Blue Ocean Interface Test Report',
                            description='Implementation Example with: ')

    # 运行匹配的脚本
    runner.run(discover)

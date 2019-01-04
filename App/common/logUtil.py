import logging, os, time


class logUtil:
    def __init__(self, logger_name="Debug"):
        logger = logging.getLogger(logger_name)
        # 设置该logger的级别（等于／高于该级别的logger都显示）
        logger.setLevel(logging.DEBUG)
        # 注：level需在logger、Handler同时进行设置
        # 检查此记录器是否已配置任何处理程序
        if not logger.hasHandlers():
            # 返回StreamHandler类的新实例，StreamHandler:log信息输出到终端
            console = logging.StreamHandler()
            # 设置日志级别
            console.setLevel(logging.INFO)
            fmt = logging.Formatter(fmt='%(asctime)s [%(levelname)s]::%(name)s: %(message)s',
                                    datefmt='%Y-%m-%d %H:%M:%S')
            console.setFormatter(fmt)
            # 将指定的handlerhdlr添加到logger中。
            logger.addHandler(console)
        self.logger = logger

    def debug(self, *args):
        # 在logger上记录一条级别为DEBUG的消息
        self.logger.debug(args)

    def info(self, msg):
        # 在logger上记录一条级别为info的消息
        self.logger.info(msg)

    def warning(self, msg):
        # 在logger上记录一条级别为warning的消息
        self.logger.warning(msg)

    def error(self, msg):
        # 在logger上记录一条级别为error的消息
        self.logger.error(msg)

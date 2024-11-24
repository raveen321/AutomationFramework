import logging

class LogGen:
    @staticmethod
    def logGen():
        # logging.basicConfig(filename=".\\Logs\\error4.log")
        logging.basicConfig(
            filename=".\\Logs\\error5.log",
            level=logging.INFO,
            format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
            datefmt='%H:%M:%S',
            force = True
        )



        logger=logging.getLogger()
        # logger.setLevel(logging.INFO)
        return logger

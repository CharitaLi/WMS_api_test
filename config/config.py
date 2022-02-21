import logging

logger = logging.getLogger()
fh = logging.FileHandler("test.log",encoding="utf-8",mode="a")
formatter = logging.Formatter("%(asctime)s - %(name)s-%(levelname)s %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)
logger.info("hello")


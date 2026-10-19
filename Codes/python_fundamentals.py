from loguru import logger
tup = 1,12
logger.info(type(tup))
tup2 = tup+ ("a","b")
logger.info(tup2)

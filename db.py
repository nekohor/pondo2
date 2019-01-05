from sqlalchemy import create_engine
import pymysql


class DB():

    def __init__(self, line):
        self.engine = create_engine(
            'mysql+pymysql://root:@localhost:3306/coil_{}?charset=utf8mb4'
            .format(line))

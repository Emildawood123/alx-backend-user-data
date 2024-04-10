#!/usr/bin/env python3
"""filter_datum for hide the sen.. data"""
from typing import List
import re
import logging
import os
import mysql.connector

PII_FIELDS: List[str] = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """filter_datum"""
    for field in fields:
        message: str = re.sub(rf'(?<={field}=)([^{separator}]+)(?=;)',
                              redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init method"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format method"""
        record.msg: str = filter_datum(self.fields, self.REDACTION,
                                       record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """get_logger method"""
    logger_with_name = logging.getLogger("user_data")
    logger_with_name.setLevel(logging.INFO)
    logger_with_name.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger_with_name.addHandler(stream_handler)
    return logger_with_name


def get_db() -> mysql.connector.connection.MySQLConnection:
    """get_db method"""
    connection = mysql.connector.connect(
        host=os.environ.get('localhost'),
        user=os.environ.get('root'),
        password=os.environ.get(''),
        database=os.environ.get('holberton')
    )
    return connection

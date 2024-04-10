#!/usr/bin/env python3
"""filter_datum for hide the sen.. data"""
from typing import List
import re
import logging


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

    def __init__(self, fields: List(str)):
        """init method"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format method"""
        record.msg: str = filter_datum(self.fields, self.REDACTION,
                                       record.msg, self.SEPARATOR)
        return super().format(record)

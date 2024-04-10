#!/usr/bin/env python3
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """filter_datum"""
    for field in fields:
        message: str = re.sub(rf'(?<={field}=)([^{separator}]+)(?=;)',
                              redaction, message)
    return message

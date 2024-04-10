#!/usr/bin/env python3
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    for field in fields:
        message = re.sub(rf'(?<={field}=)([^;]+)(?=;)', redaction, message)
    return message

import os

from helpers import strings_utils


def is_need_show_more_info() -> bool:
    return strings_utils.is_strings_equals(os.environ.get("SHOW_MORE_INFO"), 'True')

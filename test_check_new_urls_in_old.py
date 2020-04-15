import logging
import os
import unittest
from copy import copy
from typing import List
import pandas as pd

from helpers import env


class TestClass(unittest.TestCase):
    test_data_dir_name = str(os.environ['TEST_DATA_DIR'])
    test_data_file_name = str(os.environ['FILE_NAME'])
    old_site_pages = 'Старый сайт'
    new_site_pages = 'Новый сайт'

    def test_find_new_urls_in_old(self):
        """Проверяет строгое наличие каждого нового урла в списке старых урлов и выводит в конце список тех новых урлов,
        которых не смог найти"""
        df = pd.read_excel(self.test_data_dir_name + '/' + self.test_data_file_name)
        old_site_pages = self.get_old_site_pages(df)
        new_site_pages = self.get_new_site_pages(df)

        do_not_find_new_urls = list()
        old_site_pages_without_new_urls = copy(old_site_pages)

        for new_site_page in new_site_pages:
            if new_site_page not in old_site_pages:
                logging.warning(f"'{new_site_page}' НЕ НАЙДЕН в списке урлов старого сайта")
                do_not_find_new_urls.append(new_site_page)
            else:
                if env.is_need_show_more_info():
                    logging.info(f"{new_site_page} найден в списке старых урлов")
                old_site_pages_without_new_urls.remove(new_site_page)

        logging.info(f"Всего проверено новых урлов {len(new_site_pages)}")
        logging.info(f"Всего старых урлов {len(old_site_pages)}")

        if len(do_not_find_new_urls) == 0:
            logging.info("Список ненайденных новых урлов в старых пустой. Ты молодец, белка! :)")
        else:
            logging.warning(f"Список ненайденных новых урлов в старых в количестве {len(do_not_find_new_urls)}")
            print(do_not_find_new_urls)

        assert len(old_site_pages_without_new_urls) > 0, "old_site_pages_without_new_urls must be not 0"

        output_file_name = self.test_data_dir_name + '/' + 'old_urls_without_new.txt'
        with open(output_file_name, 'w') as f:
            f.truncate(0)
            for old_site_page_without_new_urls in old_site_pages_without_new_urls:
                f.write("%s\n" % old_site_page_without_new_urls)

        logging.info(f"Старые урлы без включения найденных новых записаны в файл: {output_file_name}")

    def get_old_site_pages(self, df) -> List:
        old_site_pages = df[self.old_site_pages].astype(str)
        result = list(filter(lambda old_site_page: old_site_page and old_site_page != 'nan', old_site_pages))

        assert len(result) != 0, "Old site pages list len() == 0. It's bad!"
        return result

    def get_new_site_pages(self, df) -> List:
        new_site_pages = df[self.new_site_pages].astype(str)
        result = list(filter(lambda new_site_page: new_site_page and new_site_page != 'nan', new_site_pages))

        assert len(result) != 0, "New site pages list len() == 0. It's bad!"
        return result

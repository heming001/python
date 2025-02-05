"""
    Export and Import Elasticsearch Data.
    Simple Example At __main__
    @author: wgzh159@163.com
    @note:  uncheck consistency of data, please do it by self
"""

import json
import os
import time
import logging
from elasticsearch import Elasticsearch, helpers
from concurrent.futures import ThreadPoolExecutor, as_completed

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ExportEsData:
    SIZE = 10000

    def __init__(self, url, index_pattern, type_, username, password):
        self.es = Elasticsearch([url], http_auth=(username, password))
        self.index_pattern = index_pattern
        self.type = type_

    def export_data(self):
        logging.info("Export data begin...")
        start_time = time.time()

        indices = self._get_indices()
        with ThreadPoolExecutor(max_workers=25) as executor:
            futures = [executor.submit(self._export_index, index) for index in indices]
            for future in as_completed(futures):
                future.result()

        logging.info(f"Export data end!!!\n\t total consuming time: {time.time() - start_time}s")

    def _export_index(self, index):
        try:
            query = {
                "query": {
                    "match_all": {}
                },
                "size": self.SIZE
            }
            response = helpers.scan(self.es, index=index, query=query)
            self._write_file(response, index)
        except Exception as e:
            logging.error(f"Error exporting data for index {index}: {e}")

    def _write_file(self, response, index):
        file_path = f"{index}_{self.type}.json"
        with open(file_path, "a", encoding='utf-8') as f:
            for doc in response:
                a = json.dumps(doc['_source'], ensure_ascii=False)
                f.write(a + "\n")

    def _get_indices(self):
        # 获取匹配索引模式的所有索引
        indices = self.es.indices.get_alias(index=self.index_pattern)
        return indices.keys()

class ImportEsData:
    def __init__(self, url, index_pattern, type_, username, password):
        self.es = Elasticsearch([url], http_auth=(username, password))
        self.index_pattern = index_pattern
        self.type = type_

    def import_data(self):
        logging.info("Import data begin...")
        start_time = time.time()

        indices = self._get_indices_from_files()
        with ThreadPoolExecutor(max_workers=25) as executor:
            futures = [executor.submit(self._import_index, index) for index in indices]
            for future in as_completed(futures):
                future.result()

        logging.info(f"Import data end!!!\n\t total consuming time: {time.time() - start_time}s")

    def _import_index(self, index):
        file_path = f"{index}_{self.type}.json"
        self._create_index_if_not_exists(index)
        try:
            with open(file_path, "r", encoding='utf-8') as f:
                actions = []
                batch_count = 0  # 添加计数器来跟踪批次
                for line in f:
                    source = json.loads(line)
                    action = {
                        "_index": index,
                        "_type": self.type,
                        "_source": source
                    }
                    actions.append(action)
                    if len(actions) >= ExportEsData.SIZE:
                        helpers.bulk(self.es, actions)
                        actions = []
                        batch_count += 1  # 增加批次计数
                        logging.info(f"Imported batch {batch_count} of {ExportEsData.SIZE} documents for index {index}.")
                if actions:
                    helpers.bulk(self.es, actions)
                    batch_count += 1  # 增加批次计数
                    logging.info(f"Imported final batch {batch_count} of {len(actions)} documents for index {index}.")
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
        except Exception as e:
            logging.error(f"Error reading file: {e}")

    def _get_indices_from_files(self):
        # 获取文件名中的索引名称
        files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(f"_{self.type}.json")]
        indices = [f.split(f"_{self.type}.json")[0] for f in files]
        return indices

    def _create_index_if_not_exists(self, index):
        if not self.es.indices.exists(index=index):
            self.es.indices.create(index=index)
            logging.info(f"Created index: {index}")

if __name__ == '__main__':
    """
        Export Data
        e.g.
                            URL                    index_pattern        type
        exportEsData("http://10.100.142.60:9200","watchdog","mexception").export_data()
         
        export file name: watchdog_mexception.json
    """
    ExportEsData("http://10.255.24.172:9200/", "oms*", "_doc","elastic","1234556").export_data()

    """
        Import Data
         
        *import file name:watchdog_test.json    (important)
                    "_" front part represents the elasticsearch index_pattern
                    "_" after part represents the  elasticsearch type
        e.g.
                            URL                    index_pattern        type
        importEsData("http://10.100.142.60:9200","watchdog","test").import_data()
    """
   
    # ImportEsData("http://10.255.24.172:9200/", "active_directory-corp-2021.1*", "_doc","elastic","123456").import_data()

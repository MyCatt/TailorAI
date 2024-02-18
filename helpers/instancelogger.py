import os
import shutil
import time
from datetime import datetime


class InstanceLogger:
    def __init__(self, label="", base_path="./Instances/", clear_cache=True):
        self.session = str(time.time())
        self.label = label.lower()
        self.base_path = base_path
        self.session_path = self.base_path + self.label + self.session

        if clear_cache:  # Clear Cache On Init
            self.clear_cache()

        self.__create_session()

    def clear_cache(self):
        os.makedirs(self.session_path)  # Lazy and don't want to check if the dir exists so just instantiating each time
        shutil.rmtree(self.base_path)

    def __create_session(self):
        os.makedirs(self.session_path)
        self.__create_session_file()

    def __create_session_file(self):
        with open(self.session_path + "/log.md", 'w+', encoding="utf-8") as f:
            f.write("Session Started: " + str(datetime.now()) + "\n")
            f.write("-" * 2 + "\n")

    def log_meta(self, source, meta):
        with open(self.session_path + "/log.md", 'a', encoding="utf-8") as f:
            f.write(str(f'>[{source}] ') + str(meta) + "\n\n")

    def log_raw_data(self, source, label, meta):
        with open(self.session_path + "/log.md", 'a', encoding="utf-8") as f:
            f.write(str(f'<details><summary>{label}</summary>[{source}]\n\n') + str(meta) + "</details>\n")

    def log_fenced(self, source, content):
        with open(self.session_path + "/log.md", 'a', encoding="utf-8") as f:
            f.write(f'[{source}]\n```\n{str(content)}\n\n```\n\n')

    def log_table(self, source, table):
        with open(self.session_path + "/log.md", 'a', encoding="utf-8") as f:
            f.write(f'[{source}]\n\n{str(table)}\n\n')

    def log_code(self, source, lang, content):
        with open(self.session_path + "/log.md", 'a', encoding="utf-8") as f:
            f.write(f'[{source}]\n\n```{lang}\n\n{str(content)}\n\n```\n\n')

    def log_standard(self, source, meta):
        with open(self.session_path + "/log.md", 'a', encoding="utf-8") as f:
            f.write(str(f'[{source}] \n') + str(meta) + "\n\n")


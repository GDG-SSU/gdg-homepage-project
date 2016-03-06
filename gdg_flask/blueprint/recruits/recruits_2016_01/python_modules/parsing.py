"""
파일을 파싱해서 DB에 넣을 것이다.

"""
import yaml


class FileParser(object):
    def __init__(self, file_name, file_mode="r"):
        self.file_name = file_name
        self.file_mode = file_mode

    def ymlReading(self):
        with open(self.file_name, self.file_mode) as f:
            f_content = f.read()
            yml_content = yaml.load(f_content)
        return yml_content

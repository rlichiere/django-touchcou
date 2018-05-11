
import yaml

from utils import utils


class Config(object):
    def __init__(self):
        self.data = dict()
        self.baseDir = ''

    def setBaseDir(self, base_dir):
        self.baseDir = base_dir
        self.load()

    def load(self):
        _configFile = open('%s/touchcou/config/config_private.yml' % self.baseDir)
        self.data = yaml.load(_configFile)

    def get(self, path, default=None):
        _res = utils.access(self.data, path)
        if _res is None:
            return default
        return _res


config = Config()

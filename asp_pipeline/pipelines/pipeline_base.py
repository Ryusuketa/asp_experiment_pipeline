import numpy as np
import luigi
import gzip
from abc import abstractmethod


class DataLoadTaskBase(luigi.Task):
    dir_path = luigi.Parameter()
    save_path = luigi.Parameter()

    def input_local_data(self, load_function):
        data = load_function(self.dir_path)

        return data

    def output(self):
        return luigi.LocalTarget(f"{self.save_path}.gz", format=luigi.format.GzipFormat)

    @abstractmethod
    def run(self):
        pass

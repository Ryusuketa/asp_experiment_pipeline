import luigi
from functools import partial
from asp_pipeline.pipelines.pipeline_base import DataLoadTaskBase
import glob

def _each_file_load(path):
    np.load(path)


def impulse_data_loader(data_path, n_channels):
    li_data = []
    if n_channels == 1:
        li_data.append()
    else:


class IRLoadTask(DataLoadTaskBase):
    n_channels = luigi.IntParameter()
import numpy as np


def _load(path: str) -> np.ndarray:
    ext = path.split('.')[-1]
    try:
        if ext = 'wav':
            data = load_wav(path)
        else:
            data = np.load(path)

    except:
        raise ValueError('input data must be "wav" or float64 binary data')


def load_ir(path: str, n_channels: int) -> np.ndarray:
    data = np.load(path)

    data.shape

    return

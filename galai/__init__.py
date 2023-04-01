from galai.model import Model
from galai.utils import get_checkpoint_path, get_tokenizer_path


def load_model(name: str, dtype: str=None, num_gpus: int=None):
    """
    Utility function for loading the model

    Parameters
    ----------
    name : str
        Name of the model

    dtype: str
        Optional dtype; default float32 for smaller models

    num_gpus: int
        Number of GPUs to use, default 8 GPUs

    Returns
    ----------
    Model - model object
    """
    if name not in ['mini', 'base', 'standard', 'large', 'huge']:
        raise ValueError("Invalid model name. Must be one of 'mini', 'base', 'standard', 'large', 'huge'.")

    if dtype is None:
        dtype = 'float16' if name == 'huge' else 'float32'
    if num_gpus is None:
        num_gpus = 8

    model = Model(name=name, dtype=dtype, num_gpus=num_gpus)
    model._set_tokenizer(tokenizer_path=get_tokenizer_path())
    model._load_checkpoint(checkpoint_path=get_checkpoint_path(name))
    return model

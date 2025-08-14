'''
    Folder for testing GPU types, device operations, wrapper, or handlers

    params:
        None
    returns:
        torch.device object if GPU is available, otherwise torch.device("cpu")
'''


import torch

def get_device():
    if torch.backends.mps.is_available():
        return torch.device("mps")
    else:
        return torch.device("cpu")
    


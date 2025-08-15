import pandas as pd
from typing import Generator, Optional, Callable, Sequence  




# Version 0.0.1:
class TestDataGenerator:
    def __init__(self, filepath_or_buffer: Optional[str], limit: Optional[int]):
        self.filepath_or_buffer = filepath_or_buffer
        self.limit = limit
        self.iterrows = self._function(self.filepath_or_buffer)
        
    def _function(self, filepath_or_buffer: Optional[str]):
        return pd.read_csv(filepath_or_buffer)

    def __call__(self) -> Generator[pd.DataFrame, None, None]:
        for idx, row in enumerate(self.iterrows): 
            if idx >= self.limit:
                raise StopIteration 
            yield row 



class TestDataGeneratorV2:
    
    
    pass 


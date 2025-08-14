import pandas as pd
from typing import Generator, Optional, Callable, Sequence  

class TestDataGenerator:
    def __init__(self, function: Optional[Callable[[], ...]], limit: Optional[int], filepath_or_buffer: Optional[str]):
        self.function = function
        self.limit = limit
        self.filepath_or_buffer = filepath_or_buffer
        self.iterrows = self.function(self.filepath_or_buffer)

    def __call__(self, limit: Optional[int] = None) -> Generator[pd.DataFrame, None, None]:
        for idx, row, in range(self.iterrows, self.limit): 
            yield row 



    

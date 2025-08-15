from dataclasses import dataclass
from typing import Optional, List, Any
from enum import Enum
import argparse
import json
import sys


sys.dont_write_bytecode = True 

@dataclass
class ParserType(Enum):
    TEST = "test"
    MAIN = "main"

class TestParser:
    PATH : str = ""
    
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Process some data.')
        group = self.parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--test', action='store_true', help='Run in test mode')
        group.add_argument('--main', action='store_true', help='Run in main mode')
        self.parser.add_argument('--url', type=self.add_URL, action='append', default=[], help='URL or path to the data file')
        self.parser.add_argument('--urls', type=self.parse_urls, nargs='+', default=None, help='URL or path to the data file')
        self.parser.add_argument('--limit', type=int, default=None, help='Limit the number of items to process')
        self.parser.add_argument('--device', type=str, default='cpu', help='Device to run on')
        self.parser.add_argument('--model', type=str, default='gpt-3.5-turbo', help='Model to use')
        self.parser.add_argument('--path', type=self.get_PATH, action='append', default=[], help='URL or paths to the data files')
        

    def parse_args(self):
        args = self.parser.parse_args()
        
        if hasattr(args, 'urls') and args.urls:
            args.urls = self.parse_urls(args.urls)
            
        return args.test, args.main, args

    @classmethod
    def existing_urls(cls) -> List[str]:
        try:
            with open('urls.json', 'r') as f:
                data = json.load(f)
                return data.get('urls', [])
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def write_urls(cls, urls: List[str]):
        with open('urls.json', 'w') as f:
            json.dump({"urls": urls}, f, indent=4)
        f.close()

    
    def parse_urls(self, urls):
        if isinstance(urls, str):
            urls = [url.strip() for url in urls.split(',') if url.strip()]
        if not urls:
            raise argparse.ArgumentError(None, "At least one URL must be provided") 
        return urls
         

    def parse_limit(self, limit: int) -> int:
        return limit
        
    @staticmethod
    def add_URL(url: str) -> str:
        TestParser.PATH = url.strip()
        return url.strip()
    
    @staticmethod
    def get_PATH() -> str:
        return TestParser.PATH

    def parse_json(self, json_str: str) -> Any:
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            raise argparse.ArgumentError(None, f"Invalid JSON: {e}")

    
        

    
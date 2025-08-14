
## DataLoader

DataLoader is a tool for loading and processing data from HuggingFace if they are pandas formatted.. It is still a work in progress, but I will continue to maintiain this alongside other tools. 

## Installation

This tool is currently in development and is not yet available for installation but you made load it with the UV package manager after it has been installed

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Once it is installed, you can install the package with the following command:

```bash
uv pip install -e .
```

## Building

This will require a build of the library to be installed. This can be done with the following command:

```bash
uv pip install build
python -m build
```

After building, you can install the package with the following command:
```bash
uv pip install -e .
```

And finally you can create a distribution of the package with the following command:
```bash
python -m build
```

This will create a dist directory with the package in it.

## Usage

```bash
huggingface-dataloader --test
```

This will run the tool in test mode and load the data from the default path.

```bash
huggingface-dataloader --main
```

This will run the tool in main mode and load the data from the default path.

```bash
huggingface-dataloader --url "https://huggingface.co/datasets/username/dataset_name"
```

This will run the tool in test mode and load the data from the default path.

```bash
huggingface-dataloader --urls "https://huggingface.co/datasets/username/dataset_name"
```

This will run the tool in test mode and load the data from the default path.

```bash
huggingface-dataloader --limit 10
```

This will run the tool in test mode and load the data from the default path.

```bash
huggingface-dataloader --device "cuda"
```

This will run the tool in test mode and load the data from the default path.

```bash
huggingface-dataloader --model "gpt-3.5-turbo"
```

This will run the tool in test mode and load the data from the default path.

```bash
huggingface-dataloader --path "path/to/data"
```

This will run the tool in test mode and load the data from the default path.


## License

MIT License


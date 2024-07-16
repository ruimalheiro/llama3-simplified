# llama3-simplified

This project implements llama3 8B using just torch for educational purposes. The official project from Meta can be found [here](https://github.com/meta-llama/llama3).

## Key details
- Uses 4bit quantization to reduce the pretrained weights size ~17GB to ~7GB;
- Takes advantage of flash-attention;
- Implements the KV-cache as in the original project but with a small hack to work for 4bit quantization which involves a sliding window briefly explained in the code;
- Uses the tiktoken BPE tokenizer from OpenAI. Repo [here](https://github.com/openai/tiktoken);
- Context window is set to **512** tokens and was finetuned with that in consideration.
- Dataset used for finetuning the model for chat can be found [here](https://huggingface.co/datasets/lmsys/lmsys-chat-1m).

## Instructions
- Create a python environment, ideally running python 3.10.13. Example with conda: `conda create -n my_env python=3.10.13`;
- Activate the environment and run: `pip install -r requirements.txt`;
- The weights are stored in google drive but can be downloaded using the python program **download_weights.py**. Run: `python download_weights.py`; **Note:** If you get the following error at this step: *"Too many users have viewed or downloaded this file recently..."* Please use the direct link provided in the error message. Once **weights.zip** is downloaded, extract the files **pretrained.pth** and **finetuned.safetensors** to the root directory.
- Run the notebook **main.ipynb** and experiment.

## System requirements
- This was tested on an RTX 4090 but since we don't load the pretrained weights directly into GPU memory it might be possible to initialize the model in a GPU with much less VRAM.
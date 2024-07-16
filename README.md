# llama3-simplified

This project implements llama3 8B using just torch for educational purposes. The official project from Meta can be found [here](https://github.com/meta-llama/llama3).

## Key details
- Uses 4bit quantization to reduce the pretrained weights size ~17GB to ~7GB;
- Takes advantage of flash-attention;
- Implements the KV-cache as in the original project but with a small hack to work for 4bit quantization which involves a sliding window briefly explained in the code;

## Instructions
- Create a python environment, ideally running python 3.10.13. Example with conda: `conda create -n my_env python=3.10.13`;
- Activate the environment and run: `pip install -r requirements.txt`;
- The weights are stored in google drive but can be downloaded using the python program **download_weights.py**. Run: `python download_weights.py`;
- Run the notebook **main.ipynb** and experiment.

**In-progress**

## Overview

Fine tune gpt3 model, and create news prompt summary.


## Getting Started

dataset for training:
```bash
kaggle datasets download -d sunnysai12345/news-summary
```

```bash
python format_dataset.py
```
This creates "dataset.jsonl"

```bash
openai tools fine_tunes.prepare_data -f dataset.jsonl
```
this command will create a file "dataset_prepared.jsonl"

```bash
openai api fine_tunes.create -t "dataset_prepared.jsonl" -m ada
```
this command will provide a model name

## Example Usage

```bash
python run_model.py --fine_tuned_model <YOUR_MODEL_NAME>
```
or 
```bash
openai api completions.create -m <YOUR_MODEL_NAME> -p <YOUR_PROMPT>
```

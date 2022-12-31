
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

## Usage

```bash
python run_model.py --fine_tuned_model <YOUR_MODEL_NAME>
```
or 
```bash
openai api completions.create -m <YOUR_MODEL_NAME> -p <YOUR_PROMPT>
```

### Example Prompt
```bash
Randomly read one data from test_dataset.jsonl for testing.
Selected news prompt: Technology incubator Jigsaw, a subsidiary of Google-parent Alphabet, has created an online quiz to help test users' ability to detect fake emails meant for 'phishing' attacks to steal passwords or download malware. The quiz tests and teaches users to judge factors like email address to figure out the authenticity of the emails. Jigsaw further suggests users enable '2-step Verification' feature.
Summary:
```
### Output 
```bash
{
  "choices": [
    {
      "finish_reason": "length",
      "index": 0,
      "logprobs": null,
      "text": " Alphabet govt tech incubator creates quiz to help test fake emails\n\nAl"
    }
  ],
  ...
}
```



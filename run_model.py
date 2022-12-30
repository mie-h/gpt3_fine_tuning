import openai
import random
import json
import os

TEST_DATASET = 'test_dataset.jsonl'
def run_model(pv_fine_tuned_model, pv_prompt, pv_test_dataset):
    global TEST_DATASET
    if pv_test_dataset:
        print(f"Test dataset {pv_test_dataset} is provided.")
        TEST_DATASET = pv_test_dataset

    lv_prompt = pv_prompt
    if not lv_prompt:
        print(f"Prompt is not given.")
        print(f"Randomly read one data from {TEST_DATASET} for testing.")
        lv_lines = open(TEST_DATASET).read().splitlines()
        lv_line = json.loads(random.choice(lv_lines))
        lv_prompt = lv_line['prompt']
        print(f"Selected news prompt: {lv_prompt}")
    
    print(f"Run the fine tuned model : {pv_fine_tuned_model}")
    response = openai.Completion.create(
        model=pv_fine_tuned_model,
        prompt=lv_prompt)

    print(f"Given output:")
    print(response)

def main():
    curr_filename = os.path.basename(__file__)
    print(f"Running {curr_filename}")

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--fine_tuned_model", type=str, required=True
    )
    parser.add_argument(
        "--prompt", type=str
    )
    parser.add_argument(
        "--test_dataset", type=str
    )
    args = parser.parse_args()

    run_model(args.fine_tuned_model, args.prompt, args.test_dataset)

if __name__ == "__main__":
    main()
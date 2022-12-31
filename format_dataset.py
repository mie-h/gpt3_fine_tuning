import pandas as pd 
import jsonlines
import os

NUM_TRAIN_DATA = 1000
NUM_TEST_DATA = 10

def _get_df():
    """Read csv files and convert them into a dataframe."""

    summary = pd.read_csv('./kaggle/news_summary.csv', encoding='iso-8859-1')
    raw = pd.read_csv('./kaggle/news_summary_more.csv', encoding='iso-8859-1')

    pre1 = raw.iloc[:,0:2].copy()
    pre2 = summary.iloc[:,0:6].copy()
    pre2['text'] = pre2['author'].str.cat(pre2['date'].str.cat(pre2['read_more'].str.cat(pre2['text'].str.cat(pre2['ctext'], sep = " "), sep =" "),sep= " "), sep = " ")

    pre = pd.DataFrame()
    pre['text'] = pd.concat([pre1['text'], pre2['text']], ignore_index=True)
    pre['summary'] = pd.concat([pre1['headlines'],pre2['headlines']],ignore_index = True)
    return pre

def _adjust_prompt(pv_pre):
    """Adjust prompt to train gpt3"""
    for i in range(NUM_TRAIN_DATA+NUM_TEST_DATA):
        pv_pre.at[i, 'text'] = _create_prompt(pv_pre.iloc[i]['text'])
    return pv_pre

def _create_prompt(text):
    """Given text, create a prompt"""
    return text + "\nSummary:"

def _get_train_data(pv_pre):
    """Create jsonl file with data for training."""
    dataset_filename = 'dataset.jsonl'
    with jsonlines.open(dataset_filename, mode='w') as writer:
        for i in range(NUM_TRAIN_DATA):
            writer.write({
            'prompt': pv_pre.iloc[i]['text'],
            'completion': pv_pre.iloc[i]['summary']
            })
    return dataset_filename

def _get_test_data(pv_pre):
    """Create jsonl file with data for testing."""
    test_dataset_filename = 'test_dataset.jsonl'
    with jsonlines.open(test_dataset_filename, mode='w') as writer:
        for i in range(NUM_TRAIN_DATA, NUM_TRAIN_DATA+NUM_TEST_DATA):
            writer.write({
            'prompt': pv_pre.iloc[i]['text'],
            'completion': pv_pre.iloc[i]['summary']
            })

def format_dataset():
    """ The format_dataset() function is used to format data and save it to jsonl file."""
    lv_pre = _get_df()
    lv_pre = _adjust_prompt(lv_pre)

    lv_dataset_filename = _get_train_data(lv_pre)
    lv_test_dataset_filename = _get_test_data(lv_pre)
    
    return lv_dataset_filename, lv_test_dataset_filename

def main():
    curr_filename = os.path.basename(__file__)
    print(f"Running {curr_filename}")

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--num_train_data", type=int
    )
    parser.add_argument(
        "--num_test_data", type=int
    )
    args = parser.parse_args()
    if args.num_train_data:
        NUM_TRAIN_DATA = args.num_train_data
    if args.num_test_data:
        NUM_TEST_DATA = args.num_test_data
        
    lv_dataset_filename, lv_test_dataset_filename = format_dataset()
    print(f"{lv_dataset_filename} and {lv_test_dataset_filename} are created.")

if __name__ == "__main__":
    main()
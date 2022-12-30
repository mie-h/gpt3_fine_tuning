"""
reference:
https://www.kaggle.com/code/sandeepbhogaraju/text-summarization-with-seq2seq-model
"""
import pandas as pd 
import os
import jsonlines

NUM_TRAIN_DATA = 1000
NUM_TEST_DATA = 10

def format_dataset():
    for dirname, _, filenames in os.walk('/kaggle/input'):
        for filename in filenames:
            print(os.path.join(dirname, filename))

    summary = pd.read_csv('./kaggle/news_summary.csv', encoding='iso-8859-1')
    raw = pd.read_csv('./kaggle/news_summary_more.csv', encoding='iso-8859-1')

    pre1 = raw.iloc[:,0:2].copy()
    pre2 = summary.iloc[:,0:6].copy()
    pre2['text'] = pre2['author'].str.cat(pre2['date'].str.cat(pre2['read_more'].str.cat(pre2['text'].str.cat(pre2['ctext'], sep = " "), sep =" "),sep= " "), sep = " ")

    pre = pd.DataFrame()
    pre['text'] = pd.concat([pre1['text'], pre2['text']], ignore_index=True)
    pre['summary'] = pd.concat([pre1['headlines'],pre2['headlines']],ignore_index = True)

    for i in range(NUM_TRAIN_DATA+NUM_TEST_DATA):
        pre.at[i, 'text'] = pre.iloc[i]['text'] + "\nSummary:"

    dataset_filename = 'dataset.jsonl'
    with jsonlines.open(dataset_filename, mode='w') as writer:
        for i in range(NUM_TRAIN_DATA):
            writer.write({
            'prompt': pre.iloc[i]['text'],
            'completion': pre.iloc[i]['summary']
            })

    test_dataset_filename = 'test_dataset.jsonl'
    with jsonlines.open(test_dataset_filename, mode='w') as writer:
        for i in range(NUM_TRAIN_DATA, NUM_TRAIN_DATA+NUM_TEST_DATA):
            writer.write({
            'prompt': pre.iloc[i]['text'],
            'completion': pre.iloc[i]['summary']
            })


    return dataset_filename, test_dataset_filename

def main():
    format_dataset()

if __name__ == "__main__":
    main()
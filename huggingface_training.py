from transformers import AutoTokenizer
from transformers import TrainingArguments, Trainer
from datasets import load_dataset
ds = load_dataset('csv', data_files="EarthHack_Dataset.csv")

# ds {'train':  dataset}, check hugging face for more documentation
print(ds.keys())
print(ds['train']['id'][0])
print(ds['train']['problem'][0])
print(ds['train']['solution'][0])

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
print(tokenizer(ds['train']['solution'][0], padding="max_length", truncation=True))


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

## Find the word count of each problem and solution
problem_word_count = [len(problem.split()) for problem in ds['train']['problem']]
solution_word_count = [len(solution.split()) for solution in ds['train']['solution']]
print(problem_word_count[:5])
print(solution_word_count[:5])

## Find the most common words in the problem and solution
from collections import Counter
problem_word_counter = Counter()
solution_word_counter = Counter()
for problem in ds['train']['problem']:
    problem_word_counter.update(problem.split())
for solution in ds['train']['solution']:
    solution_word_counter.update(solution.split())
print(problem_word_counter.most_common(10))
print(solution_word_counter.most_common(10))



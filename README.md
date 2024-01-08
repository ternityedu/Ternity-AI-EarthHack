# Ternity AI EarthHack
Official submission repo from team Ternity AI for the [AI EarthHack competition](genaicompetition.com)

### Instructions

#### Text preprocessing/cleaning and dataset visualization

1. Download knowledge base of articles into local copy of repository.
   Some articles are not open access, hence the exclusion of the entire `rag_kb` folder from this public repo. The folder contains two sub-folders, one for each role ("internal monologue") that CirconBot can take on, "investor" and "scholar".<br/>
   Link: https://www.4shared.com/folder/Ja_zfK4n/rag_kb.html<br/>
   pw: repo name with parts in reverse order, no hyphens or spaces

3. Run the following to install requirements, preferably on Python 3.11.

   ``` pip install -r requirements.txt ```

4. Edit `DATA_FILENAME` and `WORDCLOUD_FILENAME` in `main.py`. `DATA_FILENAME` should point to a file with the same format as `AI EarthHack Dataset.csv`, the training dataset provided for the AI EarthHack. Optional `CLEANED_DATASET` can be specified to load a pickled cleaned dataset.

5. Run `main.py` to generate two wordclouds of the key words in both problems and solutions within the dataset. This gives the user a way to visualize the key concepts and ideas in the dataset. One could then be on the lookout for pitches that _don't_ include these most common ideas, if one were to seek innovative solutions.

   ``` python3 main.py ```

6. (Optional) You will likely notice the wordclouds dominated by a few big words. Some have already been manually excluded, but you can add more words to exclude by adding them to the `EXCLUDE` list in `utils.py`. This allows you to focus on whichever level of generality you want (e.g. one could exclude many of the most general words to get a sense of specific ideas).

#### Basic evaluation rubric with ChatGPT-3.5
##### (Free OOTB solution with zero setup)

Example chat (including generation of rubric): https://chat.openai.com/share/989bec29-784e-4013-8074-885da3c241fc

1. Provide the following instructions to ChatGPT:

   ```You are a former teacher who is familiar with assignment grading rubrics for student assessment. You have since had a career as both an academic researcher studying the envoriment impact of new technologies and businesses, as well as a startup founder as well as investor who understands the market and industry around green business ventures. You will now transfer those all those skills, knowledge, and expertise, and use the provided rubric to evaluate new circular economy business ideas based on 6 evaluation criteria.```

3. Copy and paste the evaluation rubric from `Evaluation Rubric.md`.
   
4. Provide a proposed business idea in the following format:

   ```
   Business Idea Name
   Problem: [problem description goes here]
   Solution: [proposed solution goes here]
   ```
5. Adjust the output by asking ChatGPT to be more (or possibly less?) constructively critical.
   
6. (Optional) Ask ChatGPT to generate a circular economy business idea of its own.

### AI Philosophy
For all the claimed advancements in GenAI and LLMs these past few years, we would argue that relatively little _true_ progress has been made since the Transformer and BERT in 2017-18, upon which all major models today are built. While there have been some model improvements, the bulk of performance gains has been from simply larger models with more parameters and compute to train. As Ternity AI Founder Haihao Liu proposed in 2020 for his doctoral thesis (under "Graduate Research Fellow" at https://www.linkedin.com/in/haihaoliu/details/experience/), it will be the explicit incorporation of domain knowledge into models, deeply embedded and encoded in the model architecture itself, that will finally bring us out of this plateau.

### Bibliography

Rose, Stuart, et al. "Automatic keyword extraction from individual documents." Text mining: applications and theory (2010): 1-20. doi:[10.1002/9780470689646.ch1](https://doi.org/10.1002/9780470689646.ch1).

Krenn, Mario, and Anton Zeilinger. "Predicting research trends with semantic and neural networks with an application in quantum physics." Proceedings of the National Academy of Sciences 117.4 (2020): 1910-1916. doi:[10.1073/pnas.1914370116](https://doi.org/10.1073/pnas.1914370116).

Qingyun Wu, et al. "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation", 2023; [arXiv:2308.08155](https://arxiv.org/abs/2308.08155).

Alexandra Sasha Luccioni, Yacine Jernite, Emma Strubell. "Power Hungry Processing: Watts Driving the Cost of AI Deployment?", 2023; [arXiv:2311.16863](https://arxiv.org/abs/2311.16863).

Singh, Pardeep, et al. "Green Circular Economy: A New Paradigm for Sustainable Development." (2023). isbn:978-3-031-40304-0

Works consulted for technical background information:<br/>
https://www.4shared.com/folder/12qMHT7K/bib.html<br/>
pw: ditto

Unicode decode error:<br/>
https://medium.com/@anala007/dealing-with-the-unicodedecodeerror-in-pandas-when-reading-csv-files-edc4987bf68b

Co-writing text processing code:
https://chat.openai.com/share/0b8f0792-3c00-4153-96f0-efb14d6cb368

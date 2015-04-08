# Question-Answer-

The focus of this phase is to build a question­answering system for Cricket Video Dataset.

Dataset Description: 

In this, a set of matches were used. Now the dataset for this is the commentary section of those set of matches. Note that the commentary is not entirely free text, it has some structure and on the basis of the questions asked, you need to see what kind of data would you need to save or recover from that semi­structured commentary. [For some of the questions, temporal features like which ball, which over etc might be useful.]

The questions that have been asked admittedly don’t have a specific grammar but follow a pattern ­  they would talk about match number etc. You should try and extract this information from the questions using some trivial techniques like a set of regular expressions, which will make the answers more relevant and accurate. Basically there are two techniques to solve these questions, you should try with (i) and if the recall is too low, you can go ahead and try to answer the question using technique (ii). Here’s a brief description of the two techniques; ­ these are more of intuitive notions and heuristics rather than proper techniques. 


(i). Try to find sentences that match the question’s unigrams the most; this can be extended to bigram and trigram, but note that you’d have to understand the trade off between precision and recall. Another thing that can be done is to look at the bold and italicized keywords and try to rank the relevant sentences according to that and return those sentences or relevant information from them.

(ii). Second technique is what is known as query expansion. If we cannot find the keyword anywhere in the dataset, we should try to expand the query ­ what it means is we should try to look for words that have same or similar meaning as the keyword and try to search for those words. Now, how do we find the related words ­ Using synsets from nltk’s Wordnet interface which is a large concept graph.

import mylib.myTextmining as tm
from collections import Counter
from konlpy.tag import Okt
#코퍼스 로딩
#input_filename  = "daum_movie_review.csv"
input_filename  = "AI_naver_news.csv"
corpus_list = tm.load_corpus_csv("./data/"+input_filename,"description")
print(corpus_list[:10])
#빈도수 추출
my_tokenizer = Okt().pos
my_tags = ['Noun','Abjective','Verb']
#my_tags = ['NNG','NNP','VV','VA']
my_stopwords = ['하며','입','하고','로써','하여','애','한다','이','그','영화']
counter = tm.analyze_word_freq(corpus_list, my_tokenizer, my_tags, my_stopwords)
#tm.visualize_barchart(counter,"다음 영화")
tm.visualize_wordchart(counter)

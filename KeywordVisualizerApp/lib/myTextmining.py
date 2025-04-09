from collections import Counter
import pandas as pd
def load_corpus_csv(corpus_file,col_name):
    
    data_df = pd.read_csv(corpus_file)
    result_list = list(data_df[col_name])
    return result_list

def tokenize_korea_corpus(corpus_list,tokennizer,tags,stopwords):
    
    text_pos_list = []
    for text in corpus_list:
        text_pos = tokennizer(text)
        text_pos_list.extend(text_pos)
    token_list = [token for token,tag in text_pos_list if tag in tags and token not in stopwords]
    return token_list

def analyze_word_freq(corpus_list,tokenizer,tags,stopwords):
    token_list = tokenize_korea_corpus(corpus_list,tokenizer,tags,stopwords) 
    counter = Counter (token_list)
    return counter

def visualize_barchart(counter):
    most_common = counter.most_common(20)
    word_list = [word for word,counter in counter.most_common(20)]
    count_list = [count for word,count in counter.most_common(20)]

    from matplotlib import font_manager, rc
    font_path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)
    import matplotlib.pyplot as plt

    # 수평 막대그래프
    plt.barh(word_list[::-1],count_list[::-1])
    # 그래프 정보 추가 
    plt.title("")
    plt.xlabel("빈도수")
    plt.ylabel("키워드")
    # 화면에 출력
    plt.show()

def visualize_wordchart(counter):
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt 


    # 한글 폰트 path 지정
    font_path = "c:/Windows/fonts/malgun.ttf"

    # WordCloud 객체 생성
    wordcloud = WordCloud(font_path,
                      width = 600,
                      height = 600,
                      max_words = 50, 
                      background_color='ivory')
    # 빈도 데이터로 워드클라우드 시각화
    wordclude = wordcloud.generate_from_frequencies(counter)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()




###### cleaning the twitter data 
tweets_cleaning <- read.csv(file.choose())
str(tweets_cleaning)

#building corpus
library(tm)
corpus <- iconv(tweets_cleaning$text)
corpus <- Corpus(VectorSource(corpus))
inspect(corpus[1:5])


## cleaning text

corpus <- tm_map(corpus, tolower) #converting all into lower case
inspect(corpus[1:5])

corpus <- tm_map(corpus, removePunctuation)
inspect(corpus[1:5])

corpus <- tm_map(corpus, removeNumbers)
inspect(corpus[1:5])

tweets_cleaned <- tm_map(corpus, removeWords, stopwords('english'))
inspect(tweets_cleaned[1:5])

removeURL <- function(x) gsub('http[[:alnum:]]*', '', x)
tweets_cleaned <- tm_map(tweets_cleaned, content_transformer(removeURL))
inspect(tweets_cleaned[1:5])

tweets_cleaned <- tm_map(tweets_cleaned, removeWords, c('put', 'said', 'say', 'well', 'say', 'can'))
tweets_cleaned <- tm_map(tweets_cleaned, stripWhitespace)
inspect(tweets_cleaned[1:5])

##########################################################################################
#########################################################################################

## now making term document matrix
tdm <- TermDocumentMatrix(tweets_cleaned)
tdm
tdm <- as.matrix(tdm)
tdm[1:10, 1:20] ## look at the query words

## barplot
w1 <- rowSums(tdm)
w1 

w2 <- subset(w1, w1>=100)
w2
x11()
barplot(w2,
        las = 2,
        col = rainbow(66))


#################################################################################################
## wordcloud

library(wordcloud)
x11()
w3 <- sort(rowSums(tdm), decreasing = TRUE)
set.seed(223)
wordcloud(words = names(w3),
          freq = w3,
          max.words = 500,
          random.order = F,
          min.freq = 50,
          colors = brewer.pal(8, 'Dark2'),
          scale = c(7, 0.8),
          rot.per = 0.4
          )



############# obtaining sentiment scores

library(syuzhet)
library(lubridate)
library(ggplot2)
library(scales)
library(reshape2)
library(dplyr)
sen_tweets <- read.csv(file.choose(), header = T)
sen_tweets_2 <- iconv(sen_tweets$text)

A <- get_nrc_sentiment(sen_tweets_2)
head(A)

#barplot
x11()
barplot(colSums(A), 
        las = 2,
        col = rainbow(10),
        ylab = 'Count',
        main = 'sentiment scores for tweets')


library(twitteR)
??twitterR

API_Key <- "Q2pvxjzlMSQkpSyIpR1BSAH6X"
API_Secret <- "hpzRO2rIuAiHu9dapzzC3biMyQNUMUHegTx4fei895iJR2YKsw"
TOKEN_KEY <- "960934311074648065-O4mqWOcDGa2pnDFKSgB4JuNYjAGm7xP"
TOKEN_SECRET <- "NrwxGHqQO33G4dFHmlD9Frl2jdbsNRa8GvOVKAf0HWgmR"

setup_twitter_oauth(API_Key,API_Secret,TOKEN_KEY,TOKEN_SECRET)

#######
## using twitteR to pull data
suppressPackageStartupMessages(library(magrittr)) 
# for using the (pipe) %>% operator
# returns a data.frame
twitteR::getCurRateLimitInfo() %>% head(., n = 10)
twitteR::getCurRateLimitInfo("search")

# getting the data
register_sqlite_backend("newtweets_db") # if db doesn't exist, it will be created.

spacex_raw = search_twitter_and_store("TrumpShutdown", 
                                      table_name = "newtweets_db", 
                                      lang = "en",
                                      retryOnRateLimit = 50)

##converting it into data frame
newtweets_df = load_tweets_db(table_name = "newtweets_db") %>% twListToDF()
str(newtweets_df)
dim(newtweets_df)

## converting data into csv
write.csv(newtweets_df, file = 'rawTweets.csv', row.names = F)
getwd()


## for word count we need text file 
tweetsdf <- data.frame(newtweets_df$text)
write.table(tweetsdf, file = 'tweets_mrjob.txt', row.names = F, sep = '\t')
getwd()

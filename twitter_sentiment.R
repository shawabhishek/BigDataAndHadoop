#!/bin/Rscript

# grab the raw output from hive (note that hive is doing the heavy lifting and R is receiving only a small set of aggregated data)
raw <- system2("hive", "-e 'USE alanshaw8481_twitter_sentiment; SELECT country, SUM(CASE WHEN sentiment = 0 THEN 1 ELSE 0 END) AS Negative, SUM(CASE WHEN sentiment = 1 THEN 1 ELSE 0 END) AS Neutral, SUM(CASE WHEN sentiment = 2 THEN 1 ELSE 0 END) AS Positive, COUNT(*) As Total FROM tweetsbi GROUP BY country;'", stdout=TRUE)

# convert the raw character vector into a list of character vectors
intermediate <- unlist(strsplit(raw, '\t'))

# convert the list into a matrix of character data
sentimentmatrix <- matrix(data = intermediate, ncol = 5, byrow = TRUE)

# convert the matrix into a data frame
sentimentframe <- as.data.frame(sentimentmatrix, stringsAsFactors = FALSE)

# cast the count columns as numeric
class(sentimentframe[[2]]) <- "numeric"
class(sentimentframe[[3]]) <- "numeric"
class(sentimentframe[[4]]) <- "numeric"
class(sentimentframe[[5]]) <- "numeric"

# manipulate the data to work with a logarithmic scale
# (otherwise the majority of countries are too small to see)
sentimentframe[[2]] <- (sentimentframe[[2]] / sentimentframe[[5]]) * log(sentimentframe[[5]])
sentimentframe[[3]] <- (sentimentframe[[3]] / sentimentframe[[5]]) * log(sentimentframe[[5]])
sentimentframe[[4]] <- (sentimentframe[[4]] / sentimentframe[[5]]) * log(sentimentframe[[5]])

# sort the data frame descending by total number of tweets
sentimentframe <- sentimentframe[order(sentimentframe[[5]],decreasing=FALSE),]

# setup the column height matrix
hts = t(data.matrix(sentimentframe[,2:4]))

# setup the country labels vector
names = sentimentframe[[1]]

pdf(file = 'alanshaw8481project.pdf', width = 7.5, height = 10, paper = 'letter')

# adjust the margins
par(mar = c(5, 9, 4, 2) + 0.1)

# plot
barplot(height = hts, names.arg = names, horiz = TRUE, col = c('red', 'white', 'green'), main = 'Twitter Sentiment for Iron Man 3 by Country', sub = '(negative = red, netural = white, positive = green)', xlab = 'Natural Logarithm of Number of Tweets', cex.names = 0.65, las = 1)

dev.off()

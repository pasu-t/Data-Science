############ data types ##############
x<-5
str(x)
print(class(x))
y<-"python"
str(y)
print(class(y))
x1<-c(1,4,5,9,11)
class(x1)
y1<-c("abcd","xyz", "pqr", "absl", "pgn")
class(y1)

############ R Dataframe #############
Data<-data.frame(x1,y1)
Data
fix(Data)
class(Data$x1)
class(Data$y1)
str(Data)

library(datasets)
data()
data(mtcars)
head(mtcars)
fix(mtcars)
str(mtcars)

######### Datatype conversion ###########
# nem to char
x3=50
class(x3)
x33=as.character(x3)
class(x33)

y3="abc123"
class(y3)
y33=as.numeric(y3)
class(y33)
y33

y4="123"
class(y3)
y44=as.numeric(y4)
class(y44)
y44

sample=c('a','b', 'c')
class(sample)
sample
newdata<-as.numeric(sample)
class(newdata)
newdata



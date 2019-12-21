################R Programming###################
#3 ways of variable declarations
x = 5
print(x)
y <- 10
print(y)
x+y -> z
print(z)

#vector
x = c(1,2,3,4,5)
max(x)
min(x)
mean(x)
var(x)
summary(x)

#smple dataset
library(datasets)

mydata<-data.frame(cars)
View(mydata)
fix(mydata)
print(mydata)
ncol(mydata)
nrow(mydata)
str(mydata)
head(mydata)
tail(mydata)
head(mydata, 3)
tail(mydata, 10)
distance<-mydata$dist
View(distance)
str(distance)
tail(distance, 4)
speed<-mydata$speed
fix(speed)
head(mydata$dist)
tail(mydata$speed)
plot(distance, speed)
plot(mydata)
x<-c(5,10,15,20,25)
y<-c(5,10,15,20,25)
plot(x,y)
# p<-c(A,B,C,D,E)
# q<-c(5,10,15,20,25)
# plot(p,q)
maxspeed<-max(mydata$speed)
minspeed<-min(mydata$speed)
minspeed
maxdist<-max(mydata$dist)
mindist<-min(mydata$dist)
print(mindist)
summary(mydata$dist)
summary(mydata$speed)
summary(mydata)

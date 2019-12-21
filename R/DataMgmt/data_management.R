#https://www.statmethods.net/r-tutorial/index.html
#creating new variables
x1 <- c(10,20,30,40,50)
x2 <- c(1,2,3,4,5)

mydata <- data.frame(x1,x2)
fix(mydata)

mydata$sum <- mydata$x1 + mydata$x2
mydata$mean <- (mydata$x1 + mydata$x2)/2

#attach(mydata)
mydata$sum <- x1+x2
mydata$mean <- (x1+x2)/2
#detach(mydata)

mydata <- transform(mydata,
  sum <- x1+x2,
  mean <- (x1+x2)/2)

res1 = sum(mydata$x1)
res2 = sum(mydata$x2)

#Recoding variables

age = c(56,20,111,25,30,34,75,60,58,90,86,47)
mydata = data.frame(age)

mydata$agecat <- ifelse(mydata$age > 75, c("older"), c("younger"))
fix(mydata)

mydata$agecat[age > 75] <- "Elder"
mydata$agecat[age > 45 & age < 75] <- "Middle Aged"
mydata$agecat[age < 45] <- "Young"
fix(mydata)

#Renaming variables

library(reshape)
mydata <- rename(mydata, c(agecat = "age_cat"))
fix(mydata)
names(mydata) <- c("age", "agecat")


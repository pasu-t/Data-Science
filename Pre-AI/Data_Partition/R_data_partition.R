data=data.frame(mtcars)
nrow(data)
#method1
dt=sort(sample(nrow(data), nrow(data)*.7))
train=data[dt,]        
test=data[-dt,]
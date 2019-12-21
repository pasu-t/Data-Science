#Bar chart
setwd("C:/workspace/Data-Science/R/BarChart")
H <- c(7,12,28,3,41)
png(file = "barchart.png")
barplot(H)
dev.off()

# Create the data for the chart
H <- c(7,12,28,3,41)
M <- c("Mar","Apr","May","Jun","Jul")
png(file = "barchart_months_revenue.png")
barplot(H,names.arg = M, xlab = "Month", ylab = "Revenue", col = "yellow",
        main = "Revenue chart", border = "red")
dev.off()

# Create the input vectors.
colors = c("green","orange","brown")
months <- c("Mar","Apr","May","Jun","Jul")
regions <- c("East","West","North")


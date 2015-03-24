#########################################################
### A) Installing and loading required packages
#########################################################

if (!require("gplots")) {
   install.packages("gplots", dependencies = TRUE)
   library(gplots)
   }
if (!require("RColorBrewer")) {
   install.packages("RColorBrewer", dependencies = TRUE)
   library(RColorBrewer)
   }


#########################################################
### B) Reading in data and transform it into matrix format
#########################################################

data <- read.csv("/Users/jaybwilliams1/GitHub/TCR_CancerVaccineProject/ExampleData/TimePoint02.csv", comment.char="#")
rnames <- data[,1]                            # assign labels in column 1 to "rnames"
mat_data <- data.matrix(data[,2:ncol(data)])  # transform column 2-5 into a matrix
rownames(mat_data) <- rnames                  # assign row names 


#########################################################
### C) Customizing and plotting the heat map
#########################################################

# creates a own color palette from red to green
my_palette <- colorRampPalette(c("black", "green", "red"))(n = 299)

# (optional) defines the color breaks manually for a "skewed" color transition
col_breaks = c(seq(0,2,length=100),  # for red
seq(10,100,length=100),              # for yellow
seq(100,35000,length=100))              # for green

# creates a 5 x 5 inch image
png("/Users/jaybwilliams1/GitHub/TCR_CancerVaccineProject/ExampleData/TimePoint02.png",  # create PNG for the heat map        
  width = 4*300,        # 5 x 500 pixels
  height = 20*300,
  res = 300,            # 300 pixels per inch
  pointsize = 6)        # smaller font size

heatmap.2(mat_data, 
  #cellnote = mat_data,  # same data set for cell labels
  main = "MHI",  # heat map title
  #notecol="Grey",      # change font color of cell labels to black
  density.info="none",  # turns off density plot inside color legend
  trace="none",         # turns off trace lines inside the heat map
  #mar=c(20,20),     # widens margins around plot
  col=my_palette,     # use on color palette defined earlier 
  breaks=col_breaks,    # enable color transition at specified limits
  dendrogram="none",     # only draw a row dendrogram
  Colv=TRUE,			# turn off column clustering
  key=TRUE,
  Rowv=TRUE,
  sepwidth=c(0.05,0.5),
  lhei = c(.1,3))
            

dev.off()               # close the PNG device

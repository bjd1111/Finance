library('moments')             #for calculation of skewness and kurtosis


# using  'processed_data.csv' as the raw data

data<-read.csv(file.choose())  #please choose csv file: 'processed_data.csv', if you don't have this file, use 'data process.r' to get the file
portfolio<-c("MSFT","DJI Index","EURUSD Curncy","SPTSX Index","CL1 Comdty",'USGG2YR Index')

tik<-function(x){
  #function to extract specific tikers data
  dates<-subset(data,name==as.character(x))[,1]
  prices<-subset(data,name==as.character(x))[,2]
  tik<-data.frame( date = as.Date(dates) ,price = as.numeric(prices))
  tik<-na.omit(tik)
  return(tik)
}


returns<-function(tiker){
  # calculate returns for each securities
  log_retrun<-apply(tiker[2],2,function(x) diff(log(x), lag=1))
  tiker$return <-c( rep(NA, nrow(tiker)-length(log_retrun)),log_retrun) 

  return(tiker)
}


garch<-function(tiker,alpha, beta, omega){
  # enrich the garch volatility model 
  tiker$return_square <-tiker$return^2
  tiker$conditional_var[1] <- var(tiker$return)
  tiker$conditional_var[2:length(tiker$return)] <- c(omega+alpha*tiker$return_square[2:length(tiker$return)]+beta*tiker$conditional_var[1:length(tiker$return)-1])
  
  if (((alpha + beta)<= 1) && (tiker$conditional_var>0) ){
    tiker$log_likelihood = -1/2*(log(2*pi)+log(tiker$conditional_var)+tiker$return_square/tiker$conditional_var)
    
  } 
  return(tiker)
}





# choosing date from 2010-01-01 to 2015-12-31
start_date <- '2010-01-04'
end_date<-'2015-12-31'

dates<-function(x){
  #functions to slice data
  s<-which(x$date==start_date)
  e<-which(x$date==end_date)
  x<-x[s:e,]
  return(x)
}


# 
# EWMA<-function(tiker){
#   # calculate conditional standard deviation for each securities
#   variance<-var(tiker$return,na.rm=TRUE)
#   n<-nrow(tiker)
#   for (i in 1:n){
#     variance[2:n]<-0.94*variance[1:n-1]+0.06*(tiker$return^2)[1:n-1]}
#   conditional_sd<-sqrt(variance)
#   sd_return<-tiker$return/conditional_sd
#   tiker$variance <-variance
#   tiker$conditional_sd <-conditional_sd
#   tiker$sd_return <-sd_return
#   return(tiker)
# }

alpha = 0.1
beta = 0.85
omega = 0.000005

#apply to all secuitties
for (i in portfolio){
  assign(i,garch(dates(returns(tik(i)))))
}


MLE<-function(tiker, alpha, beta, omega){
  #functions to cal MLE
  
  s = sum(tiker$log_likelihood)
  return(s)
}


optimize(f = MLE(ticker = `CL1 Comdty`,alpha = 0.1,beta = 0.85,omega =  0.000005), interval = c(1,6),maximum = TRUE)


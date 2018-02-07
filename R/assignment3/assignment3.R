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




# choosing date from 2010-01-01 to 2015-12-31
start_date <- '2010-01-05'
end_date<-'2010-02-01'

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


#apply to all secuitties
for (i in portfolio){
  assign(i,dates(returns(tik(i))))
}


garch<-function(tiker,alpha, beta, omega){
  # enrich the garch volatility model 
  tiker$return_square <-tiker$return^2
  len = length(tiker$return)
  tiker$conditional_var[1] <- c(var(tiker$return))
  for (i in (1:len)){
  tiker$conditional_var[2:len] <- c(omega+alpha*tiker$return_square[1:len-1]+beta*tiker$conditional_var[1:len-1])
  }
  for (i in (1:len)){
  if (((alpha + beta)<= 1) && (tiker$conditional_var>0) ){
    tiker$log_likelihood[i] = -1/2*(log(2*pi)+log(tiker$conditional_var[i])+tiker$return_square[i]/tiker$conditional_var[i])
  } 
  else{
    tiker$log_likelihood[i] = c(-10000)
  }
  }
  return(tiker)
}


garch_leverage<-function(tiker,alpha, beta, omega, theta){
  # enrich the garch volatility model 
  tiker$return_square <-tiker$return^2
  len = length(tiker$return)
  tiker$conditional_var[1] <- c(var(tiker$return))
  for (i in (1:len)){
    tiker$conditional_var[2:len] <- c(omega+alpha*(tiker$return[1:len-1]-theta*sqrt(tiker$conditional_var[1:len-1]))^2+beta*tiker$conditional_var[1:len-1])
  }
  for (i in (1:len)){
  if (   (  (alpha *(1 + theta^2)+beta) <= 1  )  &&  (tiker$conditional_var[i]>0)   ){
     
    tiker$log_likelihood[i] = -1/2*(log(2*pi)+log(tiker$conditional_var[i])+tiker$return_square[i]/tiker$conditional_var[i])
    
  } 
  else{
    
    tiker$log_likelihood[i] = c(-10000)
  }
  }
  return(tiker)
}








# #initial value
# alpha = 0.1
# beta = 0.85
# omega = 0.000005
# theta = 0.5

MLE<-function(tiker,x){
  #functions to cal MLE
  alpha = x[1]
  beta = x[2]
  omega = var(tiker$return)*(1-alpha-beta)
  

  tiker_temp = garch(tiker, alpha, beta, omega)
  s = sum(tiker_temp$log_likelihood)
  return(s)
}


MLE_leverage<-function(tiker,x){
  #functions to cal MLE
  alpha = x[1]
  beta = x[2]
  omega  =x[3]
  theta = x[4]
  
  
  tiker_temp = garch_leverage(tiker, alpha, beta, omega,theta)
  s = sum(tiker_temp$log_likelihood)
  return(s)
}


opt<-function(ticker){
  
res = optim(par = c(0.1,0.85),MLE,tiker = ticker,lower =c(0,0), method="L-BFGS-B",control=list(fnscale=-1))
print(res)
x = c(res$par)
x = c(x,var(ticker$return)*(1-x[1]-x[2]))
mmm <- garch(ticker,x[1],x[2],x[3])
return(mmm)

}


opt_leverage<-function(ticker){
  
  res = optim(par = c(0.1,0.85,0.000005,0.5),MLE_leverage,tiker = ticker,lower =c(0,0,0,0), method="L-BFGS-B",control=list(fnscale=-1))
  print(res)
  x = c(res$par)
  
  mmm <- garch_leverage(ticker,x[1],x[2],x[3],x[4])
  return(mmm)
  
}


#opt_leverage(MSFT)

x=c(0.016190,0.890790,1.30E-05,1.450219)
x =c(0.1,0.85,0.000005,0.5)
x =c(0,0,0,1)
jj<-garch_leverage(MSFT,0,0,0,1)

#jj<-garch(MSFT,0,0,0,1)

sum(jj$log_likelihood)

MLE_leverage(MSFT,x)


res = optim(par = c(0.1,0.85,0.000005,0.5),MLE_leverage,tiker = MSFT,lower =c(0,0,0,0),method="L-BFGS-B",control=list(trace=6,fnscale=-1))
print(res)


jj<-opt_leverage(MSFT)




#garch(1,1) with leverage effect
#question 4 


# #apply to all secuitties
# for (i in portfolio){
#   assign(i,opt_leverage(dates(returns(tik(i)))))
# }







#opt(MSFT)



# #garch(1,1) without leverage effect
# #question 3, variance targeting

# #apply to all secuitties
# for (i in portfolio){
#   assign(i,opt(dates(returns(tik(i)))))
# }




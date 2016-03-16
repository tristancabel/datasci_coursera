#step 1
dat=read.csv("seaflow_21min.csv")
summary(dat)
#2 synecho:18146
#3 fsc_small -> 3rd Qu.:39184

#step 2
library(caret)
set.seed(1234)
#paste(dat$file_id,    )
trainIndex<-createDataPartition(dat$cell_id, p=0.5, list=FALSE)
dat_train <- dat[trainIndex,]
dat_test <- dat[-trainIndex,]
#4 342.2

#step 3
library(ggplot2)
p <- ggplot(data=dat_train, aes(x=chl_small,y=pe, colour=pop))
p <- p + geom_point(size=2)
print(p)
#5 ultra mix with pico and nano

#step 4
library(rpart)
fol<-formula(pop ~ fsc_small+fsc_perp+fsc_big+pe+chl_small+chl_big)
model <- rpart(fol, method="class", data=dat_train)
print(model)
#6 crypto
#7 5006.5
#8 chl_small

#step 5
dat_test2<-subset(dat_test,select = -c(pop,file_id,time,cell_id,d1,d2 ))
test_predict<-predict(object=model, newdata=dat_test2, type="class", se.fit=TRUE)
sum(test_predict==dat_test$pop)/length(test_predict)
#9 0.8531144

#step 6
library(randomForest)
model_for <- randomForest(fol, data=dat_train)
test_predict_for<-predict(object=model_for, newdata=dat_test, type="class")
sum(test_predict_for==dat_test$pop)/length(test_predict_for)
 importance(model_for)
#10 0.9215946
#11 pe

#step 7
library(e1071)
model_svm <-svm(fol, data=dat_train)
test_predict_svm<-predict(object=model_svm, newdata=dat_test, type="class")
sum(test_predict_svm==dat_test$pop)/length(test_predict_svm)
#12 0.9207929

#step 8
accuracy<-sum(temp)/length(test_predict_svm)
table(pred=test_predict_svm, true=dat_test$pop)
#13 predic pico true ultra

#step 9
new_dat<-subset(dat,dat$file_id != 208)
#14 svm new accuracy 0.9719285 so dif 0.0503339
#15 fsc_big
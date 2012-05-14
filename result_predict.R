data<-read.csv(file="C:\\Users\\subhash\\Documents\\subhash\\interests\\C_Study\\Project\\whatdoyouknow\\grockit_all_data\\data.csv")
testdata<-read.csv(file="C:\\Users\\subhash\\Documents\\subhash\\interests\\C_Study\\Project\\whatdoyouknow\\grockit_all_data\\testdata.csv")
library(e1071)
svmmodel<-svm(correct~aveplayers_track+numentr_track+subtrack_name+game_type+track_name,type='C-classification',data=data[1:10000,])
pred<-predict(svmmodel,subset(testdata[1:10000,],select=-c(qsid_track,correct)))
tb<-table(pred,testdata[1:10000,]$correct)
error<-((tb[2]+tb[3])/sum(tb))*100
print(error)
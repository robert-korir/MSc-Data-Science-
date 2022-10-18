 x <- "Introduction to R"
 X = "DSA class"
 print(nchar(x))
 print(x)
 print(cat(x))
 #variable
 y <-30
 class(x)
 name <-"Robert"
 yob <-2015
 print(name)
 print(paste("Hello", name, ".Age:", 2022-yob,))
 #Numeric variables
 x<- 5.69
 z<-65L
 #Complex variables
 
 #Logical variables
 a<- TRUE
 #Strings
 s<- "Hello"
 nchars(s)
 #concatenate
 s<-"Hello"
 s1<-"Hello"
 s2<-"World"
 nchar(s1)
 print(cat(s1,s2))
 tolower(s1)
 s3<-substring(s1,0,2)
 s3
 
 
 a<- grepl("el", s1)
 print (grepl())
 
 
 help(print)
 grepl("Intro", x)
 x<-c2:23
 min(x)
 max(x)
 x = 30.4
 ceiling(x)
 #Functions
 x = function(){
   print("Monday 13th")
 }
 dsa()
 #OPERATORS
 #Arithmetic
 #Add
 b<-3+4
 b
 #Multiplication
 b<-3*4
 b
#Subtraction
 b<-3-4
 b
 #Division
 b<-4/3
 b
 #Modulus
 b<-5%%3
 b
 #Modified Modulus %%:quotient of a division
 b<-5%/%3
 b
 
 
 #ASSIGNMENT OPERATORS
 x<-3
 x=3
 3->x
 #Relational Operators
 x<-5
 y<-4
 x<=y #relational
 #Logical are used to combine 2 or more relational
 x<1
 x>5 #check if x is within 1-5
 x<1 && x>5 #&& -AND: all conditions have value of x TRUE
 x>1 || x<5 # || -OR:any condition TRUE
 !(x>1 || x<5)#used to negate the value TRUE to be FALSE and vise versa
 #Vector: a collection of elements of the same dataset
 x=23
 x2=45
 x40=67
 x=c(30.3,31.2,29.8,30.6)
 x
 mean(x)
 max(x)
 min(x)
 trunc(x)
 sqrt(x)
 floor(x)
 ceiling(x)
 #selection structures
 #1. if tests if 1condition is TRUE
 #2. if-else testing 1condition if TRUE,
 #3. if-else-if test more than 1condition
 #if-statement
 if(x>5){
   print("yes")#TRUE statement
   #if-else statement
   if(x<y){
     print("yes")
     else
       print("No")
     #if-else-if statement
     if (x<-5)
       y<-5
     print("yes")
     
       
   }
 }
 
 #Looping structures
 #repeats a block of statements as long as the condition remains TRUE
 #for-loop
 #while-loop
 #do-while loop
 #Problem:Print "hello" 5times
 x<-1
 x<=5 #1,2,3,4,5
 x<-x*2
 x>=-3#1,0,
 x
 #while-loop
 #Problem:Print "hello" 5times
 x<-1
 while(x<=5){
   print("Hello")#statement is repeated 5times
   x<-x*1
   
 }
 #special operator
 x<-1
 for (x in range(1:5,1)){
   print("hello")
 }
 
 a <-c(23,34,56,78)
 for(x in a){
   print("hello")
   print(x)
 }
 
 #FUNCTIONS
 #1. Library Functions e.g print,grepl,cat,mean,max etc.
 #2. User-defined Functions e.g created by own and do documentation e.g print("Hello)
 #?help
 #User-defined function
 #must have name,input(parameters),output(return value)
 myfunc <- function (a){
   if (a> 5){
     print(paste(a,"is greater than 5"))
     
   }
   else{
     print(paste(a,"is less than 5"))
     
   }
   return (a)
   #this function prints whatever the input is
   print(a)
  
   
   
 }
 myfunc("Hello")
 #Name: myfunc
 #Parameter:a
 #output:None
 #Calling /executing a function:name+arguments
 x<-myfunct(4)
 
 ?function
 
 #Exercise
 #problem:a program that displays all the even numbers from 0-100, display 
 x<-0
 x<=100
 x<-x+2#0,2,4,6,8
 x%%2==0# remainder is 0, it is even
 
 s<-0
 
 for (x in 0:100) {
   if (x %% 2 == 0) {# only TRUE if remainder is 0
     print(x)
     print(paste("Even number is :", x))
     s<-s+x
   }
 }
 return(s)
 print (paste(sum))
 
 
 
 
 
 
 
 
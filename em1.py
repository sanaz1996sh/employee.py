class Employee:
    emp = "municipality " 
    def __init__(self,n,f,pc,a,addr,sd,jp,an):
        self._name = n
        self._family = f
        self._personnel_code = pc
        self.age = a
        self.address = addr
        self.start_date = sd
        self.job_post = jp
        self._accont_number = an
    def chap(self):
        print(self._name +"|" + self._family +"|"+ self._personnel_code + "|" + self.age +"|" + self.address +"|" + self.start_date +"|" + self.job_post +"|" + self._accont_number)
class HourlyEmployee(Employee):
    def __init__(self,nwh,n,f,pc,a,addr,sd,jp,an):
        self.number_of_working_hours = nwh
        super().__init__(n,f,pc,a,addr,sd,jp,an)
    def chap(self):
         print (self.number_of_working_hours +"|"+ self._name +"|" + self._family +"|" + self._personnel_code + "|"+ self.age +"|" +self.address +"|" + self.start_date +"|" + self.job_post +"|" + self._accont_number)
         print (128*"=")
e1 = HourlyEmployee("work:4h a day","ali" , "akbari", "code:18161412" ,"age: 35" , "shahrekord" , "start date:1395/8/1" , "accountants" ,"accont number: 123456789")
print(e1.emp )
e1.chap()
e2 = HourlyEmployee("work:3h a day","reza" , "asgari", "code:52146379" ,"age: 30" , "shahrekord" , "start date:1400/5/1" , "accountants" ,"accont number: 147258369")
print(e2.emp )
e2.chap()
class MonthlyEmployee(Employee):
    def __init__(self,ms,n,f,pc,a,addr,sd,jp,an):
        self.monthly_salary = ms
        super().__init__(n,f,pc,a,addr,sd,jp,an) 
    def chap(self):
        print (self.monthly_salary +"|"+ self._name +"|" + self._family +"|" + self._personnel_code +"|" + self.age +"|" + self.address +"|" + self.start_date +"|" + self.job_post +"|" + self._accont_number)
        print (128*"=")
e3 =  MonthlyEmployee("salary:15000000ml monthly" , "parisa" , "ahmadi" ,"code:19171531" ,"age: 38 ", "sharekord" , "1393/10/1" , "software engineering" ,"accont number: 987654321")
print(e3.emp )
e3.chap()
e4 =  MonthlyEmployee("salary:10000000ml monthly" , "azar" , "bahrami" ,"code:98756264" ,"age: 29 ", "sharekord" , "1401/10/1" , "software engineering" ,"accont number: 456123789")
print(e4.emp)
e4.chap()
      




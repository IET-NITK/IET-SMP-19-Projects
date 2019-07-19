class Time(object):
    def __init__(self,hour,mins):
        assert hour>=0 and mins<=59 and mins>=0 ,"Invalid time entered"
        self.hour=hour
        self.mins=mins
    def __str__(self):
        return str(self.hour)+":"+str(self.mins)
    def __add__(self,other):
        ans_hour=self.hour+other.hour
        if (self.mins+other.mins)>60:
            ans_hour+=(self.mins+other.mins)//60
        ans_mins=(self.mins+other.mins)%60
        return Time(ans_hour,ans_mins)
    def displayTime(self):
        print (str(self.hour)+":"+str(self.mins))
    def DisplayMinute(self):
        return self.hour*60+self.mins
    
        
        
        
        
        
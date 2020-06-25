class TuningVariable:
    def __init__(self):
        self.Kp = 0
        self.N_threshold = 0 #default
        self.Amax = 45 #default        
        self.deltaMax = 90
        self.deltaMin = -90

    def getVariables():
        return (self.Kp,self.N_threshold,self.Amax, self.deltaMax, self.deltaMin)







        
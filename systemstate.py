class SystemState():
    def __init__(self):
        print("Starting the node")

    def setGpsVariables(data):
        self.lat = data.lat
        self.lon = data.lon
        self.hour = data.hh
        self.minute = data.mm
        self.second = data.ss
    
    def setAngleVariables(data):
        self.Wrel = data.Wrel
        self.RigAngle = data.RigAngle
        self.RudderAngle = data.RudderAngle
        self.AAngle = data.AAngle
    
    def getControlVariables():
        return (self.lat,self.lon,self.Wrel,self.RigAngle,self.RudderAngle,self.AAngle)


    def getPsi(wpLat,wpLon):
        psi = 123456
        return psi

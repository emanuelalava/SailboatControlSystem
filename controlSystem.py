#!/usr/bin/env python

import rospy
from sensailor.msg import gps
from sensailor.msg import angle
from sensailor.msg import servoControl

from systemstate import SystemState
from tuningvariables import TuningVariable
from controlvariables import ControlVariable
def initNode():
    rospy.init_node("ControlSystem",anonymous=True)

def initSub(TOPIC,MSG_TYPE,CALLBACK):
    rospy.Subscriber(TOPIC,MSG_TYPE,CALLBACK)
    rospy.spin()

def gpsCallback(data):
    State.setGpsVariables(data)
    #initControl()
def angleVariable(data):
    State.setAngleVariables(data)
    initControl()

def initPub(TOPIC,MSG_TYPE,QUEVE_SIZE):
    pub = rospy.Publisher(TOPIC,MSG_TYPE,QUEVE_SIZE)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        msg = servoControl()
        msg.rigAngle = controlVariable.rigangle
        msg.rudderAngle controlVariable.rudderangle
        pub.publish(msg)
        rate.sleep()


def initControl():
    currentLat,currentLon,currentWrel,currentRigAngle,currentRudderAngle,AAngle = State.getControlVariables()
    Kp,N_threshold,Amax,deltaMax, deltaMin = Tune.getVariables()
    
    waypointLat = 000000000
    waypointLon = 000000000
    psi = State.getPsi()
    psiRef = State.getPsiRef()

    error = psiRef - psi

    Ndes = Kp*error #pertenece [-1,1]

    delta = (0.5)*Ndes*(deltaMax-deltaMin)

    epsilon = abs(Ndes)-abs(N_threshold) # pertenece a [0,1]

    windDirection = (currentWrel>=0) and (currentWrel<180) # True for Right (Starboard tack) False for Left (Port tack)

    isPositive = Ndes>0

    #xor = ((starboardTack) and (not isPositive)) or ((not starboardTack) and (isPositive))
    Amoment = epsilon*Amax #*xor

    if (windDirection) and (isPositive):
        Amoment*=-1
    #elif (windDirection) and (not isPositive):
    #    pass
    #elif (not windDirection) and (isPositive):
    #    pass
    elif (not windDirection) and (not isPositive):
        Amoment*=-1
    
    Atotal = AAngle + Amoment



    #Values to send to servos

    controlVariable.setControlVariable(Atotal,delta)

if __name__ == '__main__':
    State = SystemState()
    controlVariable = ControlVariable()
    Tune = TuningVariable()
    initNode()
    initSub("gps_data",gps,gpsCallback)
    initSub("angle_data",angle,angleCallback)
    initPub("servo_data",servoControl,10)

    
"""This is my first attempt at writing an alarm clock program. We'll see how it
goes!
"""
import time

class alarm_motif(object):
  def __init__(self, motif_no):
    self.motif_no = motif_no
  def alarm():

class alarm_motif_one(alarm_motif):
  def __init__(self):
    pass
  def alarm():
    

def alarm_on():
#time is all in military time!"""
  while True:
    #sleep for 10 seconds, then check the time again"""
    time.sleep(10)
    #get the localtime
    current_hour = time.localtime().tm_hour
    current_min = time.localtime().tm_min
    """open the waketime.txt file and read the alarm times. If an alarm time is
    within __ seconds of the current time, read the rest of the file and run the
    alarm as described in the file.
    """
    with open("waketimes.txt","r") as waketimes:
      #open the file, do stuff, then close it.
      while waketimes.readline != "END":
        

"""
"""

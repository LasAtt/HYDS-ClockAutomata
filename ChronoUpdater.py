import threading
import time

class ChronoUpdater:

  def __init__(self, g):
    self.g = g
    self.on = False
    self.visible = False
    threading.Thread(target = self.updater).start()

  def updater(self):
    while(True): 
      if self.on:
        self.g.increaseChronoByOne()
        if self.visible:
          self.g.refreshChronoDisplay()
        time.sleep(0.25)

  def start(self):
    self.on = True

  def stop(self):
    self.on = False

  def show(self):
    self.visible = True

  def hide(self):
    self.visible = False
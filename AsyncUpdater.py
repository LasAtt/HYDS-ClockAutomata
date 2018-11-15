import threading
import time

class AsyncUpdater:

  def __init__(self, func, visibleFunc, interval):
    self.func = func
    self.visibleFunc = visibleFunc
    self.interval = interval
    self.on = False
    self.visible = False
    threading.Thread(target = self.updater).start()

  def updater(self):
    while(True): 
      if self.on:
        self.func()
        if self.visible:
          self.visibleFunc()
        time.sleep(self.interval)

  def start(self):
    self.on = True

  def stop(self):
    self.on = False

  def show(self):
    self.visible = True

  def hide(self):
    self.visible = False
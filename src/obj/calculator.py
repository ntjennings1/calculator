import tkinter as tk

from obj.controller import Controller
from obj.viewer import Viewer

class Calculator():
  """ 
    A class representation of a calculator.

    ```
    Attributes
    ----------
    root : The calculators tk application
    controller : The calculators controller
    viewer : The calulators viewer
  """

  """ Initialize class instance. """
  def __init__(self): 
    self.root = tk.Tk()
    self.controller = None
    self.viewer = None

  """ Return root.

  @return root : The calculators app
  @rtype root : tk.Tk()
  """
  def get_root(self):
    return self.root

  """ Set root. 

  @param root : The calculators app
  @type root : tk.Tk()
  """
  def set_root(self, root):
    self.root = root

  """ Returns the calculators controller.

  @return controller : The calculators controller
  @rtype controller : tk.Frame
  """
  def get_controller(self):
    return self.controller

  """ Sets the calculators controller. 

  @param controller : The apps controller
  @type controller : tk.Frame
  """
  def set_controller(self, controller):
    self.controller = controller

  """ Returns the calculators viewer.

  @return viewer : The calculators viewer
  @rtype viewer : tk.Frame
  """
  def get_viewer(self):
    return self.viewer

  """ Sets the calculators viewer.

  @param viewer : The calculators viewer
  @type viewer : tk.Frame
  """
  def set_viewer(self, viewer):
    self.viewer = viewer

  """ Fills the calculator.

  @return null
  """
  def fill(self):
    #self.get_root().geometry('400x400')
    self.set_viewer(Viewer(self.get_root()))
    self.set_controller(Controller(self.get_root(), self))

  """ Runs the calculator. 

  @return null
  """
  def run(self):

    self.fill()

    self.get_root().mainloop()

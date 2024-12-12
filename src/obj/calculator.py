""" Native imports. """
import tkinter as tk

""" Class imports. """
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

    ```
    Methods
    -------
    customize : Customizes the calculator
    fill : Fills the calculator with corresponding components
    run : Starts the calculator application
  """

  """ Initialize class instance. """
  def __init__(self): 
    self.root = tk.Tk()
    self.controller = None
    self.viewer = None

  """ Returns the calculators root.

  @return root : The calculators app
  @rtype root : tk.Tk()
  """
  def get_root(self):
    return self.root

  """ Sets the calculators root. 

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

  """ Fills the calculators with its components.

  @return null
  """
  def fill(self):
    self.set_viewer(Viewer(self.get_root()))
    self.set_controller(Controller(self.get_root(), self))

  """ Customizes the calculator.
  
  @return null
  """
  def customize():
    #self.get_root().geometry('400x400')
    pass

  """ Starts the calculator application. 

  @return null
  """
  def run(self):

    self.customize()
    self.fill()
    self.get_root().mainloop()

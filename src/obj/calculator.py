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
    nviewer : The calulators new viewer
    pviewer : The calculators previous viewer
    
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
    self.nviewer = None
    self.pviewer = None

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
  def get_nviewer(self):
    return self.viewer

  """ Sets the calculators viewer.

  @param viewer : The calculators viewer
  @type viewer : tk.Frame
  """
  def set_nviewer(self, viewer):
    self.viewer = viewer

  """ Returns the calculators viewer.

  @return viewer : The calculators viewer
  @rtype viewer : tk.Frame
  """
  def get_pviewer(self):
    return self.pviewer

  """ Sets the calculators viewer.

  @param viewer : The calculators viewer
  @type viewer : tk.Frame
  """
  def set_pviewer(self, pviewer):
    self.pviewer = pviewer

  """ Fills the calculators with its components.

  @return null
  """
  def fill(self):
    self.set_nviewer(Viewer(self.get_root()))
    self.set_pviewer(Viewer(self.get_root()))
    self.set_controller(Controller(self.get_root(), self))

  """ Customizes the calculator.
  
  @return null
  """
  def customize(self):

    self.get_pviewer().place(0,0)
    self.get_pviewer().get_view().configure(width=50, anchor='e', font=('Arial', 7))
    
    self.get_nviewer().place(1,0)
    self.get_nviewer().get_view().configure(width=30, anchor='e', font=('Arial', 15))
    
    self.get_controller().place(2,0)

  """ Starts the calculator application. 

  @return null
  """
  def run(self):

    self.fill()
    self.customize()
    self.get_root().mainloop()

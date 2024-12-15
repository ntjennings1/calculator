""" Native imports. """
import tkinter as tk 

class Viewer(tk.Frame):
  """
  A class representation of a calculator.

  ```
  Attributes
  ----------
  view : The viewers view window

  ```
  Methods
  -------
  customize : Customizes the viewer
  place : Places the viewer on the calculator
  update : Updates the viewer
  """

  """ Initialize the class instance.
  
  @param master : Calculator application root
  @type master : tk.Tk()
  """
  def __init__(self, master):
    super().__init__(master)
    self.view = None

    self.customize()

  """ Returns the viewers view.

  @return view : The viewers view
  @rtype view : 
  """
  def get_view(self):
    return self.view

  """ Sets the viewers view.

  @param view : The viewers view
  @type view : 
  """
  def set_view(self, view):
    self.view = view

  """ Updates the view with new text.

  @param updates : The views updates
  @type updates : str
  """
  def update(self, updates):
    self.get_view().config(text=updates)

  """ Customizes the viewer.

  @return null
  """
  def customize(self):
    self.set_view(tk.Label(self, text=''))
    self.get_view().grid(row=0, column=0, padx=15)

  """ Places the viewer on the calculator.

  @return null
  """
  def place(self, row, col):
    self.grid(row=row, column=col)


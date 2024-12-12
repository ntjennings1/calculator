import tkinter as tk 

class Viewer(tk.Frame):
  """ Defines the initalize function. """
  def __init__(self, master):
    super().__init__(master)
    self.view = None
    self.text = "" 

    self.customize()
    self.place()

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

  """ Returns the views text content.

  @return text : The viewers text content
  @rtype text : str
  """
  def get_text(self):
    return self.text

  """ Sets the viewers text content.

  @param text : The viewers text content
  @type text : str
  """
  def set_text(self, text):
    self.text = text

  """ Updates the view.

  @param updates : The views updates
  @type updates : str
  """
  def update(self, updates):
    self.get_view().config(text=updates)

  """ Customizes the viewer.

  @return null
  """
  def customize(self):
    self.set_view(tk.Label(self, text=self.get_text()))
    self.get_view().grid(row=0, column=0, padx=15, pady=15)

  """ Places the viewer.

  @return null
  """
  def place(self):
    self.grid(row=0, column=0)


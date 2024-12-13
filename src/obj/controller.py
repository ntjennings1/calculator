""" Native imports. """
import tkinter as tk
import ast

class Controller(tk.Frame):
  """
  A class representation of a calculator controller.

  ```
  Attributes
  ----------
  calc : The controllers calculator
  num_buttons : The controllers number buttons
  op_buttons : The controllers operation buttons
  equation : The controllers input equation

  ```
  Methods
  -------
  customize : Customized the controller
  place : Places the controller on the calculator
  add_buttons : Adds all the controllers buttons
  place_num_buttons : Places the number buttons on the controller
  place_op_buttons : Places the operation buttons on the controller
  clear : Clears the input equation
  delete : Deleted the last character in the equation
  swap : Swaps the polarity of the last variable in the equation 
  search : Searches for the last variable in the input equation
  check : Checks the user input character for possible errors
  equate : Solves the input equation
  """

  """ Initialize the class instance.

  @param master : Calculator application root
  @type master : tk.Tk()

  @param calc : The calculator
  @type calc : Object.class
  """
  def __init__(self, master, calc):
    super().__init__(master)
    self.calc = calc
    self.num_buttons = []
    self.op_buttons = []
    self.equation = ""

    self.customize()
    self.place()

  """ Returns the controllers calculator.

  @returns calc : The controllers calculator
  @rtype calc : Object
  """
  def get_calc(self):
    return self.calc

  """ Sets the controllers calculator.

  @param calc : The controllers calculator
  @type calc : Object
  """
  def set_calc(self, calc):
    self.calc = calc

  """ Returns the controllers number buttons.

  @return num_buttons : The controllers number buttons
  @rtype num_buttons : list
  """
  def get_num_buttons(self):
    return self.num_buttons

  """ Sets the controllers number buttons.

  @param num_buttons : The controllers number buttons
  @type num_buttons : list
  """
  def set_num_buttons(self, num_buttons):
    self.num_buttons = num_buttons

  """ Returns the controllers operation buttons.

  @return op_buttons : The controllers operation buttons
  @rtype op_buttons : list
  """
  def get_op_buttons(self):
    return self.op_buttons

  """ Sets the controllers operation buttons.

  @param op_buttons : The controllers operation buttons
  @type op_buttons : list
  """
  def set_op_buttons(self, op_buttons):
    self.op_buttons = op_buttons

  """ Returns the controllers equation.

  @return equation : The controllers equation
  @rtype equation : str
  """
  def get_equation(self):
    return self.equation

  """ Sets the controllers equation.

  @param equation : The controllers equation
  @type equation : str
  """
  def set_equation(self, equation):
    self.equation = equation

  """ Checks the input character for possible errors.

  @param var : The input character
  @type var : str
  """
  def check(self, var):

    ops = ['+', '-', '/', '*', '**', '.'] 
    par = ['(', ')']
    last = None 

    if len(self.get_equation()) == 0:
      pass
    else:
      last= str(self.get_equation()[len(self.get_equation()) - 1])
      if var in ops:
        if str(var) == last:
          pass
        elif last in ops:
          pass
        else:
          self.press(str(var))
      elif var in par:
        if str(var) == '(':
          if last not in ops:
            self.press('*' + str(var))
          else:
            self.press(str(var))
        elif str(var) == ')':
          if last not in ops:
            self.press(str(var))


  """ Callback to add to controllers equation.

  @param var : The input char
  @type var : str
  """
  def press(self, var):
    self.set_equation(self.get_equation() + var)
    self.get_calc().get_viewer().update(self.get_equation())

  """ Clears the controllers equation.

  @return null
  """
  def clear(self):
    self.set_equation("")
    self.get_calc().get_viewer().update(self.get_equation())

  """ Finds the last variable.
  
  @return null
  """
  def search(self):
    pass

  """ Swaps the polarity of the last variable.

  @return null
  """
  def swap(self):
    pass

  """ Delete the last character in the equation.
  
  @return null
  """
  def delete(self):
    if len(self.get_equation()) > 0:
      self.set_equation(self.get_equation()[:-1])
      self.get_calc().get_viewer().update(self.get_equation())
    else:
      pass

  """ Solves the input equation.

  @return null
  """
  def equate(self):
    if len(self.get_equation()) > 0:
      try:
        eq = ast.parse(self.get_equation(), mode='eval')
        sol = eval(compile(eq, '<string>', 'eval'))
        self.get_calc().get_viewer().update(sol)
        self.set_equation(str(sol))
      except Exception as ex: 
        self.clear()
        self.get_calc().get_viewer().update('Err')
    else:
      pass
    
  """ Places controller operation buttons in grid.

  @return null
  """
  def place_op_buttons(self):
    row = 0
    col = 0
    for b in self.get_op_buttons():
      if row % 5 == 0:
        row = 0 
        col += 1
      b.grid(row=row, column=col)
      row += 1

  """ Places controller number buttons in grid.

  @return null
  """
  def place_num_buttons(self):
    row = 0 
    col = 0 

    for b in self.get_num_buttons():
      if col % 3 == 0 and col > 0:
        row += 1 
        col = 0
      b.grid(row=row, column=col+3)
      col += 1

  """ Adds buttons to the controller.

  @return null
  """
  def add_buttons(self):
    button0 = tk.Button(self, text="0", command=lambda: self.press('0'), width='5')
    button1 = tk.Button(self, text="1", command=lambda: self.press('1'), width='5')
    button2 = tk.Button(self, text="2", command=lambda: self.press('2'), width='5')
    button3 = tk.Button(self, text="3", command=lambda: self.press('3'), width='5')
    button4 = tk.Button(self, text="4", command=lambda: self.press('4'), width='5')
    button5 = tk.Button(self, text="5", command=lambda: self.press('5'), width='5')
    button6 = tk.Button(self, text="6", command=lambda: self.press('6'), width='5')
    button7 = tk.Button(self, text="7", command=lambda: self.press('7'), width='5')
    button8 = tk.Button(self, text="8", command=lambda: self.press('8'), width='5')
    button9 = tk.Button(self, text="9", command=lambda: self.press('9'), width='5')

    minus_button = tk.Button(self, text="-", command=lambda: self.check('-'), width='5')
    plus_button = tk.Button(self, text="+", command=lambda: self.check('+'), width='5')
    mult_button = tk.Button(self, text="*", command=lambda: self.check('*'), width='5')
    div_button = tk.Button(self, text="/", command=lambda: self.check('/'), width='5')
    lpar_button = tk.Button(self, text="(", command=lambda: self.check('('), width='5')
    rpar_button = tk.Button(self, text=")", command=lambda: self.check(')'), width='5')
    exp_button = tk.Button(self, text="^", command=lambda: self.check('**'), width='5')

    deci_button = tk.Button(self, text=".", command=lambda: self.check('.'), width='5')
    blank_button = tk.Button(self, text=" ", state=tk.DISABLED, width='5')
    clear_button = tk.Button(self, text="C", command=self.clear, width='5')
    equate_button = tk.Button(self, text="=", command=self.equate, width='5')
    delete_button = tk.Button(self, text='<x', command=self.delete, width='5')
    swap_button = tk.Button(self, text="+/-", command=self.swap, width='5')

    self.get_num_buttons().append(button7)
    self.get_num_buttons().append(button8)
    self.get_num_buttons().append(button9)
    self.get_num_buttons().append(button4)
    self.get_num_buttons().append(button5)
    self.get_num_buttons().append(button6)
    self.get_num_buttons().append(button1)
    self.get_num_buttons().append(button2)
    self.get_num_buttons().append(button3)
    self.get_num_buttons().append(blank_button)
    self.get_num_buttons().append(button0)
    self.get_num_buttons().append(deci_button)
    self.get_num_buttons().append(equate_button)


    self.get_op_buttons().append(minus_button)
    self.get_op_buttons().append(mult_button)
    self.get_op_buttons().append(exp_button)
    self.get_op_buttons().append(lpar_button)
    self.get_op_buttons().append(swap_button)

    self.get_op_buttons().append(plus_button)
    self.get_op_buttons().append(div_button)
    self.get_op_buttons().append(rpar_button)
    self.get_op_buttons().append(clear_button)
    self.get_op_buttons().append(delete_button)

    self.place_num_buttons()
    self.place_op_buttons()

  """ Customizes the controller.

  @return null
  """
  def customize(self):
    self.add_buttons()

  """ Places the controller on the calculator.

  @return null
  """
  def place(self):
    self.grid(row=1, column=0)

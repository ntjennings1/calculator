""" Native imports. """
import os
import time
import tkinter as tk
import ast
import sqlite3

class Controller(tk.Frame):
  """
  A class representation of a calculator controller.

  ```
  Attributes
  ----------
  calc : The controllers calculator
  db : The controllers database
  db_path : The path to the controllers database
  num_buttons : The controllers number buttons
  op_buttons : The controllers operation buttons
  equation : The controllers input equation
  previous_equations : The controllers previous input equations
  index : The controllers scroll index
  travelling : The controllers travelling status

  ```
  Methods
  -------
  close : Closes the application
  customize : Customized the controller
  place : Places the controller on the calculator
  connect : Connect to database and creates a data table
  add_buttons : Adds all the controllers buttons
  place_num_buttons : Places the number buttons on the controller
  place_op_buttons : Places the operation buttons on the controller
  clear : Clears the input equation
  delete : Deleted the last character in the equation
  swap : Swaps the polarity of the last variable in the equation 
  search : Searches for the last variable in the input equation
  check : Checks the user input character for possible errors
  equate : Solves the input equation
  up : Scrolls upward through previous equations
  down : Scrolls downward through previous equations
  querry : Querries through database table for previous entries
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
    self.previous_equations = None
    self.index = 0
    self.travelling = False
    self.db = None
    self.db_path=''

    self.connect()
    self.customize()

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

  """ Returns the controllers previous equations.
  
  @return previous_equation : The controllers previous equations
  @rtype previous_equation : list
  """
  def get_previous_equations(self):
    return self.previous_equations
  
  """ Sets the controllers previous equations
  
  @param previous_equation : The controllers previous equations
  @type previous_equations : list
  """
  def set_previous_equations(self, previous_equations):
    self.previous_equations = previous_equations

  """ Returns the controllers current index.
  
  @return index : The controllers current index
  @rtype index : int
  """
  def get_index(self):
    return self.index
  
  """ Sets the controllers current index.
  
  @param index : The controllers current index
  @type index : int
  """
  def set_index(self, index):
    self.index = index

  """ Returns the controllers travelling status.
  
  @return travelling : The controllers travelling status
  @rtype travelling : boolean
  """
  def get_travelling(self):
    return self.travelling
  
  """ Sets the controllers travelling status.
  
  @param travelling : The controllers travelling status
  @type travelling : boolean
  """
  def set_travelling(self, travelling):
    self.travelling = travelling

  """ Returns the controllers database.
  
  @return db : The controllers database
  @rtype db : sqlite3.connect
  """
  def get_db(self):
    return self.db
  
  """ Sets the controllers database.
  
  @param db : The controllers database
  @type db : sqlite3.connect
  """
  def set_db(self, db):
    self.db = db

  """ Returns the controllers database path.
  
  @return db : The controllers database path
  @rtype db : str
  """
  def get_db_path(self):
    return self.db_path
  
  """ Sets the controllers database path.
  
  @param db_path : The controllers database path
  @type db_path : str
  """
  def set_db_path(self, db_path):
    self.db_path = db_path

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
    self.get_calc().get_nviewer().update(self.get_equation())

  """ Clears the controllers equation.

  @return null
  """
  def clear(self):
    self.set_travelling(False)
    self.set_equation("")
    self.get_calc().get_nviewer().update(self.get_equation())
    self.get_calc().get_pviewer().update(self.get_previous_equations()[len(self.get_previous_equations())-1])

  """ Closes the application.
  
  @return null
  """
  def close(self):
    try:
      self.get_calc().get_root().quit()
      self.get_calc().get_root().destroy()
      self.get_db().commit()
      self.get_db().close()
      exit()
    except Exception as ex:
      print('Error closing calculator.')

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
      self.get_calc().get_nviewer().update(self.get_equation())
    else:
      pass

  """ Scrolls upward in previous equations. 
  
  @return null
  """
  def up(self):
    
    if len(self.get_previous_equations()) > 0:

      if not self.get_travelling():
        self.set_index(len(self.get_previous_equations())-1)
        self.set_equation(self.get_previous_equations()[self.get_index()])
        self.get_calc().get_nviewer().update(self.get_previous_equations()[self.get_index()])
        if len(self.get_previous_equations()) == 1:
          self.get_calc().get_pviewer().update('')
        else:
          self.get_calc().get_pviewer().update(self.get_previous_equations()[self.get_index()-1])
        self.set_travelling(True)

      elif self.get_travelling():
        if self.get_index() > 0:
          self.set_index(self.get_index()-1)
          self.set_equation(self.get_previous_equations()[self.get_index()])
          self.get_calc().get_nviewer().update(self.get_previous_equations()[self.get_index()]) 
          if self.get_index()-1 >= 0:
            self.get_calc().get_pviewer().update(self.get_previous_equations()[self.get_index()-1])   
          else:
            self.get_calc().get_pviewer().update('') 

  """ Scrolls downward in previous equations.
  
  @return null
  """
  def down(self):
    
    if self.get_index() <= len(self.get_previous_equations())-1:
      
      if self.get_travelling():
        if self.get_index()+1 < len(self.get_previous_equations()):
          self.set_index(self.get_index()+1)
          self.set_equation(self.get_previous_equations()[self.get_index()])
          self.get_calc().get_nviewer().update(self.get_previous_equations()[self.get_index()])
          self.get_calc().get_pviewer().update(self.get_previous_equations()[self.get_index()-1])

  """ Solves the input equation.

  @return null
  """
  def equate(self):
    if len(self.get_equation()) > 0:
      try:
        eq = ast.parse(self.get_equation(), mode='eval')

        self.get_db().cursor().execute("INSERT INTO previous_table (content) VALUES (?)", (self.get_equation(),) )
        self.get_db().commit()

        sol = eval(compile(eq, '<string>', 'eval'))
        self.get_calc().get_nviewer().update(sol)
        self.set_equation(str(sol))

        self.set_travelling(False)
        self.querry()
        time.sleep(0)

      except Exception as ex:
        print(ex)
        self.clear()
        self.get_calc().get_nviewer().update('Err')
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
    font = ('Arial', 14)
    button0 = tk.Button(self, text="0", command=lambda: self.press('0'), width='5', bg='orange', font=font)
    button1 = tk.Button(self, text="1", command=lambda: self.press('1'), width='5', bg='orange', font=font)
    button2 = tk.Button(self, text="2", command=lambda: self.press('2'), width='5', bg='orange', font=font)
    button3 = tk.Button(self, text="3", command=lambda: self.press('3'), width='5', bg='orange', font=font)
    button4 = tk.Button(self, text="4", command=lambda: self.press('4'), width='5', bg='orange', font=font)
    button5 = tk.Button(self, text="5", command=lambda: self.press('5'), width='5', bg='orange', font=font)
    button6 = tk.Button(self, text="6", command=lambda: self.press('6'), width='5', bg='orange', font=font)
    button7 = tk.Button(self, text="7", command=lambda: self.press('7'), width='5', bg='orange', font=font)
    button8 = tk.Button(self, text="8", command=lambda: self.press('8'), width='5', bg='orange', font=font)
    button9 = tk.Button(self, text="9", command=lambda: self.press('9'), width='5', bg='orange', font=font)

    minus_button = tk.Button(self, text="-", command=lambda: self.check('-'), width='5', font=font)
    plus_button = tk.Button(self, text="+", command=lambda: self.check('+'), width='5', font=font)
    mult_button = tk.Button(self, text="*", command=lambda: self.check('*'), width='5', font=font)
    div_button = tk.Button(self, text="/", command=lambda: self.check('/'), width='5', font=font)
    lpar_button = tk.Button(self, text="(", command=lambda: self.check('('), width='5', font=font)
    rpar_button = tk.Button(self, text=")", command=lambda: self.check(')'), width='5', font=font)
    exp_button = tk.Button(self, text="^", command=lambda: self.check('**'), width='5', font=font)

    deci_button = tk.Button(self, text=".", command=lambda: self.check('.'), width='5', bg='orange', font=font)
    blank_button = tk.Button(self, text=" ", state=tk.DISABLED, width='5', bg='orange', font=font)
    clear_button = tk.Button(self, text="C", command=self.clear, width='5', font=font)
    equate_button = tk.Button(self, text="=", command=self.equate, width='5', font=font)
    delete_button = tk.Button(self, text='<', command=self.delete, width='5', font=font)
    exit_button = tk.Button(self, text="EXIT", command=self.close, width='5', font=font)
    up_button = tk.Button(self, text="\u2191", command=self.up, width='5', font=font)
    down_button = tk.Button(self, text=" \u2193", command=self.down, width='5', font=font)

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
    self.get_num_buttons().append(up_button)
    self.get_num_buttons().append(down_button)


    self.get_op_buttons().append(minus_button)
    self.get_op_buttons().append(mult_button)
    self.get_op_buttons().append(exp_button)
    self.get_op_buttons().append(lpar_button)
    self.get_op_buttons().append(exit_button)

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
  def place(self, row, col):
    self.grid(row=row, column=col)

  """ Querries the controllers database for previous equations.
  
  @return null
  """
  def querry(self):
    cursor = self.get_db().cursor()
    cursor.execute("SELECT * FROM previous_table")
    
    rows=[]
    for i in cursor.fetchall():
        rows.append(i[0])

    self.set_previous_equations(rows)
    self.get_calc().get_pviewer().update(self.get_previous_equations()[-1])
    cursor.close()

  """ Connects to database and creates table.
  
  @return null
  """
  def connect(self):
    
    try:
      root_dir = os.path.dirname(os.path.abspath(__file__))
      self.set_db_path(os.path.join(root_dir, r'../data/data.db'))
      create_command = """
        CREATE TABLE previous_table (
          content TEXT NOT_NULL
        )
      """
      self.set_db(sqlite3.connect(self.get_db_path()))
      self.get_db().execute('DROP TABLE IF EXISTS previous_table')
      self.get_db().execute(create_command)
    except Exception as ex:
      print('Error connecting to database')
      self.close()
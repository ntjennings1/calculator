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
		self.zed_button = None
		self.one_button = None
		self.two_button = None
		self.three_button = None
		self.four_button = None
		self.five_button = None
		self.six_button = None
		self.seven_button = None
		self.eight_button = None
		self.nine_button = None
		self.deci_button = None
		self.blank_button = None

		self.op_buttons = []
		self.clear_button = None
		self.eq_button = None
		self.lpar_button = None
		self.rpar_button = None
		self.plus_button = None
		self.minus_button = None
		self.mult_button = None
		self.div_button = None
		self.exp_button = None
		self.mod_button = None
		self.fact_button = None
		self.sin_button = None
		self.cos_button = None
		self.tan_button = None
		self.back_button = None
		self.up_button = None
		self.down_button = None
		self.exit_button = None

		self.equation = ""
		self.previous_equations = []
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

	def add_num_button(self, num_button):
		self.get_num_buttons().append(num_button)

	def get_zed_button(self):
		return self.zed_button

	def set_zed_button(self, zbutton):
		self.zed_button = zbutton

	def get_one_button(self):
		return self.one_button

	def set_one_button(self, one_button):
		self.one_button = one_button

	def get_two_button(self):
		return self.two_button

	def set_two_button(self, two_button):
		self.two_button = two_button

	def get_three_button(self):
		return self.three_button

	def set_three_button(self, three_button):
		self.three_button = three_button

	def get_four_button(self):
		return self.four_button

	def set_four_button(self, four_button):
		self.four_button = four_button

	def get_five_button(self):
		return self.five_button

	def set_five_button(self, five_button):
		self.five_button = five_button

	def get_six_button(self):
		return self.six_button

	def set_six_button(self, six_button):
		self.six_button = six_button

	def get_seven_button(self):
		return self.seven_button

	def set_seven_button(self, seven_button):
		self.seven_button = seven_button

	def get_eight_button(self):
		return self.eight_button

	def set_eight_button(self, eight_button):
		self.eight_button = eight_button

	def get_nine_button(self):
		return self.nine_button

	def set_nine_button(self, nine_button):
		self.nine_button = nine_button

	def get_deci_button(self):
		return self.deci_button

	def set_deci_button(self, deci_button):
		self.deci_button = deci_button

	def get_blank_button(self):
		return self.blank_button

	def set_blank_button(self, blank_button):
		self.blank_button = blank_button

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

	def add_op_button(self, op_button):
		self.get_op_buttons().append(op_button)

	def get_clear_button(self):
		return self.clear_button

	def set_clear_button(self, clear_button):
		self.clear_button = clear_button

	def get_eq_button(self):
		return self.eq_button

	def set_eq_button(self, eq_button):
		self.eq_button = eq_button

	def get_lpar_button(self):
		return self.lpar_button

	def set_lpar_button(self, lpar_button):
		self.lpar_button = lpar_button

	def get_rpar_button(self):
		return self.rpar_button

	def set_rpar_button(self, rpar_button):
		self.rpar_button = rpar_button

	def get_plus_button(self):
		return self.plus_button

	def set_plus_button(self, plus_button):
		self.plus_button = plus_button

	def get_minus_button(self):
		return self.minus_button

	def set_minus_button(self, minus_button):
		self.minus_button = minus_button

	def get_mult_button(self):
		return self.mult_button

	def set_mult_button(self, mult_button):
		self.mult_button = mult_button

	def get_div_button(self):
		return self.div_button

	def set_div_button(self, div_button):
		self.div_button = div_button

	def get_exp_button(self):
		return self.exp_button

	def set_exp_button(self, exp_button):
		self.exp_button = exp_button

	def get_mod_button(self):
		return self.mod_button

	def set_mod_button(self, mod_button):
		self.mod_button = mod_button

	def get_back_button(self):
		return self.back_button

	def set_back_button(self, back_button):
		self.back_button = back_button

	def get_up_button(self):
		return self.up_button

	def set_up_button(self, up_button):
		self.up_button = up_button

	def get_down_button(self):
		return self.down_button

	def set_down_button(self, down_button):
		self.down_button = down_button

	def get_exit_button(self):
		return self.exit_button

	def set_exit_button(self, exit_button):
		self.exit_button = exit_button

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

	def throw_exec(self, mes):

		if (mes == 'cust'):
			print('[!] Error customizing controller.') 
		elif (mes == 'close'):
			print('[!] Error closing calculator.')

	""" Checks the input character for possible errors.

	@param var : The input character
	@type var : str
	"""
	def check(self, var):

		ops = ['+', '-', '/', '*', '**', '.', '%']
		par = ['(', ')']
		last = None

		if (len(self.get_equation()) == 0):
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
		if (len(self.get_previous_equations()) > 0):
			self.get_calc().get_pviewer().update(self.get_previous_equations()[len(self.get_previous_equations())-1])

	""" Closes the application.

	@return null
	"""
	def close(self):
		try:
			print('[!] Calculator shutdown.')
			self.get_calc().get_root().destroy()
			os._exit(0)
		except Exception as ex:
			self.throw_exec('close')

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
				if (self.get_index()+1 < len(self.get_previous_equations())):
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

	""" Customizes the controller.

	@return null
	"""
	def customize(self):
		try:
			font = ('Courier New', 20)

			# Number buttons
			self.set_zed_button(tk.Button(self, text="0", command=lambda: self.press('0'), width='6', height='2', font=font))
			self.set_one_button(tk.Button(self, text="1", command=lambda: self.press('1'), width='6', height='2', font=font))
			self.set_two_button(tk.Button(self, text="2", command=lambda: self.press('2'), width='6', height='2', font=font))
			self.set_three_button(tk.Button(self, text="3", command=lambda: self.press('3'), width='6', height='2', font=font))
			self.set_four_button(tk.Button(self, text="4", command=lambda: self.press('4'), width='6', height='2', font=font))
			self.set_five_button(tk.Button(self, text="5", command=lambda: self.press('5'), width='6', height='2', font=font))
			self.set_six_button(tk.Button(self, text="6", command=lambda: self.press('6'), width='6', height='2', font=font))
			self.set_seven_button(tk.Button(self, text="7", command=lambda: self.press('7'), width='6', height='2', font=font))
			self.set_eight_button(tk.Button(self, text="8", command=lambda: self.press('8'), width='6', height='2', font=font))
			self.set_nine_button(tk.Button(self, text="9", command=lambda: self.press('9'), width='6', height='2', font=font))
			self.set_deci_button(tk.Button(self, text=".", command=lambda: self.check('.'), width='6', height='2', font=font))
			self.set_blank_button(tk.Button(self, text=" ", state=tk.DISABLED, width='6', height='2', font=font, bg='orange'))

			self.add_num_button(self.get_zed_button())
			self.add_num_button(self.get_one_button())
			self.add_num_button(self.get_two_button())
			self.add_num_button(self.get_three_button())
			self.add_num_button(self.get_four_button())
			self.add_num_button(self.get_five_button())
			self.add_num_button(self.get_six_button())
			self.add_num_button(self.get_seven_button())
			self.add_num_button(self.get_eight_button())
			self.add_num_button(self.get_nine_button())
			self.add_num_button(self.get_deci_button())
			self.add_num_button(self.get_blank_button())

			self.get_deci_button().grid(row=5, column=0, padx=2, pady=2)
			self.get_zed_button().grid(row=5, column=1, padx=2, pady=2)
			self.get_one_button().grid(row=4, column=0, padx=2, pady=2)
			self.get_two_button().grid(row=4, column=1, padx=2, pady=2)
			self.get_three_button().grid(row=4, column=2, padx=2, pady=2)
			self.get_four_button().grid(row=3, column=0, padx=2, pady=2)
			self.get_five_button().grid(row=3, column=1, padx=2, pady=2)
			self.get_six_button().grid(row=3, column=2, padx=2, pady=2)
			self.get_seven_button().grid(row=2, column=0, padx=2, pady=2)
			self.get_eight_button().grid(row=2, column=1, padx=2, pady=2)
			self.get_nine_button().grid(row=2, column=2, padx=2, pady=2)

			# Operation buttons
			self.set_minus_button(tk.Button(self, text="-", command=lambda: self.check('-'), width='6', height='2', font=font, bg='skyblue1'))
			self.set_plus_button(tk.Button(self, text="+", command=lambda: self.check('+'), width='6', height='2', font=font, bg='skyblue1'))
			self.set_mult_button(tk.Button(self, text="x", command=lambda: self.check('*'), width='6', height='2', font=font, bg='skyblue1'))
			self.set_div_button(tk.Button(self, text="/", command=lambda: self.check('/'), width='6', height='2', font=font, bg='skyblue1'))
			self.set_lpar_button(tk.Button(self, text="(", command=lambda: self.check('('), width='6', height='2', font=font, bg='skyblue1'))
			self.set_rpar_button(tk.Button(self, text=")", command=lambda: self.check(')'), width='6', height='2', font=font, bg='skyblue1'))
			self.set_exp_button(tk.Button(self, text="^", command=lambda: self.check('**'), width='6', height='2', font=font, bg='skyblue1'))
			self.set_mod_button(tk.Button(self, text="mod", command=lambda: self.check('%'), width='6', height='2', font=font, bg='skyblue1'))
			self.set_clear_button(tk.Button(self, text="C", command=self.clear, width='6', height='2', font=font, bg='skyblue1'))
			self.set_eq_button(tk.Button(self, text="=", command=self.equate, width='6', height='2', font=font, bg='skyblue1'))
			self.set_back_button(tk.Button(self, text='<', command=self.delete, width='6', height='2', font=font, bg='skyblue1'))
			self.set_exit_button(tk.Button(self, text="EXIT", command=self.close, width='6', height='2', font=font, bg='skyblue1'))
			self.set_up_button(tk.Button(self, text="\u2191", command=self.up, width='6', height='2', font=font, bg='skyblue1'))
			self.set_down_button(tk.Button(self, text=" \u2193", command=self.down, width='6', height='2', font=font, bg='skyblue1'))

			self.add_op_button(self.get_minus_button())
			self.add_op_button(self.get_plus_button())
			self.add_op_button(self.get_mult_button())
			self.add_op_button(self.get_div_button())
			self.add_op_button(self.get_lpar_button())
			self.add_op_button(self.get_rpar_button())
			self.add_op_button(self.get_exp_button())
			self.add_op_button(self.get_clear_button())
			self.add_op_button(self.get_eq_button())
			self.add_op_button(self.get_back_button())
			self.add_op_button(self.get_exit_button())
			self.add_op_button(self.get_up_button())
			self.add_op_button(self.get_down_button())

			self.get_exit_button().grid(row=0, column=0, padx=2, pady=2)
			self.get_back_button().grid(row=0, column=1, padx=2, pady=2)
			self.get_up_button().grid(row=0, column=2, padx=2, pady=2)
			self.get_down_button().grid(row=0, column=3, padx=2, pady=2)
			self.get_mod_button().grid(row=1, column=0, padx=2, pady=2)
			self.get_lpar_button().grid(row=1, column=1, padx=2, pady=2)
			self.get_rpar_button().grid(row=1, column=2, padx=2, pady=2)
			self.get_div_button().grid(row=1, column=3, padx=2, pady=2)
			self.get_mult_button().grid(row=2, column=3, padx=2, pady=2)
			self.get_minus_button().grid(row=3, column=3, padx=2, pady=2)
			self.get_plus_button().grid(row=4, column=3, padx=2, pady=2)
			self.get_eq_button().grid(row=5, column=3, padx=2, pady=2)
			self.get_clear_button().grid(row=5, column=2, padx=2, pady=2)
		except Exception as ex:
			self.throw_exec('cust')

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
			script_dir = os.path.dirname(os.path.abspath(__file__))
			src_dir = os.path.dirname(script_dir)
			proj_dir = os.path.dirname(src_dir)
			data_dir = os.path.join(proj_dir, "data")
			data_path = os.path.join(data_dir, "data.db")
			self.set_db_path(os.path.join(data_path))
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

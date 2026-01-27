""" Native imports. """
import os
import asyncio
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
	calc : The controller's calculator
	num_buttons : The controller's number buttons
	zed_button : The controller's zero button
	one_button : The controller's one button
	two_button : The controller's two button
	three_button : The controller's three button
	four_button : The controller's four button
	five_button : The controller's five button
	six_button : The controller's six button
	seven_button : The controller's seven button
	eight_button : The controller's eight button
	nine_button : The controller's nine button
	deci_button : The controller's decimal button
	blank_button : The controller's blank button
	op_buttons : The controller's operation buttons
	clear_button : The controller's clear button
	eq_button : The controller's equals button
	lpar_button : The controller's left parentheses button
	rpar_button : The controller's right parentheses button
	plus_button : The controller's plus button
	minus_button : The controller's minus button
	mult_button : The controller's multiplication button
	div_button : The controller's division button
	exp_button : The controller's exponent button
	mod_button : The controller's modulo button
	fact_button : The controller's factorial button
	sin_button : The controller's sine button
	cos_button : The controller's cosine button
	tan_button : The controller's tangent button
	back_button : The controller's back button
	up_button : The controller's up button
	down_button : The controller's down button
	exit_button : The controller's exit button
	equation : The controller's equation
	previous_equations : The controller's previous input equations
	index : The controller's scroll index
	travelling : The controller's travelling status
	db : The controller's database
	db_path : The path to the controller's database

	```
	Methods
	-------
	throw_exec : Throws a specified exception
	check : Checks the user input character for possible errors
	press : Callback to add to controller's equation
	clear : Clears the input equation
	close : Closes the application
	delete : Deleted the last character in the equation
	up : Scrolls upward through previous equations
	down : Scrolls downward through previous equations
	equate : Solves the input equation
	customize : Customized the controller
	place : Places the controller on the calculator
	querry : Querries through database table for previous entries
	connect : Connect to database and creates a data table

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
		self.db_path = None

		self.diresolve()
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

	""" Adds a button to the controller's number buttons.

	@param num_button : A number button
	@type num_button : tk.Button()
	"""
	def add_num_button(self, num_button):
		self.get_num_buttons().append(num_button)

	""" Returns the controller's zero button.

	@return zed_button : The controller's zero button
	@rtype zed_button : tk.Button()
	"""
	def get_zed_button(self):
		return self.zed_button

	""" Sets the controller's zero button.

	@param zbutton : A zero button
	@type zbutton : tk.Button()
	"""
	def set_zed_button(self, zbutton):
		self.zed_button = zbutton

	""" Returns the controller's one button.

	@return one_button : The controller's one button
	@rtype one_button : tk.Button()
	"""
	def get_one_button(self):
		return self.one_button

	""" Sets the controller's one button.

	@param one_button : A one button
	@type one_button : tk.Button()
	"""
	def set_one_button(self, one_button):
		self.one_button = one_button

	""" Returns the controller's two button.

	@return two_button : The controller's two button
	@rtype two_button : tk.Button()
	"""
	def get_two_button(self):
		return self.two_button

	""" Sets the controller's two button.

	@param two_button : A two button
	@type two_button : tk.Button()
	"""
	def set_two_button(self, two_button):
		self.two_button = two_button

	""" Returns the controller's three button.

	@return three_button : The controller's three button
	@rtype three_button : tk.Button()
	"""
	def get_three_button(self):
		return self.three_button

	""" Sets the controller's three button.

	@param three_button : A three button
	@type three_button : tk.Button()
	"""
	def set_three_button(self, three_button):
		self.three_button = three_button

	""" Returns the controller's four button.

	@return four_button : The controller's four button
	@rtype four_button : tk.Button()
	"""
	def get_four_button(self):
		return self.four_button

	""" Sets the controller's four button.

	@param four_button : A four button
	@type four_button : tk.Button()
	"""
	def set_four_button(self, four_button):
		self.four_button = four_button

	""" Returns the controller's five button.

	@return five_button : The controller's five button
	@rtype five_button : tk.Button()
	"""
	def get_five_button(self):
		return self.five_button

	""" Sets the controller's five button.

	@param five_button : A five button
	@type five_button : tk.Button()
	"""
	def set_five_button(self, five_button):
		self.five_button = five_button

	""" Returns the controller's six button.

	@return six_button : The controller's six button
	@rtype six_button : tk.Button()
	"""
	def get_six_button(self):
		return self.six_button

	""" Sets the controller's six button.

	@param six_button : A six button
	@type six_button : tk.Button()
	"""
	def set_six_button(self, six_button):
		self.six_button = six_button

	""" Returns the controller's seven button.

	@return seven_button : The controller's seven button
	@rtype seven_button : tk.Button()
	"""
	def get_seven_button(self):
		return self.seven_button

	""" Sets the controller's seven button.

	@param seven_button : A seven button
	@type seven_button : tk.Button()
	"""
	def set_seven_button(self, seven_button):
		self.seven_button = seven_button

	""" Returns the controller's eight button.

	@return eight_button : The controller's eight button
	@rtype eight_button : tk.Button()
	"""
	def get_eight_button(self):
		return self.eight_button

	""" Sets the controller's eight button.

	@param eight_button : An eight button.
	@type eight_button : tk.Button()
	"""
	def set_eight_button(self, eight_button):
		self.eight_button = eight_button

	""" Returns the controller's nine button.

	@return nine_button : The controller's nine button
	@rtype nine_button : tk.Button()
	"""
	def get_nine_button(self):
		return self.nine_button

	""" Sets the controller's nine button.

	@param nine_button : A nine button
	@type nine_button : tk.Button()
	"""
	def set_nine_button(self, nine_button):
		self.nine_button = nine_button

	""" Returns the controller's decimal button.

	@return deci_button : The controller's decimal button
	@rtype deci_button : tk.Button()
	"""
	def get_deci_button(self):
		return self.deci_button

	""" Sets the controller's decimal button.

	@param deci_button : A decimal button
	@type deci_button : tk.Button()
	"""
	def set_deci_button(self, deci_button):
		self.deci_button = deci_button

	""" Returns the controller's blank button.

	@return blank_button : The controller's blank button
	@rtype blank_button : tk.Button()
	"""
	def get_blank_button(self):
		return self.blank_button

	""" Sets the controller's blank button.

	@param blank_button : A blank button
	@type blank_button : tk.Button()
	"""
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

	""" Adds a button to the controller's operation buttons.

	@param op_button : An operation button
	@type op_button : tk.Button()
	"""
	def add_op_button(self, op_button):
		self.get_op_buttons().append(op_button)

	""" Returns the controller's clear button.

	@return clear_button : The controller's clear button
	@rtype clear_button : tk.Button()
	"""
	def get_clear_button(self):
		return self.clear_button

	""" Sets the controller's clear button.

	@param clear_button : A clear button
	@type clear_button : tk.Button()
	"""
	def set_clear_button(self, clear_button):
		self.clear_button = clear_button

	""" Returns the controller's equals button.

	@return eq_button : The controller's equals button
	@rtype eq_button : tk.Button()
	"""
	def get_eq_button(self):
		return self.eq_button

	""" Sets the controller's equals button.

	@param eq_button : An equals button
	@type eq_button : tk.Button()
	"""
	def set_eq_button(self, eq_button):
		self.eq_button = eq_button

	""" Returns the controller's left parentheses button.

	@return lpar_button : The controller's left parentheses button
	@rtype lpar_button : tk.Button()
	"""
	def get_lpar_button(self):
		return self.lpar_button

	""" Sets the controller's left parentheses button.

	@param lpar_button : A left parentheses button
	@type lpar_button : tk.Button()
	"""
	def set_lpar_button(self, lpar_button):
		self.lpar_button = lpar_button

	""" Returns the controller's right parentheses button.

	@return rpar_button : The controller's right parentheses button
	@rtype rpar_button : tk.Button()
	"""
	def get_rpar_button(self):
		return self.rpar_button

	""" Sets the controller's right parentheses button.

	@param rpar_button : A right parentheses button
	@type rpar_button : tk.Button()
	"""
	def set_rpar_button(self, rpar_button):
		self.rpar_button = rpar_button

	""" Returns the controller's plus button.

	@return plus_button : The controller's plus button
	@rtype plus_button : tk.Button()
	"""
	def get_plus_button(self):
		return self.plus_button

	""" Sets the controller's plus button.

	@param plus_button : A plus button
	@type plus_button : tk.Button()
	"""
	def set_plus_button(self, plus_button):
		self.plus_button = plus_button

	""" Returns the controller's minus button.

	@return minus_button : The controller's minus button
	@rtype minus_button : tk.Button()
	"""
	def get_minus_button(self):
		return self.minus_button

	""" Sets the controller's minus button.

	@param minus_button : A minus button
	@type minus_button : tk.Button()
	"""
	def set_minus_button(self, minus_button):
		self.minus_button = minus_button

	""" Returns the controller's multiplication button.

	@return mult_button : The controller's multiplication button.
	@rtype mult_button : tk.Button()
	"""
	def get_mult_button(self):
		return self.mult_button

	""" Sets the controller's multiplication button.

	@param mult_button : A multiplication button
	@type mult_button : tk.Button()
	"""
	def set_mult_button(self, mult_button):
		self.mult_button = mult_button

	""" Returns the controller's division button.

	@return div_button : The controller's division button
	@rtype div_button : tk.Button()
	"""
	def get_div_button(self):
		return self.div_button

	""" Sets the controller's division button.

	@param div_button : A division button
	@type div_button : tk.Button()
	"""
	def set_div_button(self, div_button):
		self.div_button = div_button

	""" Returns the controller's exponent button.

	@return exp_button : The controller's exponent button
	@rtype exp_button : tk.Button()
	"""
	def get_exp_button(self):
		return self.exp_button

	""" Sets the controller's exponent button.

	@param exp_button : An exponent button
	@type exp_button : tk.Button()
	"""
	def set_exp_button(self, exp_button):
		self.exp_button = exp_button

	""" Returns the controller's mod button.

	@return mod_button : The controller's mod button
	@rtype mod_button : tk.Button()
	"""
	def get_mod_button(self):
		return self.mod_button

	""" Sets the controller's mod button.

	@param mod_button : A mod button
	@type mod_button : tk.Button()
	"""
	def set_mod_button(self, mod_button):
		self.mod_button = mod_button

	""" Returns the controller's back button.

	@return back_button : The controller's back button
	@rtype back_button : tk.Button()
	"""
	def get_back_button(self):
		return self.back_button

	""" Sets the controller's back button.

	@param back_button : A back button
	@type back_button : tk.Button()
	"""
	def set_back_button(self, back_button):
		self.back_button = back_button

	""" Returns the controller's up button.

	@return up_button : The controller's up button
	@rtype up_button : tk.Button()
	"""
	def get_up_button(self):
		return self.up_button

	""" Sets the controller's up button.

	@param up_button : An up button
	@type up_button : tk.Button()
	"""
	def set_up_button(self, up_button):
		self.up_button = up_button

	""" Returns the controller's down button.

	@return down_button : The controller's down button
	@rtype down_button : tk.Button()
	"""
	def get_down_button(self):
		return self.down_button

	""" Sets the controller's down button.

	@param down_button : A down button
	@type down_button : tk.Button()
	"""
	def set_down_button(self, down_button):
		self.down_button = down_button

	""" Returns the controller's exit button.

	@return exit_button : The controller's exit button
	@rtype exit_button : tk.Button()
	"""
	def get_exit_button(self):
		return self.exit_button

	""" Sets the controller's exit button.

	@param exit_button : An exit button
	@type exit_button : tk.Button()
	"""
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

	""" Throws a specified exception.

	@param mes : The exception
	@type mes : string
	"""
	def throw_exec(self, mes):

		if (mes == 'cust'):
			print('[!] Error customizing controller.')
		elif (mes == 'create'):
			print('[!] Error creating controller.')
		elif (mes == 'dir'):
			print('[!] Error resolving directory structure.')
		elif (mes == 'con'):
			print('[!] Error connecting to database.')
		elif (mes == 'query'):
			print('[!] Error querying database.')
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
		try:
			cursor = self.get_db().cursor()
			cursor.execute("SELECT * FROM previous_table")

			rows=[]
			for i in cursor.fetchall():
				rows.append(i[0])

			self.set_previous_equations(rows)
			self.get_calc().get_pviewer().update(self.get_previous_equations()[-1])
			cursor.close()
		except Exception as ex:
			self.throw_exec('query')

	""" Connects to database and creates table.

	@return null
	"""
	async def connect(self):
		try:
			self.set_db(sqlite3.connect(self.get_db_path()))
		except Exception as ex:
			self.throw_exec('con')

	def diresolve(self):
		try:
			script_dir = os.path.dirname(os.path.abspath(__file__))
			src_dir = os.path.dirname(script_dir)
			proj_dir = os.path.dirname(src_dir)
			data_dir = os.path.join(proj_dir, "data")
			data_path = os.path.join(data_dir, "data.db")

			self.set_db_path(data_path)
		except Exception as ex:
			self.throw_exec('dir')

	async def create(self):
		try:
			create_command = """
			CREATE TABLE previous_table (
			content TEXT NOT_NULL
			)
			"""
			await self.connect()
			self.get_db().cursor().execute('DROP TABLE IF EXISTS previous_table')
			self.get_db().cursor().execute(create_command)
		except Exception as ex:
			self.throw_exec('create')
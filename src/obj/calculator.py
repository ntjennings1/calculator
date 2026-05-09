""" Native imports. """
import asyncio
import tkinter as tk

""" Class imports. """
from obj.scenario import Scenario
from obj.controller import Controller
from obj.viewer import Viewer

class Calculator():
	"""
	A class representation of a calculator.

	```
	Attributes
	----------
	root : The calculator's tk application
	controller : The calculator's controller
	nviewer : The calculator's new viewer
	pviewer : The calculator's previous viewer
	bviewer : The calculator's blank viewer
	open : The calculator's open status

	```
	Methods
	-------
	throw_exec : Throws a specified exception
	customize : Customizes the calculator
	fill : Fills the calculator with corresponding components
	run : Starts the calculator application
	"""

	""" Initialize class instance. """
	def __init__(self, scenario, loop):
		self.scenario = scenario
		self.loop = loop
		self.root = tk.Tk()
		self.controller = None
		self.nviewer = None
		self.pviewer = None
		self.bviewer = None
		self.open = False

	def get_scenario(self):
		return self.scenario

	def set_scenario(self, scenario):
		return self.scenario

	def get_loop(self):
		return self.loop

	def set_loop(self, loop):
		self.loop = loop

	""" Returns the calculator's root.

	@return root : The calculator's root
	@rtype root : tk.Tk()
	"""
	def get_root(self):
		return self.root

	""" Sets the calculator's root.

	@param root : The calculator's root
	@type root : tk.Tk()
	"""
	def set_root(self, root):
		self.root = root

	""" Returns the calculator's controller.

	@return controller : The calculator's controller
	@rtype controller : Object.class
	"""
	def get_controller(self):
		return self.controller

	""" Sets the calculator's controller.

	@param controller : The apps controller
	@type controller : Object.class
	"""
	def set_controller(self, controller):
		self.controller = controller

	""" Returns the calculator's new viewer.

	@return viewer : The calculator's new viewer
	@rtype viewer : Object.class
	"""
	def get_nviewer(self):
		return self.nviewer

	""" Sets the calculator's new viewer.

	@param nviewer : The calculator's viewer
	@type nviewer : Object.class
	"""
	def set_nviewer(self, nviewer):
		self.nviewer = nviewer

	""" Returns the calculator's previous viewer.

	@return viewer : The calculator's previous viewer
	@rtype viewer : Object.class
	"""
	def get_pviewer(self):
		return self.pviewer

	""" Sets the calculator's previous viewer.

	@param viewer : A previous viewer
	@type viewer : Object.class
	"""
	def set_pviewer(self, pviewer):
		self.pviewer = pviewer

	""" Returns the calculator's blank viewer.

	@return bviewer : The calculators blank viewer
	@rtype bviewer : Object.class
	"""
	def get_bviewer(self):
		return self.bviewer

	""" Sets the calculator's blank viewer.

	@param bviewer : A blank view
	@type bviewer : Object.class
	"""
	def set_bviewer(self, bviewer):
		self.bviewer = bviewer

	""" Returns the calculator's open status.

	@return open : The calculator's open status
	@rtype open : bool
	"""
	def get_open(self):
		return self.open

	""" Sets the calculator's open status.

	@param open : An open status
	@type open : bool
	"""
	def set_open(self, open):
		self.open = open

	""" Throws a specified exception.

	@param mes : An exception
	@type mes : string
	"""
	def throw_exec(self, mes):

		if (mes == 'run'):
			print('[!] Error running calculator.')
		elif (mes == 'custom'):
			print('[!] Error customizing ui elements.')
		elif (mes == 'fill'):
			print('[!] Error filling calculator ui.')

	""" Fills the calculator's with its components.

	@return null
	"""
	async def fill(self):

		try:
			self.set_nviewer(Viewer(self.get_root()))
			self.set_bviewer(Viewer(self.get_root()))
			self.set_pviewer(Viewer(self.get_root()))
			self.set_controller(Controller(self.get_root(), self))
			await self.get_controller().create()
		except Exception as ex:
			self.throw_exec('fill')

	""" Customizes the calculator.

	@return null
	"""
	async def customize(self):

		try:
			self.get_pviewer().place(0,0)
			self.get_pviewer().get_view().configure(padx=0, font=('Courier New', 10))

			self.get_bviewer().place(1,0)
			self.get_bviewer().get_view().configure(padx=0)

			self.get_nviewer().place(2,0)
			self.get_nviewer().get_view().configure(padx=0, font=('Courier New', 20))

			self.get_controller().place(3,0)
		except Exception as ex:
			self.throw_exec('custom')


	async def pump(self):
		while True:
			try:
				self.get_root().update_idletasks()
				self.get_root().update()
			except tk.TclError:
				print(ex)
				print('s')
				return
			await asyncio.sleep(0.001)

	""" Starts the calculator application.

	@return null
	"""
	async def run(self):

		try:
			print('[-->] Running calculator.')
			await self.fill()
			await self.customize()
			self.get_root().title('Calculator')
			self.get_root().config(bg='gray87')

			self.set_open(True)	
			asyncio.create_task(self.pump())

		except asyncio.CancelledError:
			print('[!] Tasks were cancelled.')
		except Exception as ex:
			print(ex)
			self.throw_exec('run')


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

	```
	Methods
	-------
	customize : Customizes the calculator
	fill : Fills the calculator with corresponding components
	run : Starts the calculator application
	"""

	""" Initialize class instance. """
	def __init__(self):
		self.scenario = Scenario()

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

	""" Returns the calculator's root.

	@return root : The calculator's app
	@rtype root : tk.Tk()
	"""
	def get_root(self):
		return self.root

	""" Sets the calculator's root. 

	@param root : The calculator's app
	@type root : tk.Tk()
	"""
	def set_root(self, root):
		self.root = root

	""" Returns the calculator's controller.

	@return controller : The calculator's controller
	@rtype controller : tk.Frame
	"""
	def get_controller(self):
		return self.controller

	""" Sets the calculator's controller. 

	@param controller : The apps controller
	@type controller : tk.Frame
	"""
	def set_controller(self, controller):
		self.controller = controller

	""" Returns the calculator's viewer.

	@return viewer : The calculator's viewer
	@rtype viewer : tk.Frame
	"""
	def get_nviewer(self):
		return self.viewer

	""" Sets the calculator's viewer.

	@param viewer : The calculator's viewer
	@type viewer : tk.Frame
	"""
	def set_nviewer(self, viewer):
		self.viewer = viewer

	""" Returns the calculator's viewer.

	@return viewer : The calculator's viewer
	@rtype viewer : tk.Frame
	"""
	def get_pviewer(self):
		return self.pviewer

	""" Sets the calculator's viewer.

	@param viewer : The calculator's viewer
	@type viewer : tk.Frame
	"""
	def set_pviewer(self, pviewer):
		self.pviewer = pviewer

	def get_bviewer(self):
		return self.bviewer

	def set_bviewer(self, bviewer):
		self.bviewer = bviewer

	def get_open(self):
		return self.open

	def set_open(self, open):
		self.open = open

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

	""" Starts the calculator application. 

	@return null
	"""
	async def run(self):

		try:
			print('[!] Running calculator.')
			await self.get_scenario().diresolve()
			await self.fill()
			await self.customize()
			self.get_root().title('Calculator')
			self.get_root().config(bg='gray87')
			self.set_open(True)

			while True:
				self.get_root().update()
				await asyncio.sleep(.1)
		except asyncio.CancelledError:
			print('[!] Tasks were cancelled.')
		except Exception as ex:
			self.throw_exec('run')


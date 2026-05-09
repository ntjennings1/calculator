""" Native imports. """
import asyncio

""" Class imports. """
from obj.calculator import Calculator
from obj.scenario import Scenario

""" Throws a specified exception.

@param mes : The exceptin
@type mes : string
"""
def throw_exec(mes):

	if (mes == 'main'):
		print('[!] Error running calculator.')
	elif (mes == 'cboot'):
		print('[!] Error booting calculator ui.')

""" Creates and runs the calculator.

@returns null
"""
async def main():

	try:
		scene = Scenario()
		await scene.reqresolve()
		await scene.pkgresolve()

		calc = Calculator(scene, asyncio.get_event_loop())
		await calc.run()

		while True:
			await asyncio.sleep(3600)
	except Exception as ex:
		print(ex)
		throw_exec('cboot')

""" Runs the main function.

@return null
"""
if __name__ == '__main__':

	try:
		asyncio.run(main())
	except asyncio.CancelledError:
		print('[!] Tasks were cancelled.')
	except KeyboardInterrupt:
		print('[!] Calculator shutdown.')
	except Exception as ex:
		throw_exec('main')

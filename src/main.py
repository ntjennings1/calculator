import asyncio

""" Class imports. """
from obj.calculator import Calculator

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
		calc = Calculator()
		await calc.run()
	except Exception as ex:
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

""" Native imports. """
import os
import sys
import subprocess
from importlib.metadata import distributions

class Scenario():
    """
    A class representation of a scenario.
    
    ```
    Attributes
    ----------
    system : The scenario's name
    server : The scenario's server
    dir : The scenario's directory
    req_file : The scenario's requirements file
    req : The scenario's requirements
    packages : The scenario's packages
    state : The scenario's state
    
    ```
    Methods
    -------
    throw_exec : Throws a specified exception
    clear_terminal : Clears the systems terminal
    pkgresolve : Satisfies required packages
    reqresolve : Determines required packages
    eval : Evaluates the system
    """
    
    """ Initializes the class instance.
    
    @return null
    """
    def __init__(self):
        self.system = ""
        self.server = None

        self.dir = os.path.dirname(os.path.abspath(__file__))
        self.req_file = None
        self.reqs = []
        self.packages = []
        self.state = False

        self.eval()
        self.clear_terminal()

    """ Returns the systems name.
    
    @return system : The system's name
    @rtype system : string
    """
    def get_system(self):
        return self.system
    
    """ Sets the systems name.
    
    @param system : The system's name
    @type system : string
    """
    def set_system(self, system):
        self.system = system

    """ Returns the scenario's server.

    @return server : The scenario's server
    @rtype server : Obj.class
    """
    def get_server(self):
        return self.server

    """ Sets the scenario's server.

    @param server : A server
    @type server : Obj.class
    """
    def set_server(self, server):
        self.server = server

    """ Returns the scenario's directory.

    @return dir : The scenario's directory
    @rtype dir : os.path.abspath()
    """
    def get_dir(self):
        return self.dir

    """ Sets the scenario's directory.

    @param di : A directory
    @type di : os.path.abspath()
    """
    def set_dir(self, di):
        self.dir = di

    """ Returns the scenario's requirements file.

    @return req_file : The scenario's requirements file
    @rtype req_file : os.path.abspath()
    """
    def get_rfile(self):
        return self.req_file

    """ Sets the scenario's requirements file.

    @param rfile : A requirements file
    @type rfile : os.path.abspath()
    """
    def set_rfile(self, rfile):
        self.req_file = rfile

    """ Returns the scenario's requirements.

    @return req : The scenario's requirements
    @rtype req : list
    """
    def get_reqs(self):
        return self.reqs

    """ Sets the scenario's requirements.

    @param reqs : Requirements
    @type reqs : list
    """
    def set_reqs(self, reqs):
        self.reqs = reqs

    """ Adds a requirement to the scenario's requirements.

    @param req : A requirement
    @type req : string
    """
    def add_req(self, req):
        self.get_reqs().append(req)

    """ Returns the scenario's packages.

    @return packages : The scenario's packages
    @rtype packages : list
    """
    def get_packages(self):
        return self.packages

    """ Sets the scenario's packages.

    @param packages : Packages
    @type packages : list
    """
    def set_packages(self, packages):
        self.packages = packages

    """ Adds a package to the scenario's packages.

    @param package : A package
    @type package : string
    """
    def add_package(self, package):
        self.get_packages().append(package)

    """ Returns the scenario's state.

    @return state : The scenario's state
    @rtype state : bool
    """
    def get_state(self):
        return self.state

    """ Sets the scenario's state.

    @param state : A state
    @type state : bool
    """
    def set_state(self, state):
        self.state = state

    """ Throws a specified exception.

    @param mes : The exception
    @type mes : string
    """
    def throw_exec(self,mes):

        if (mes == 'read'):
            print('[!] Error reading system name.')
        elif (mes == 'clear'):
            print('[!] Error clearing terminal.')
        elif (mes == 'req'):
            print('[!] Error reading requirements.')
        elif (mes == 'pkg'):
            print('[!] Error satisfying dependencies.')

    """ Clears the system's terminal.

    @return null
    """
    def clear_terminal(self):
        try:
            if self.get_system() == 'Windows':
                os.system('cls')
            else:
                os.system('clear')
        except Exception as ex:
            self.throw_exec('clear')

    """ Satisfies required packages.

    @return null
    """
    async def pkgresolve(self):
        try:
            print('[!] Comparing installed packages ...')
            for dist in distributions():
                self.add_package(dist.metadata['Name'] + '==' + dist.version)

            for r in self.get_reqs():
                if r in self.get_packages():
                    pass
                else:
                    print('[!] Installing ' + r)
                    subprocess.check_call([sys.executable, "-m", "pip", "install", str(r)])
                    self.add_package(r)
                print(f'[!] {r} installed.')
            print('[-->] All requirements satisfied.')
        except Exception as ex:
            self.throw_exec('pkg')

    """ Determines required packages.

    @return null
    """
    async def reqresolve(self):
        try:
            print('[!] Checking dependencies ...')
            project_dir = os.path.dirname(os.path.dirname(self.get_dir()))
            self.set_rfile(os.path.join(project_dir, 'requirements.txt'))

            with open (self.get_rfile(), 'r') as req_file:
                for line in req_file:
                    if ('\n' in line):
                        self.add_req(line.replace('\n', ''))
                    else:
                        self.add_req(line)
        except Exception as ex:
            self.throw_exec('req')

    """ Evaluates the system.
    
    @return null
    """    
    def eval(self):
        try:
            if (os.name == 'nt'):
                self.set_system('Windows')
                print('[&] Windows system.')
            else:
                self.set_system('Linux')
                print('[&] Linux system.')

        except Exception as ex:
            self.throw_exec('read')
import os

import click

# assigning the parent directory, commands, to a variable
cmd_folder = os.path.join(os.path.dirname(__file__), 'commands')

# creating the cmd prefix for the file
cmd_prefix = 'cmd_'


class CLI(click.MultiCommand):
    def list_commands(self, ctx):
        """
        Obtain a list of all available commands.
        """
        commands = []

        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and filename.startswith(cmd_prefix):
                
                # here we loop through each of the python files that have a cmd prefix and then append append 
                # the name of the file excluding cmd_ in the name to the list named commands and that is then sorted and returned
                commands.append(filename[4:-3])

        commands.sort()

        return commands

    def get_command(self, ctx, name):
        """
        Get a specific command by looking up the module.
        """
        ns = {}

        filename = os.path.join(cmd_folder, cmd_prefix + name + '.py')

        with open(filename) as f:
            code = compile(f.read(), filename, 'exec')
            eval(code, ns, ns)

        return ns['cli']


@click.command(cls=CLI)
def cli():
    """ Commands to help manage your project. """
    pass

import sys
from tack.commands.CertificateCommand import CertificateCommand
from tack.version import __version__
from tack.commands.BreakCommand import BreakCommand
from tack.commands.Command import Command
from tack.commands.GenerateKeyCommand import GenerateKeyCommand
from tack.commands.SignCommand import SignCommand
from tack.commands.ViewCommand import ViewCommand
from tack.crypto.openssl.OpenSSL import openssl as o

class HelpCommand(Command):

    COMMANDS = {"genkey" : GenerateKeyCommand, "sign" : SignCommand,
                "break" : BreakCommand, "view" : ViewCommand,
                "tackcert" : CertificateCommand}

    def __init__(self, argv):
        Command.__init__(self, argv, "", "")

        if len(argv) < 1:
            HelpCommand.printGeneralUsage()

        self.command = argv[0]

        if not self.command in HelpCommand.COMMANDS:
            self.printError("%s not a valid command." % self.command)

    def execute(self):
        HelpCommand.COMMANDS[self.command].printHelp()

    @staticmethod
    def printHelp():
        print(
"""Provides help for individual commands.

help <command>
""")

    @staticmethod
    def printGeneralUsage(message=None):
        if o.enabled:
            cryptoVersion = "(%s)" % o.SSLeay_version(0)
        else:
            cryptoVersion = "(python crypto)"
        if message:
            print "Error: %s\n" % message
        sys.stdout.write(
"""tack.py version %s %s

Commands (use "help <command>" to see optional args):
  genkey
  sign     -k KEY -c CERT
  break    -k KEY
  view     FILE
  help     COMMAND
""" % (__version__, cryptoVersion))
        sys.exit(-1)

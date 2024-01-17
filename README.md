# KnightsPathTextParser
A program that can parse, edit and repackage text from the language file of Knight's Path: The Tournament game.
Python must be installed to run the program.

In order to parse the text in KP_EN.po, after downloading the files, you need to put the .po file in the same folder with them and run it that way. There is a backup KP_EN.po file inside the project.

getText.bat: Parses the text in the language file KP_EN.po and outputs neededLines.txt.

createNew.bat: Imports the edited neededLines.txt file into a new .po file (KP_NEW.PO).

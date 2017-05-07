from distutils.core import setup
import py2exe

setup(console=['AutoClicker.py'],
	  options={"py2exe":{"bundle_files":1}},
      zipfile = "test.lib"
	  )

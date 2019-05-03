from distutils.core import setup
import py2exe

setup(
	options = {
		"py2exe": {
			"includes": ["sip"]
		}
	},
	windows=['App.pyw']
)


from setuptools import setup, find_packages


setup (
		name = "sqlapi",
		version = "0.1.0",
		packages = find_packages('src'),
		package_dir = {'':'src'},
		include_package_data = True,
		package_data = {
			'': ['TODO', 'BUGS', 'ChangeLog', 'test/*.py'],
		},

#		install_requires = ['sqlite'],


		author = "Essien Ita Essien",
		author_email = "essiene@gmail.com",
		license = "BSD",
		description = "A simple sql abstraction helper layer. Not quite an ORM though",
		keywords = "simple orm sql",
		#url = "http://simpleweb.essienitaessien.com",

		long_description = """
            sqlapi is a simple sql abstraction help layer. It is not an ORM.
		"""
		)

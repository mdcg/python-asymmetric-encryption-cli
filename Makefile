install_dependencies:
	pip install -r requirements/requirements.txt

compile:
	$(MAKE) install_dependencies
	pyinstaller --onefile src/cli.py
	echo Executable was generated in ${PWD}/dist/
package:
	python3 setup.py sdist bdist_wheel

preprocess:
	cd cuteuid && python3 preprocess.py

upload_package:
	python3 -m twine upload --skip-existing dist/*


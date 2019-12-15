package:
	mv src cuteuid && python3 setup.py sdist bdist_wheel && mv cuteuid src && rm -rf build && rm -rf cuteuid.egg-info

preprocess:
	cd cuteuid && python3 preprocess.py

upload_package:
	python3 -m twine upload --skip-existing dist/*


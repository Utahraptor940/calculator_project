venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

run: venv/bin/activate
	./venv/bin/python3 main.py

setup: 
	pip install -r requirements.txt
	pip install -r test_requirements.txt

clean:
	rm -rf __pycache__
	rm -rf venv

test:
	python3 calculator_test.py

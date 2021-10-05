# set -ue
# set -x

# folder for the python virtual environment
PYTHON_VENV="bac0_venv"

# python command
PYTHON=python3.9

FILE_PATH="$(realpath "$(dirname $0)")"

# check if python virtual environment folder exists, if not initialize it
python_venv_created=false

if [ ! -d "$PYTHON_VENV" ]; then
	$PYTHON -m venv "$FILE_PATH/$PYTHON_VENV"

	if [ $? -ne 0 ]; then
		rm -rf "$PYTHON_VENV"
		exit 1
	fi

	python_venv_created=true
fi

# activate python environment
. "$PYTHON_VENV"/bin/activate

if [ $python_venv_created = true ]; then
	# initialize virtual environment: install dependencies
	pip3 install wheel
	pip3 install BAC0 pandas ipython odfpy openpyxl

	if [ $? -ne 0 ]; then
		rm -rf "$PYTHON_VENV"
		exit 1
	fi
fi

# run python script
python "$FILE_PATH"/bacnet_get_objects_props.py "$@"

# deactivate python virtual environment
deactivate

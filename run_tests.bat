set PYTHONPATH=%PYTHONPATH%;%~dp0/environment/PYTHONPATH
set LUCIDITY_TEMPLATE_PATH=%~dp0/environment/LUCIDITY_TEMPLATE_PATH
pip install pytest
pytest

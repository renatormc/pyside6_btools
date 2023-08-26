# What it does

This tool is for developing PySide6 apps using Qt Designer. It scans the project folder to find all the .ui files and uses pyside6-uic to convert them into .py files. The great thing about it is that it automates the task of converting ui files to .py files, saving you from having to do it manually every time you make changes to the GUI in Qt Designer.

# Dependencies

- Python 3.11
- Qt Designer
- Poetry

# Install

```bash
git clone https://github.com/renatormc/pyside6_btools.git
cd pyside6_btools
poetry install && poetry shell && python main.py install
```


# Use

Open Qt Designer
```bash
pbt design
```

Convert all the ui fiels to py
```bash
pbt build
```

Watch ui files and recompile them everytime they change
```bash
pbt watch
```
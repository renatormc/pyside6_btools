# What it does

This tool is for developing Pyside6 apps using Qt Designer. It scans the project folder, finds all the ui files and use pyside6-uic to convert them to py files. The good thing about it is that it automatize the task of converting ui files to py without doing it manually everytime you changes the gui on Qt Designer.

# Dependencies

- Python 3.11
- Qt Designer
- Poetry

# Install

```bash
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
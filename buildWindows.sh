#!/bin/bash

# Variables
PYTHON_SCRIPT="ccfsSearchWindows.py"
EXE_NAME="ccfsSearchWindows.exe"

# Ensure PyInstaller is installed
echo "Installing PyInstaller..."
pip install pyinstaller

# Build the executable
echo "Building the executable..."
pyinstaller --onefile --windowed --name $EXE_NAME $PYTHON_SCRIPT

# Move the executable to the project root directory
echo "Moving the executable to the project root directory..."
mv dist/$EXE_NAME .

# Clean up build files
echo "Cleaning up build files..."
rm -rf build dist __pycache__ $PYTHON_SCRIPT.spec

echo "Executable built successfully!"
@echo off
echo ========================================
echo 🧠 INFINITY MEMORY AI - WINDOWS DEMO
echo ========================================
echo.

echo Installing required libraries...
pip install -r requirements.txt

echo.
echo Checking memory file...

IF NOT EXIST memory.json (
    echo {} > memory.json
    echo Created new memory.json
)

echo.
echo ========================================
echo DEMO INSTRUCTIONS FOR JUDGES:
echo ----------------------------------------
echo 1. Type: My name is Alex
echo 2. Type: I like AI
echo 3. Type: I like Coding
echo 4. Ask: What are my preferences?
echo ========================================
echo.

echo Starting AI Assistant...
echo.

python app.py

pause

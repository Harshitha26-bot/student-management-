#!/bin/bash

echo "Checking Student Management System files..."

if [ -f app.py ]; then
    echo "app.py exists"
else
    echo "app.py is missing"
fi

if [ -f requirements.txt ]; then
    echo "requirements.txt exists"
else
    echo "requirements.txt is missing"
fi

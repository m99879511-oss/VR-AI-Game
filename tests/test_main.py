Python

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import main

def test_main_callable():
    """Test that main function exists and is callable."""
    assert callable(main.main)

def test_dependency_check():
    """Test that dependency check function exists."""
    assert callable(main.check_ai_dependencies)

def test_environment_check():
    """Test that environment check function exists."""
    assert callable(main.check_environment)

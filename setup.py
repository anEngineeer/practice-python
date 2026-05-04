#!/usr/bin/env python3
"""
Setup script for Python Learning Repository

This script helps set up the learning environment and provides useful utilities.
"""

import os
import subprocess
import sys
from pathlib import Path


def setup_virtual_environment():
    """Create and activate virtual environment"""
    print("🔧 Setting up virtual environment...")
    
    venv_path = Path("venv")
    if not venv_path.exists():
        subprocess.run([sys.executable, "-m", "venv", "venv"])
        print("✅ Virtual environment created")
    else:
        print("ℹ️  Virtual environment already exists")
    
    # Instructions for activation
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate"
    else:  # Unix/MacOS
        activate_cmd = "source venv/bin/activate"
    
    print(f"📝 To activate: {activate_cmd}")


def install_dependencies():
    """Install required packages"""
    print("\n📦 Installing dependencies...")
    
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ], check=True)
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        print("💡 Make sure you've activated the virtual environment")


def run_sample_tests():
    """Run sample tests to verify setup"""
    print("\n🧪 Running sample tests...")
    
    try:
        # Test the args_kwargs example
        subprocess.run([
            sys.executable, "fundamentals/03-functions/args_kwargs.py"
        ], check=True)
        print("✅ Sample Python code runs successfully")
        
        # Test pytest if available
        result = subprocess.run([
            sys.executable, "-m", "pytest", "coding-problems/01-easy/two-sum/test_solution.py", "-v"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Tests pass successfully")
        else:
            print("⚠️  Some tests failed (this is normal for initial setup)")
            
    except FileNotFoundError:
        print("ℹ️  Some test files not found (expected for fresh setup)")


def show_directory_structure():
    """Display the organized directory structure"""
    print("\n📁 Repository Structure:")
    
    structure = """
    practice-python/
    ├── 📚 fundamentals/           # Core Python concepts
    │   ├── 01-variables-and-types/
    │   ├── 02-control-flow/
    │   ├── 03-functions/          # ✅ args_kwargs.py moved here
    │   ├── 04-data-structures-basic/
    │   └── 05-file-handling/
    ├── 🏗️  oop/                   # Object-oriented programming
    │   ├── 01-classes-objects/    # ✅ classes_object.py, property_attribute.py
    │   ├── 02-inheritance/        # ✅ inheritence.py
    │   ├── 03-polymorphism/
    │   ├── 04-encapsulation/      # ✅ encapsulation.py
    │   ├── 05-abstraction/        # ✅ abstract_classes.py
    │   └── 06-composition/        # ✅ composition.py
    ├── 🔧 advanced/               # Advanced Python topics
    │   ├── 01-decorators/         # ✅ decorators.py
    │   ├── 02-generators/
    │   ├── 03-context-managers/
    │   ├── 04-metaclasses/
    │   └── 05-async-programming/
    ├── 🧪 testing/                # Testing frameworks
    ├── 📊 data-structures/        # Data structures implementations
    │   ├── 01-arrays-lists/       # ✅ dynamic_array.py example
    │   ├── 02-linked-lists/
    │   ├── 03-stacks-queues/
    │   ├── 04-trees/
    │   ├── 05-graphs/
    │   ├── 06-hash-tables/
    │   └── 07-heaps/
    ├── ⚡ algorithms/             # Algorithm implementations
    │   ├── 01-sorting/            # ✅ sorting_algorithms.py example
    │   ├── 02-searching/
    │   ├── 03-recursion/
    │   ├── 04-dynamic-programming/
    │   ├── 05-graph-algorithms/
    │   └── 06-greedy-algorithms/
    ├── 💻 coding-problems/        # Practice problems
    │   ├── 01-easy/               # ✅ two-sum example complete
    │   ├── 02-medium/
    │   ├── 03-hard/
    │   └── 04-company-specific/
    ├── 🌐 web-development/        # Web frameworks
    ├── 📈 projects/               # Hands-on projects
    ├── 📝 notes/                  # Learning notes
    ├── 🔄 legacy/                 # Old files (organized)
    ├── 📋 LEARNING_ROADMAP.md     # ✅ 12-week structured plan
    ├── 📋 requirements.txt        # ✅ All necessary dependencies
    └── 📋 README.md               # ✅ Complete guide
    """
    
    print(structure)


def show_next_steps():
    """Show what to do next"""
    print("\n🚀 Next Steps:")
    print("1. Activate virtual environment:")
    
    if os.name == 'nt':
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    
    print("\n2. Install dependencies:")
    print("   pip install -r requirements.txt")
    
    print("\n3. Start learning with Week 1:")
    print("   cd fundamentals/01-variables-and-types/")
    
    print("\n4. Follow the roadmap:")
    print("   📖 Read LEARNING_ROADMAP.md")
    print("   📚 Study fundamentals/ first")
    print("   💻 Practice coding-problems/ daily")
    
    print("\n5. Test your knowledge:")
    print("   python fundamentals/03-functions/args_kwargs.py")
    print("   pytest coding-problems/01-easy/two-sum/test_solution.py")


def main():
    """Main setup function"""
    print("🐍 Python Learning Repository Setup")
    print("=" * 50)
    
    # Check if we're in the right directory
    current_dir = Path.cwd()
    readme_exists = Path("README.md").exists()
    
    print(f"📍 Current directory: {current_dir}")
    print(f"📋 README.md exists: {readme_exists}")
    
    if not readme_exists:
        print("⚠️  README.md not found, but continuing with setup...")
    
    # Setup steps
    setup_virtual_environment()
    
    # Show structure
    show_directory_structure()
    
    # Show next steps
    show_next_steps()
    
    print("\n🎯 Your learning journey is ready to begin!")
    print("📅 Follow the 12-week roadmap in LEARNING_ROADMAP.md")
    print("💪 Consistency is key - 2 hours daily!")
    print("\n✨ Happy Learning! ✨")


if __name__ == "__main__":
    main()
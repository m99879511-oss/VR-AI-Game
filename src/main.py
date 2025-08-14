# Entry point for VR-AI Game  
import os
import sys
from pathlib import Path

def check_ai_dependencies():
    """Check if AI dependencies are properly installed."""
    dependencies = {
        'openai': 'OpenAI API',
        'elevenlabs': 'ElevenLabs TTS', 
        'torch': 'PyTorch',
        'numpy': 'NumPy',
        'transformers': 'Hugging Face Transformers'
    }
    
    print("🔍 Checking AI dependencies...")
    missing = []
    
    for module, description in dependencies.items():
        try:
            __import__(module)
            print(f"✅ {description} - OK")
        except ImportError:
            print(f"❌ {description} - Missing")
            missing.append(module)
    
    if missing:
        print(f"\n⚠️  Missing dependencies: {', '.join(missing)}")
        print("Run 'pip install -r requirements.txt' to install them.")
        return False
    
    print("\n✅ All AI dependencies are installed!")
    return True

def check_environment():
    """Check environment configuration."""
    print("\n🌍 Checking environment...")
    
    # Check for .env file
    env_file = Path('.env')
    if env_file.exists():
        print("✅ .env file found")
    else:
        print("⚠️  .env file not found. Copy .env.example to .env and configure your API keys.")
    
    # Check Python version
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"🐍 Python version: {python_version}")
    
    # Check if GPU is available
    try:
        import torch
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            print(f"🚀 GPU available: {gpu_name}")
        else:
            print("💻 Running on CPU (GPU not available)")
    except ImportError:
        print("⚠️  PyTorch not available - cannot check GPU status")

def main():
    """Main entry point for VR-AI Game."""
    print("=" * 50)
    print("🎮 VR-AI Game - AI System Startup")
    print("=" * 50)
    
    # Check dependencies
    deps_ok = check_ai_dependencies()
    
    # Check environment
    check_environment()
    
    if deps_ok:
        print("\n🚀 VR-AI Game AI system is ready!")
        print("\nNext steps:")
        print("1. Configure your API keys in .env file")
        print("2. Check docs/AI_SETUP.md for detailed setup instructions")
        print("3. Explore ai-scripts/ for AI implementation examples")
    else:
        print("\n❌ Setup incomplete. Please install missing dependencies.")
        sys.exit(1)

if __name__ == "__main__":
    main()

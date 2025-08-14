"""
AI NPC System - Basic Example
This script demonstrates basic AI functionality for the VR-AI-Game.
"""

import os
import sys
from pathlib import Path

# Add src to path for imports
sys.path.append(str(Path(__file__).parent.parent / 'src'))

def test_openai_connection():
    """Test OpenAI API connection (requires API key)."""
    try:
        import openai
        from dotenv import load_dotenv
        
        # Load environment variables
        load_dotenv()
        
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("⚠️  OPENAI_API_KEY not found in .env file")
            return False
            
        # Initialize client
        client = openai.OpenAI(api_key=api_key)
        
        print("✅ OpenAI client initialized successfully")
        return True
        
    except ImportError:
        print("❌ OpenAI library not installed. Run: pip install openai")
        return False
    except Exception as e:
        print(f"❌ OpenAI connection failed: {e}")
        return False

def test_elevenlabs_connection():
    """Test ElevenLabs API connection (requires API key)."""
    try:
        import elevenlabs
        from dotenv import load_dotenv
        
        # Load environment variables  
        load_dotenv()
        
        api_key = os.getenv('ELEVENLABS_API_KEY')
        if not api_key:
            print("⚠️  ELEVENLABS_API_KEY not found in .env file")
            return False
            
        # Set API key
        elevenlabs.set_api_key(api_key)
        
        print("✅ ElevenLabs client configured successfully")
        return True
        
    except ImportError:
        print("❌ ElevenLabs library not installed. Run: pip install elevenlabs")
        return False
    except Exception as e:
        print(f"❌ ElevenLabs connection failed: {e}")
        return False

def test_pytorch():
    """Test PyTorch installation and GPU availability."""
    try:
        import torch
        
        print(f"✅ PyTorch {torch.__version__} installed")
        
        if torch.cuda.is_available():
            device_count = torch.cuda.device_count()
            device_name = torch.cuda.get_device_name(0)
            print(f"🚀 GPU available: {device_name} ({device_count} device(s))")
        else:
            print("💻 Running on CPU (no GPU detected)")
            
        return True
        
    except ImportError:
        print("❌ PyTorch not installed. Run: pip install torch")
        return False

def generate_sample_dialogue():
    """Generate sample NPC dialogue using OpenAI."""
    try:
        import openai
        from dotenv import load_dotenv
        
        load_dotenv()
        api_key = os.getenv('OPENAI_API_KEY')
        
        if not api_key:
            print("⚠️  Cannot generate dialogue: OpenAI API key not configured")
            return
            
        client = openai.OpenAI(api_key=api_key)
        
        prompt = """You are a friendly AI NPC in a VR game. The player has just approached you in a medieval tavern. 
        Greet them and offer some advice about the dangerous dungeon nearby. Keep it under 50 words."""
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=60
        )
        
        dialogue = response.choices[0].message.content
        print(f"🗨️  Sample NPC Dialogue: {dialogue}")
        
    except Exception as e:
        print(f"❌ Failed to generate dialogue: {e}")

def main():
    """Main function to test AI components."""
    print("=" * 60)
    print("🤖 VR-AI Game - AI Component Test")
    print("=" * 60)
    
    # Test core AI libraries
    print("\n📚 Testing AI Libraries:")
    openai_ok = test_openai_connection()
    elevenlabs_ok = test_elevenlabs_connection()
    pytorch_ok = test_pytorch()
    
    # Test API functionality (if configured)
    if openai_ok:
        print("\n🧠 Testing AI Dialogue Generation:")
        generate_sample_dialogue()
    
    print("\n" + "=" * 60)
    
    if openai_ok and elevenlabs_ok and pytorch_ok:
        print("✅ All AI components are working! Your PC is ready for AI development.")
    else:
        print("⚠️  Some components need configuration. Check the setup guide.")
        
    print("\nNext steps:")
    print("1. Configure API keys in .env file")
    print("2. Explore more AI scripts in this directory")
    print("3. Check docs/AI_SETUP.md for detailed guides")

if __name__ == "__main__":
    main()
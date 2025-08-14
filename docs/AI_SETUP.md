# AI Development Setup Guide

This guide will help you set up your PC to run the AI components of the VR-AI-Game project.

## Prerequisites

### Required Software
- **Python 3.8 or later** - [Download from python.org](https://www.python.org/downloads/)
- **Git** - For version control
- **At least 8GB RAM** - For AI model inference
- **GPU with CUDA support** (recommended) - For faster AI processing

### Optional but Recommended
- **NVIDIA RTX GPU** - For AI model training and inference
- **16GB+ RAM** - For larger AI models
- **SSD storage** - For faster model loading

## Quick Setup

### 1. Clone the Repository
```bash
git clone https://github.com/m99879511-oss/VR-AI-Game.git
cd VR-AI-Game
```

### 2. Run Automated Setup
```bash
./scripts/setup.sh
```

This will:
- Create a Python virtual environment
- Install all required AI/ML dependencies
- Set up the development environment

### 3. Activate Environment
```bash
source venv/bin/activate
```

### 4. Test Installation
```bash
python src/main.py
```

## Manual Setup (Alternative)

If the automated setup doesn't work, follow these manual steps:

### 1. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## AI Components Overview

The project includes these AI technologies:

### 🧠 Core AI Stack
- **OpenAI API** - GPT models for NPC dialogue and decision making
- **ElevenLabs** - Text-to-speech for realistic NPC voices
- **PyTorch** - Deep learning framework for custom AI models
- **Transformers** - Pre-trained models for natural language processing

### 🎮 Game Integration
- **Pygame** - Game development utilities
- **FastAPI** - API framework for AI service integration
- **WebSockets** - Real-time communication between game and AI

### 🔊 Audio Processing
- **Librosa** - Audio analysis and processing
- **Pydub** - Audio manipulation
- **SoundFile** - Audio file handling

## Configuration

### API Keys Setup
Create a `.env` file in the project root:

```bash
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# ElevenLabs Configuration  
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here

# Optional: Custom model configurations
MODEL_CACHE_DIR=./models
MAX_TOKENS=150
TEMPERATURE=0.7
```

### Hardware Optimization

#### For NVIDIA GPUs:
```bash
# Install CUDA-enabled PyTorch (if you have a compatible GPU)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### For CPU-only systems:
The default installation works on CPU, but AI inference will be slower.

## Testing Your Setup

### 1. Run Basic Tests
```bash
python -m pytest tests/ -v
```

### 2. Test AI Components
```bash
# Test OpenAI integration (requires API key)
python -c "import openai; print('OpenAI: OK')"

# Test ElevenLabs integration (requires API key)  
python -c "import elevenlabs; print('ElevenLabs: OK')"

# Test PyTorch
python -c "import torch; print(f'PyTorch: {torch.__version__}')"
```

### 3. GPU Verification (if applicable)
```bash
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
```

## Troubleshooting

### Common Issues

#### 1. Python Version Error
Make sure you have Python 3.8 or later:
```bash
python --version
```

#### 2. Permission Errors (Linux/Mac)
Make the setup script executable:
```bash
chmod +x scripts/setup.sh
```

#### 3. Virtual Environment Issues
Delete and recreate the virtual environment:
```bash
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 4. GPU/CUDA Issues
For NVIDIA GPUs, install CUDA toolkit from [NVIDIA's website](https://developer.nvidia.com/cuda-downloads).

#### 5. Memory Issues
If you encounter out-of-memory errors:
- Close other applications
- Use smaller AI models
- Reduce batch sizes in AI processing

### Getting Help

- **Issues**: Open an issue on the GitHub repository
- **Discussions**: Use GitHub Discussions for questions
- **Documentation**: Check the `/docs` folder for more detailed guides

## Next Steps

After setup is complete:

1. **Read the Documentation**: Check `/docs/AI_NPC_Arena.md` for project details
2. **Explore AI Scripts**: Look at `/ai-scripts/` for AI implementation examples
3. **Configure APIs**: Set up your OpenAI and ElevenLabs API keys
4. **Run Examples**: Try the sample AI scripts to see the system in action

## Performance Tips

- **Use GPU acceleration** when available for faster AI processing
- **Cache AI models** locally to reduce loading times
- **Optimize memory usage** by closing unused applications
- **Use SSD storage** for faster model loading

Your PC is now ready to run advanced AI for the VR-AI-Game project! 🚀
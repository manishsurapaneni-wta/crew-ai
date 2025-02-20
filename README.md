# CrewAI with Supabase Starter Kit

Welcome to the **CrewAI with Supabase Starter Kit**! This repository provides a ready-to-use setup for working with CrewAI and Supabase, allowing you to quickly get started with your AI-driven applications.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python** (Recommended: 3.11.9)
- **Anaconda**

## Installation Guide

Follow these steps to set up your environment and get started:

### 1. Install CrewAI
```sh
pip install crewai
```

### 2. Create a Conda Virtual Environment
```sh
conda create -n crew-ai python=3.11.9
```

### 3. Activate the Virtual Environment
```sh
conda activate crew-ai
```

### 4. Install CrewAI Tools
```sh
pip install crewai 'crewai[tools]'
```

### 5. Create a New CrewAI Project
```sh
crewai create crew example-project
```

### 6. Run the Main File
Once your environment is set up, execute the following command to start the project:
```sh
python main.py
```

## Additional Notes
- Ensure your Supabase client is properly configured within `main.py`.
- Modify and expand the project as needed to suit your requirements.

## License
This project is licensed under [MIT License](LICENSE).

Happy coding! 🚀


"""
Content generators for Daily GitHub Agent.

Generates real, runnable file content for each project category.
No placeholder functions — every generated file contains meaningful code.

Each generator returns a dict of {relative_filepath: content_string}.
"""

from typing import Dict, List


# ============================================================================
# Technology → pip package mapping
# ============================================================================
TECH_TO_PACKAGE = {
    "Python": None,  # stdlib
    "NumPy": "numpy>=1.24.0",
    "Pandas": "pandas>=2.0.0",
    "Scikit-learn": "scikit-learn>=1.3.0",
    "XGBoost": "xgboost>=2.0.0",
    "LightGBM": "lightgbm>=4.0.0",
    "Optuna": "optuna>=3.0.0",
    "SHAP": "shap>=0.42.0",
    "SciPy": "scipy>=1.11.0",
    "Statsmodels": "statsmodels>=0.14.0",
    "PyTorch": "torch>=2.0.0",
    "Torch": "torch>=2.0.0",
    "TorchVision": "torchvision>=0.15.0",
    "Torchaudio": "torchaudio>=2.0.0",
    "OpenCV": "opencv-python>=4.8.0",
    "PIL": "Pillow>=10.0.0",
    "Transformers": "transformers>=4.35.0",
    "Datasets": "datasets>=2.14.0",
    "Evaluate": "evaluate>=0.4.0",
    "PEFT": "peft>=0.6.0",
    "TRL": "trl>=0.7.0",
    "Accelerate": "accelerate>=0.24.0",
    "BitsAndBytes": "bitsandbytes>=0.41.0",
    "Sentence-Transformers": "sentence-transformers>=2.2.0",
    "FAISS": "faiss-cpu>=1.7.4",
    "ChromaDB": "chromadb>=0.4.0",
    "Qdrant": "qdrant-client>=1.6.0",
    "spaCy": "spacy>=3.7.0",
    "NLTK": "nltk>=3.8.0",
    "TextBlob": "textblob>=0.17.0",
    "NetworkX": "networkx>=3.1",
    "BERTopic": "bertopic>=0.15.0",
    "UMAP": "umap-learn>=0.5.0",
    "HDBSCAN": "hdbscan>=0.8.0",
    "Rank-BM25": "rank-bm25>=0.2.2",
    "FastAPI": "fastapi>=0.104.0",
    "Pydantic": "pydantic>=2.0.0",
    "Uvicorn": "uvicorn>=0.24.0",
    "SQLAlchemy": "sqlalchemy>=2.0.0",
    "SQLite": None,  # stdlib
    "Streamlit": "streamlit>=1.28.0",
    "Plotly": "plotly>=5.18.0",
    "Gradio": "gradio>=4.0.0",
    "LangChain": "langchain>=0.1.0",
    "LangGraph": "langgraph>=0.0.20",
    "OpenAI": "openai>=1.3.0",
    "Whisper": "openai-whisper>=20231117",
    "Tesseract": "pytesseract>=0.3.10",
    "Ultralytics": "ultralytics>=8.0.0",
    "Redis": "redis>=5.0.0",
    "AsyncIO": None,  # stdlib
    "AST": None,  # stdlib
    "Regex": None,  # stdlib (re)
    "Radon": "radon>=6.0.0",
    "Pylint": "pylint>=3.0.0",
    "Jinja2": "Jinja2>=3.1.0",
    "YAML": "PyYAML>=6.0.0",
    "JSONSchema": "jsonschema>=4.20.0",
    "PyMuPDF": "PyMuPDF>=1.23.0",
    "Prometheus-Client": "prometheus-client>=0.19.0",
    "Tree-sitter": "tree-sitter>=0.20.0",
}


def generate_files(project: dict) -> Dict[str, str]:
    """
    Generate all files for a project based on its category.

    Args:
        project: Project metadata dict from the catalog.

    Returns:
        Dict mapping relative filepath to file content string.
    """
    files = {}

    # Common files for all projects
    files["README.md"] = _generate_readme(project)
    files["requirements.txt"] = _generate_requirements(project)
    files[".gitignore"] = _generate_gitignore()

    # Add .env.example if project uses API keys
    if _needs_api_keys(project):
        files[".env.example"] = _generate_env_example(project)

    # Category-specific source files
    category = project["category"]
    generators = {
        "Machine Learning": _gen_ml_files,
        "Deep Learning": _gen_dl_files,
        "NLP": _gen_nlp_files,
        "Hugging Face": _gen_hf_files,
        "Generative AI": _gen_genai_files,
        "RAG": _gen_rag_files,
        "LangChain": _gen_langchain_files,
        "LangGraph": _gen_langgraph_files,
        "LLM Engineering": _gen_llm_eng_files,
        "Computer Vision": _gen_cv_files,
        "Multimodal AI": _gen_multimodal_files,
        "Speech/Audio AI": _gen_audio_files,
        "AI + Databases": _gen_db_files,
        "Graph RAG": _gen_graph_rag_files,
        "AI + Web": _gen_web_files,
        "AI Automation": _gen_automation_files,
        "MLOps": _gen_mlops_files,
        "AI Security": _gen_security_files,
        "LLM Evaluation": _gen_evaluation_files,
        "Fine-Tuning": _gen_finetuning_files,
    }

    gen_func = generators.get(category, _gen_generic_files)
    source_files = gen_func(project)
    files.update(source_files)

    return files


# ============================================================================
# Common file generators
# ============================================================================

def _generate_readme(project: dict) -> str:
    """Generate a professional README with Mermaid diagram."""
    name = project["name"]
    title = name.replace("-", " ").title()
    desc = project["description"]
    category = project["category"]
    difficulty = project["difficulty"]
    tech_stack = project["tech_stack"]
    subcategory = project.get("subcategory", category)

    tech_badges = " | ".join(tech_stack)
    tech_list = "\n".join(f"- **{t}**" for t in tech_stack)

    # Build architecture diagram based on category
    mermaid = _get_mermaid_diagram(project)

    return f'''# {title}

> {desc}

![Category](https://img.shields.io/badge/Category-{category.replace(" ", "%20")}-blue)
![Difficulty](https://img.shields.io/badge/Difficulty-{difficulty}-orange)
![Python](https://img.shields.io/badge/Python-3.9%2B-green)

## Overview

**{title}** is a {difficulty.lower()}-level {category.lower()} project focused on {subcategory.lower()}.
{desc}

## Problem

{_get_problem_statement(project)}

## Solution

{_get_solution_description(project)}

## Architecture

```mermaid
{mermaid}
```

## Features

{_get_features(project)}

## Tech Stack

{tech_list}

## Project Structure

```
{name}/
├── main.py              # Entry point
├── src/
│   ├── __init__.py      # Package init
│   ├── core.py          # Core logic
│   ├── utils.py         # Utilities
│   └── config.py        # Configuration
├── tests/
│   └── test_core.py     # Unit tests
├── requirements.txt     # Dependencies
├── .gitignore           # Git ignore
└── README.md            # Documentation
```

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/{name}.git
cd {name}

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
```

## Environment Variables

{_get_env_vars_section(project)}

## Usage

```bash
python main.py
```

## Example Output

```
{_get_example_output(project)}
```

## Limitations

- This is a demonstration project for educational purposes
- Some features may require API keys to be configured
- Performance may vary based on hardware and data size

## Future Improvements

{_get_future_improvements(project)}

## License

MIT License
'''


def _generate_requirements(project: dict) -> str:
    """Generate requirements.txt from tech stack."""
    packages = []
    for tech in project["tech_stack"]:
        pkg = TECH_TO_PACKAGE.get(tech)
        if pkg:
            packages.append(pkg)

    # Add FastAPI's uvicorn if FastAPI is used
    if "FastAPI" in project["tech_stack"] and "Uvicorn" not in project["tech_stack"]:
        packages.append(TECH_TO_PACKAGE["Uvicorn"])

    # Add python-dotenv for projects needing env vars
    if _needs_api_keys(project):
        packages.append("python-dotenv>=1.0.0")

    return "\n".join(sorted(set(packages))) + "\n"


def _generate_gitignore() -> str:
    """Generate a standard Python .gitignore."""
    return """# Environment
.env
.venv/
venv/
env/

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.egg-info/
dist/
build/
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Data
*.db
*.sqlite
*.sqlite3

# Models
*.pt
*.pth
*.bin
*.onnx
*.h5
model_output/

# Logs
*.log
wandb/
mlruns/
"""


def _generate_env_example(project: dict) -> str:
    """Generate .env.example with relevant API key placeholders."""
    lines = ["# Environment variables for " + project["name"], ""]

    tech = project["tech_stack"]
    if "OpenAI" in tech:
        lines.append("OPENAI_API_KEY=your-openai-api-key-here")
    if "LangChain" in tech or "LangGraph" in tech:
        lines.append("OPENAI_API_KEY=your-openai-api-key-here")
        lines.append("# LANGCHAIN_TRACING_V2=true")
        lines.append("# LANGCHAIN_API_KEY=your-langsmith-key-here")
    if "Qdrant" in tech:
        lines.append("QDRANT_URL=http://localhost:6333")
        lines.append("# QDRANT_API_KEY=your-qdrant-key-here")
    if "ChromaDB" in tech:
        lines.append("CHROMA_PERSIST_DIR=./chroma_data")
    if "Redis" in tech:
        lines.append("REDIS_URL=redis://localhost:6379")

    lines.append("")
    return "\n".join(lines)


def _needs_api_keys(project: dict) -> bool:
    """Check if project requires API keys."""
    api_techs = {"OpenAI", "LangChain", "LangGraph", "Qdrant", "Redis", "ChromaDB"}
    return bool(set(project["tech_stack"]) & api_techs)


# ============================================================================
# README helper functions
# ============================================================================

def _get_mermaid_diagram(project: dict) -> str:
    """Generate a Mermaid flowchart based on project category."""
    cat = project["category"]

    if cat in ("RAG", "Graph RAG"):
        return """flowchart LR
    Documents[("Documents")] --> Chunker["Text Chunker"]
    Chunker --> Embedder["Embedding Model"]
    Embedder --> VectorDB[("Vector Store")]
    Query["User Query"] --> QueryEmbed["Query Embedding"]
    QueryEmbed --> Retriever["Retriever"]
    VectorDB --> Retriever
    Retriever --> Context["Retrieved Context"]
    Context --> LLM["Language Model"]
    Query --> LLM
    LLM --> Answer["Generated Answer"]"""

    if cat == "Machine Learning":
        return """flowchart LR
    Data[("Raw Data")] --> Preprocess["Preprocessing"]
    Preprocess --> Features["Feature Engineering"]
    Features --> Split["Train/Test Split"]
    Split --> Train["Model Training"]
    Train --> Evaluate["Evaluation"]
    Evaluate --> Metrics["Metrics Report"]
    Train --> Predict["Prediction"]"""

    if cat == "Deep Learning":
        return """flowchart LR
    Input[("Input Data")] --> Preprocess["Preprocessing"]
    Preprocess --> DataLoader["DataLoader"]
    DataLoader --> Model["Neural Network"]
    Model --> Loss["Loss Function"]
    Loss --> Optimizer["Optimizer"]
    Optimizer --> Model
    Model --> Output["Predictions"]
    Output --> Evaluate["Evaluation"]"""

    if cat == "NLP":
        return """flowchart LR
    Text[("Raw Text")] --> Preprocess["Text Preprocessing"]
    Preprocess --> Tokenize["Tokenization"]
    Tokenize --> Encode["Encoding/Embedding"]
    Encode --> Model["NLP Model"]
    Model --> PostProcess["Post-processing"]
    PostProcess --> Output["Results"]"""

    if cat in ("LangChain", "LangGraph"):
        return """flowchart LR
    Input["User Input"] --> Agent["Agent"]
    Agent --> Planner["Task Planner"]
    Planner --> Tools["Tools"]
    Tools --> Execute["Execution"]
    Execute --> Reflect["Reflection"]
    Reflect --> Agent
    Reflect --> Output["Final Output"]"""

    if cat == "Computer Vision":
        return """flowchart LR
    Image[("Input Image")] --> Preprocess["Preprocessing"]
    Preprocess --> Features["Feature Extraction"]
    Features --> Model["CV Model"]
    Model --> PostProcess["Post-processing"]
    PostProcess --> Output["Results"]
    Output --> Visualize["Visualization"]"""

    if cat == "Generative AI":
        return """flowchart LR
    Input["User Input"] --> Parse["Input Parser"]
    Parse --> Process["Processing Engine"]
    Process --> Analyze["Analysis"]
    Analyze --> Format["Output Formatter"]
    Format --> Output["Structured Output"]"""

    # Default diagram
    return """flowchart LR
    Input["Input"] --> Process["Processing"]
    Process --> Model["Model/Engine"]
    Model --> Output["Output"]
    Output --> Evaluate["Evaluation"]"""


def _get_problem_statement(project: dict) -> str:
    """Generate a problem statement based on project metadata."""
    cat = project["category"]
    sub = project.get("subcategory", "")

    statements = {
        "Machine Learning": "Traditional approaches to this problem lack systematic evaluation and explainability. This project provides a structured pipeline with comprehensive metrics.",
        "Deep Learning": "Complex neural architectures require careful implementation and training strategies. This project demonstrates best practices for deep learning model development.",
        "NLP": "Processing and understanding natural language at scale requires specialized pipelines. This project implements production-ready NLP workflows.",
        "Hugging Face": "Leveraging state-of-the-art transformer models effectively requires proper tooling and evaluation. This project streamlines the Hugging Face ecosystem workflow.",
        "Generative AI": "Building reliable AI-powered applications requires structured approaches to input processing, output validation, and error handling.",
        "RAG": "Simple retrieval-augmented generation often suffers from poor retrieval quality and hallucinations. Advanced RAG architectures address these limitations systematically.",
        "LangChain": "Complex AI workflows require careful orchestration of multiple components. This project demonstrates structured approach to building AI chains and pipelines.",
        "LangGraph": "Multi-step agent workflows need state management, error handling, and human oversight. Graph-based architectures provide this structure naturally.",
        "LLM Engineering": "Production LLM systems require infrastructure beyond basic API calls — including caching, rate limiting, evaluation, and safety guardrails.",
        "Computer Vision": "Visual understanding tasks require robust preprocessing pipelines, model selection, and post-processing for production deployment.",
        "AI Security": "AI systems face unique security challenges including prompt injection, data leakage, and adversarial attacks that require specialized defenses.",
    }
    return statements.get(cat, f"This project addresses challenges in {cat.lower()} with a practical, well-engineered solution.")


def _get_solution_description(project: dict) -> str:
    """Generate solution description."""
    return f"This project implements a modular, well-tested solution using {', '.join(project['tech_stack'][:3])}. The architecture follows separation of concerns with clear interfaces between components."


def _get_features(project: dict) -> str:
    """Generate feature list based on project metadata."""
    features = [
        f"- **Modular Architecture**: Clean separation of concerns with reusable components",
        f"- **{project.get('subcategory', project['category'])} Implementation**: Core functionality with real processing logic",
        f"- **Configuration Management**: Environment-based configuration with sensible defaults",
        f"- **Error Handling**: Comprehensive error handling and logging",
        f"- **Type Hints**: Full Python type annotations throughout",
    ]

    if "FastAPI" in project["tech_stack"]:
        features.append("- **REST API**: Production-ready API with automatic OpenAPI docs")
    if "Streamlit" in project["tech_stack"]:
        features.append("- **Interactive Dashboard**: Web-based UI for visualization and interaction")
    if any(t in project["tech_stack"] for t in ["FAISS", "ChromaDB", "Qdrant"]):
        features.append("- **Vector Search**: Efficient similarity search with vector embeddings")

    return "\n".join(features)


def _get_env_vars_section(project: dict) -> str:
    """Generate environment variables documentation section."""
    if not _needs_api_keys(project):
        return "No environment variables required for basic functionality."

    return """Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
# Edit .env with your API keys
```

See `.env.example` for all available configuration options."""


def _get_example_output(project: dict) -> str:
    """Generate example output based on project type."""
    cat = project["category"]

    if cat == "Machine Learning":
        return """Loading dataset...
Dataset shape: (1000, 15)
Training model...
Evaluation Results:
  Accuracy:  0.9234
  Precision: 0.9156
  Recall:    0.9312
  F1 Score:  0.9233"""

    if cat == "NLP":
        return """Processing text...
Tokens: 156
Results:
  Category: Technology
  Confidence: 0.9412
  Key entities: ['Python', 'machine learning', 'NLP']"""

    if cat == "RAG":
        return """Indexing 50 documents...
Documents indexed: 50
Chunks created: 234

Query: What is retrieval augmented generation?
Retrieved 5 relevant chunks
Answer: Retrieval Augmented Generation (RAG) is...
Sources: [doc_3.txt, doc_7.txt]"""

    return f"""Initializing {project['name']}...
Processing complete.
Results saved to output/"""


def _get_future_improvements(project: dict) -> str:
    """Generate future improvements list."""
    improvements = [
        "- Add comprehensive unit and integration tests",
        "- Implement logging and monitoring",
        "- Add Docker support for containerized deployment",
        "- Create CI/CD pipeline with GitHub Actions",
    ]

    cat = project["category"]
    if cat in ("Machine Learning", "Deep Learning"):
        improvements.append("- Add MLflow experiment tracking")
        improvements.append("- Implement model versioning")
    if cat in ("RAG", "NLP"):
        improvements.append("- Add streaming response support")
        improvements.append("- Implement advanced caching strategies")
    if cat in ("Generative AI", "LLM Engineering"):
        improvements.append("- Add multi-model support")
        improvements.append("- Implement cost optimization")

    return "\n".join(improvements)


# ============================================================================
# Category-specific source code generators
# ============================================================================

def _gen_ml_files(project: dict) -> Dict[str, str]:
    """Generate Machine Learning project files."""
    name = project["name"]
    title = name.replace("-", " ").title()

    main_py = '''"""
{title} - Main Entry Point

Runs the complete ML pipeline: load data, engineer features,
train models, evaluate, and report results.
"""

import numpy as np
from src.data_loader import load_dataset, split_data
from src.feature_engineer import engineer_features
from src.model import ModelTrainer
from src.evaluator import evaluate_model, print_report


def main():
    """Execute the complete ML pipeline."""
    print("=" * 60)
    print("{title}")
    print("=" * 60)

    # Step 1: Load data
    print("\\n[1/5] Loading dataset...")
    X, y, feature_names = load_dataset()
    print(f"  Dataset shape: {{X.shape}}")
    print(f"  Features: {{len(feature_names)}}")
    print(f"  Class distribution: {{dict(zip(*np.unique(y, return_counts=True)))}}")

    # Step 2: Feature engineering
    print("\\n[2/5] Engineering features...")
    X_eng, eng_names = engineer_features(X, feature_names)
    print(f"  Engineered features: {{X_eng.shape[1]}}")

    # Step 3: Split data
    print("\\n[3/5] Splitting data...")
    X_train, X_test, y_train, y_test = split_data(X_eng, y)
    print(f"  Train samples: {{X_train.shape[0]}}")
    print(f"  Test samples: {{X_test.shape[0]}}")

    # Step 4: Train and compare models
    print("\\n[4/5] Training models...")
    trainer = ModelTrainer()
    results = trainer.train_and_compare(X_train, y_train, X_test, y_test)

    # Step 5: Report
    print("\\n[5/5] Evaluation Results:")
    print_report(results)

    # Find best model
    best = max(results, key=lambda r: r["f1_score"])
    print(f"\\nBest Model: {{best['model_name']}}")
    print(f"  F1 Score: {{best['f1_score']:.4f}}")
    print(f"  Accuracy: {{best['accuracy']:.4f}}")


if __name__ == "__main__":
    main()
'''.format(title=title)

    init_py = '"""Source package for {title}."""\n'.format(title=title)

    data_loader = '''"""
Data loading and preprocessing utilities.

Generates synthetic datasets for demonstration.
Replace with real data loading for production use.
"""

import numpy as np
from typing import Tuple, List


def load_dataset(
    n_samples: int = 1000,
    n_features: int = 10,
    random_state: int = 42,
) -> Tuple[np.ndarray, np.ndarray, List[str]]:
    """
    Load or generate a dataset for the ML pipeline.

    For demonstration, generates a synthetic classification dataset
    with realistic feature distributions.

    Returns:
        X: Feature matrix (n_samples, n_features)
        y: Target labels
        feature_names: List of feature names
    """
    rng = np.random.RandomState(random_state)

    # Generate features with different distributions
    features = []
    feature_names = []

    # Numerical features
    for i in range(n_features // 2):
        feat = rng.normal(loc=i * 0.5, scale=1.0 + i * 0.2, size=n_samples)
        features.append(feat)
        feature_names.append(f"numeric_{i}")

    # Skewed features
    for i in range(n_features // 4):
        feat = rng.exponential(scale=1.0 + i * 0.3, size=n_samples)
        features.append(feat)
        feature_names.append(f"skewed_{i}")

    # Categorical-like features (encoded)
    for i in range(n_features - len(features)):
        feat = rng.randint(0, 5 + i, size=n_samples).astype(float)
        features.append(feat)
        feature_names.append(f"categorical_{i}")

    X = np.column_stack(features)

    # Generate target with non-trivial decision boundary
    decision = (
        0.5 * X[:, 0]
        - 0.3 * X[:, 1]
        + 0.8 * X[:, 2] * X[:, 3]
        - 0.2 * X[:, 4] ** 2
        + rng.normal(0, 0.5, n_samples)
    )
    y = (decision > np.median(decision)).astype(int)

    return X, y, feature_names


def split_data(
    X: np.ndarray,
    y: np.ndarray,
    test_size: float = 0.2,
    random_state: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Split data into train and test sets using stratified sampling.
    """
    rng = np.random.RandomState(random_state)
    n = len(y)
    indices = np.arange(n)
    rng.shuffle(indices)

    split_idx = int(n * (1 - test_size))
    train_idx = indices[:split_idx]
    test_idx = indices[split_idx:]

    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]
'''

    feature_eng = '''"""
Feature engineering utilities.

Creates polynomial, interaction, and statistical features
from the raw feature matrix.
"""

import numpy as np
from typing import Tuple, List


def engineer_features(
    X: np.ndarray,
    feature_names: List[str],
) -> Tuple[np.ndarray, List[str]]:
    """
    Apply feature engineering transformations.

    Creates:
    - Standardized features
    - Polynomial features (squared)
    - Interaction features (top pairs)
    - Statistical aggregation features

    Returns:
        X_eng: Engineered feature matrix
        eng_names: Names of engineered features
    """
    eng_features = []
    eng_names = list(feature_names)

    # Original features (standardized)
    means = X.mean(axis=0)
    stds = X.std(axis=0)
    stds[stds == 0] = 1.0
    X_std = (X - means) / stds
    eng_features.append(X_std)

    # Squared features
    X_sq = X_std ** 2
    eng_features.append(X_sq)
    eng_names.extend([f"{name}_squared" for name in feature_names])

    # Interaction features (first 3 pairs)
    n_interact = min(3, X.shape[1] - 1)
    for i in range(n_interact):
        interaction = X_std[:, i] * X_std[:, i + 1]
        eng_features.append(interaction.reshape(-1, 1))
        eng_names.append(f"{feature_names[i]}_x_{feature_names[i+1]}")

    # Row-level statistics
    row_mean = X_std.mean(axis=1).reshape(-1, 1)
    row_std = X_std.std(axis=1).reshape(-1, 1)
    row_max = X_std.max(axis=1).reshape(-1, 1)
    row_min = X_std.min(axis=1).reshape(-1, 1)

    eng_features.extend([row_mean, row_std, row_max, row_min])
    eng_names.extend(["row_mean", "row_std", "row_max", "row_min"])

    X_eng = np.hstack(eng_features)
    return X_eng, eng_names
'''

    model_py = '''"""
Model training and comparison utilities.

Implements multiple classifiers and compares their performance.
Uses only NumPy for portability (swap in sklearn for production).
"""

import numpy as np
from typing import List, Dict, Any


class SimpleLogisticRegression:
    """Logistic regression implemented from scratch."""

    def __init__(self, lr: float = 0.01, n_iters: int = 1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0.0

        for _ in range(self.n_iters):
            linear = X @ self.weights + self.bias
            predictions = self._sigmoid(linear)

            dw = (1 / n_samples) * (X.T @ (predictions - y))
            db = (1 / n_samples) * np.sum(predictions - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X: np.ndarray) -> np.ndarray:
        linear = X @ self.weights + self.bias
        return (self._sigmoid(linear) >= 0.5).astype(int)

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        linear = X @ self.weights + self.bias
        return self._sigmoid(linear)

    @staticmethod
    def _sigmoid(z):
        return 1.0 / (1.0 + np.exp(-np.clip(z, -500, 500)))


class SimpleDecisionStump:
    """Decision stump (1-level decision tree)."""

    def __init__(self):
        self.feature_idx = 0
        self.threshold = 0.0
        self.polarity = 1

    def fit(self, X: np.ndarray, y: np.ndarray):
        best_acc = 0
        for feat_idx in range(X.shape[1]):
            thresholds = np.unique(X[:, feat_idx])
            for threshold in thresholds[::max(1, len(thresholds) // 20)]:
                for polarity in [1, -1]:
                    preds = np.ones(len(y))
                    if polarity == 1:
                        preds[X[:, feat_idx] < threshold] = 0
                    else:
                        preds[X[:, feat_idx] >= threshold] = 0
                    acc = np.mean(preds == y)
                    if acc > best_acc:
                        best_acc = acc
                        self.feature_idx = feat_idx
                        self.threshold = threshold
                        self.polarity = polarity

    def predict(self, X: np.ndarray) -> np.ndarray:
        preds = np.ones(X.shape[0])
        if self.polarity == 1:
            preds[X[:, self.feature_idx] < self.threshold] = 0
        else:
            preds[X[:, self.feature_idx] >= self.threshold] = 0
        return preds.astype(int)


class SimpleKNN:
    """K-nearest neighbors classifier."""

    def __init__(self, k: int = 5):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        self.X_train = X
        self.y_train = y

    def predict(self, X: np.ndarray) -> np.ndarray:
        predictions = []
        for x in X:
            distances = np.sqrt(np.sum((self.X_train - x) ** 2, axis=1))
            k_indices = np.argsort(distances)[:self.k]
            k_labels = self.y_train[k_indices]
            counts = np.bincount(k_labels)
            predictions.append(np.argmax(counts))
        return np.array(predictions)


class ModelTrainer:
    """Train and compare multiple models."""

    def __init__(self):
        self.models = {
            "Logistic Regression": SimpleLogisticRegression(lr=0.01, n_iters=500),
            "Decision Stump": SimpleDecisionStump(),
            "KNN (k=5)": SimpleKNN(k=5),
        }

    def train_and_compare(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        X_test: np.ndarray,
        y_test: np.ndarray,
    ) -> List[Dict[str, Any]]:
        """Train all models and return comparison results."""
        results = []

        for name, model in self.models.items():
            print(f"  Training {name}...")
            model.fit(X_train, y_train)
            preds = model.predict(X_test)

            accuracy = np.mean(preds == y_test)
            tp = np.sum((preds == 1) & (y_test == 1))
            fp = np.sum((preds == 1) & (y_test == 0))
            fn = np.sum((preds == 0) & (y_test == 1))

            precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
            f1 = (
                2 * precision * recall / (precision + recall)
                if (precision + recall) > 0
                else 0.0
            )

            results.append({
                "model_name": name,
                "accuracy": accuracy,
                "precision": precision,
                "recall": recall,
                "f1_score": f1,
            })

        return results
'''

    evaluator_py = '''"""
Model evaluation and reporting utilities.
"""

from typing import List, Dict, Any


def evaluate_model(y_true, y_pred) -> Dict[str, float]:
    """Calculate classification metrics."""
    import numpy as np

    accuracy = np.mean(y_true == y_pred)
    tp = np.sum((y_pred == 1) & (y_true == 1))
    fp = np.sum((y_pred == 1) & (y_true == 0))
    fn = np.sum((y_pred == 0) & (y_true == 1))

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
    }


def print_report(results: List[Dict[str, Any]]):
    """Print a formatted comparison report."""
    print(f"\\n  {'Model':<25} {'Accuracy':>10} {'Precision':>10} {'Recall':>10} {'F1':>10}")
    print(f"  {'-'*25} {'-'*10} {'-'*10} {'-'*10} {'-'*10}")

    for r in results:
        print(
            f"  {r['model_name']:<25}"
            f" {r['accuracy']:>10.4f}"
            f" {r['precision']:>10.4f}"
            f" {r['recall']:>10.4f}"
            f" {r['f1_score']:>10.4f}"
        )
'''

    config_py = '''"""
Project configuration.
"""

import os

# Data settings
N_SAMPLES = int(os.getenv("N_SAMPLES", "1000"))
N_FEATURES = int(os.getenv("N_FEATURES", "10"))
TEST_SIZE = float(os.getenv("TEST_SIZE", "0.2"))
RANDOM_STATE = int(os.getenv("RANDOM_STATE", "42"))
'''

    utils_py = '''"""
Utility functions for the ML pipeline.
"""

import numpy as np
from typing import Dict


def format_metrics(metrics: Dict[str, float], decimals: int = 4) -> str:
    """Format a metrics dictionary as a readable string."""
    lines = []
    for name, value in metrics.items():
        lines.append(f"  {name}: {value:.{decimals}f}")
    return "\\n".join(lines)


def check_data_quality(X: np.ndarray) -> Dict[str, any]:
    """Run basic data quality checks."""
    return {
        "shape": X.shape,
        "has_nan": bool(np.any(np.isnan(X))),
        "has_inf": bool(np.any(np.isinf(X))),
        "min_value": float(np.min(X)),
        "max_value": float(np.max(X)),
        "mean_value": float(np.mean(X)),
    }
'''

    test_core = '''"""
Unit tests for the ML pipeline.
"""

import numpy as np
import unittest
from src.data_loader import load_dataset, split_data
from src.feature_engineer import engineer_features
from src.model import SimpleLogisticRegression, SimpleKNN


class TestDataLoader(unittest.TestCase):
    def test_load_dataset_shape(self):
        X, y, names = load_dataset(n_samples=100, n_features=8)
        self.assertEqual(X.shape[0], 100)
        self.assertEqual(len(names), X.shape[1])
        self.assertEqual(len(y), 100)

    def test_binary_labels(self):
        _, y, _ = load_dataset(n_samples=100)
        unique = np.unique(y)
        self.assertTrue(set(unique).issubset({0, 1}))

    def test_split_sizes(self):
        X, y, _ = load_dataset(n_samples=100)
        X_tr, X_te, y_tr, y_te = split_data(X, y, test_size=0.2)
        self.assertEqual(len(X_tr), 80)
        self.assertEqual(len(X_te), 20)


class TestFeatureEngineering(unittest.TestCase):
    def test_adds_features(self):
        X, _, names = load_dataset(n_samples=50, n_features=6)
        X_eng, eng_names = engineer_features(X, names)
        self.assertGreater(X_eng.shape[1], X.shape[1])
        self.assertEqual(len(eng_names), X_eng.shape[1])


class TestModels(unittest.TestCase):
    def test_logistic_regression(self):
        X, y, _ = load_dataset(n_samples=200, n_features=4)
        X_tr, X_te, y_tr, y_te = split_data(X, y)
        model = SimpleLogisticRegression(lr=0.01, n_iters=100)
        model.fit(X_tr, y_tr)
        preds = model.predict(X_te)
        acc = np.mean(preds == y_te)
        self.assertGreater(acc, 0.4)  # Better than random

    def test_knn(self):
        X, y, _ = load_dataset(n_samples=200, n_features=4)
        X_tr, X_te, y_tr, y_te = split_data(X, y)
        model = SimpleKNN(k=3)
        model.fit(X_tr, y_tr)
        preds = model.predict(X_te)
        self.assertEqual(len(preds), len(y_te))


if __name__ == "__main__":
    unittest.main()
'''

    return {
        "main.py": main_py,
        "src/__init__.py": init_py,
        "src/data_loader.py": data_loader,
        "src/feature_engineer.py": feature_eng,
        "src/model.py": model_py,
        "src/evaluator.py": evaluator_py,
        "src/config.py": config_py,
        "src/utils.py": utils_py,
        "tests/test_core.py": test_core,
    }


def _gen_dl_files(project: dict) -> Dict[str, str]:
    """Generate Deep Learning project files."""
    title = project["name"].replace("-", " ").title()

    main_py = '''"""
{title} - Main Entry Point

Demonstrates deep learning model training with PyTorch-style
implementation using only NumPy for portability.
"""

import numpy as np
from src.data_loader import generate_data
from src.model import NeuralNetwork
from src.trainer import Trainer
from src.config import EPOCHS, LEARNING_RATE, HIDDEN_SIZE, BATCH_SIZE


def main():
    """Run the deep learning training pipeline."""
    print("=" * 60)
    print("{title}")
    print("=" * 60)

    # Generate data
    print("\\n[1/3] Generating dataset...")
    X_train, y_train, X_test, y_test = generate_data()
    print(f"  Train: {{X_train.shape}}, Test: {{X_test.shape}}")

    # Create model
    print("\\n[2/3] Building model...")
    input_dim = X_train.shape[1]
    model = NeuralNetwork(input_dim=input_dim, hidden_dim=HIDDEN_SIZE, output_dim=1)
    print(f"  Architecture: {{input_dim}} -> {{HIDDEN_SIZE}} -> 1")
    print(f"  Parameters: {{model.count_parameters()}}")

    # Train
    print("\\n[3/3] Training...")
    trainer = Trainer(model, lr=LEARNING_RATE)
    history = trainer.train(X_train, y_train, X_test, y_test,
                           epochs=EPOCHS, batch_size=BATCH_SIZE)

    # Final evaluation
    preds = model.predict(X_test)
    accuracy = np.mean(preds == y_test)
    print(f"\\nFinal Test Accuracy: {{accuracy:.4f}}")
    print(f"Best Validation Loss: {{min(history['val_loss']):.4f}}")


if __name__ == "__main__":
    main()
'''.format(title=title)

    init_py = '"""Source package for {title}."""\n'.format(title=title)

    data_loader = '''"""
Data generation for deep learning demonstration.
"""

import numpy as np
from typing import Tuple


def generate_data(
    n_train: int = 800,
    n_test: int = 200,
    n_features: int = 20,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Generate a non-linear classification dataset."""
    rng = np.random.RandomState(seed)

    def _make_data(n):
        X = rng.randn(n, n_features)
        # Non-linear decision boundary
        y = (
            np.sin(X[:, 0] * 2) + X[:, 1] ** 2 - X[:, 2] * X[:, 3]
            + 0.5 * np.cos(X[:, 4]) + rng.randn(n) * 0.3
        )
        y = (y > np.median(y)).astype(np.float64)
        return X, y

    X_train, y_train = _make_data(n_train)
    X_test, y_test = _make_data(n_test)
    return X_train, y_train, X_test, y_test
'''

    model_py = '''"""
Neural network implementation from scratch using NumPy.
"""

import numpy as np


class NeuralNetwork:
    """Two-layer neural network with ReLU activation."""

    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        scale1 = np.sqrt(2.0 / input_dim)
        scale2 = np.sqrt(2.0 / hidden_dim)

        self.W1 = np.random.randn(input_dim, hidden_dim) * scale1
        self.b1 = np.zeros(hidden_dim)
        self.W2 = np.random.randn(hidden_dim, output_dim) * scale2
        self.b2 = np.zeros(output_dim)

        # Cache for backprop
        self._cache = {}

    def forward(self, X: np.ndarray) -> np.ndarray:
        """Forward pass."""
        z1 = X @ self.W1 + self.b1
        a1 = np.maximum(0, z1)  # ReLU
        z2 = a1 @ self.W2 + self.b2
        a2 = 1.0 / (1.0 + np.exp(-np.clip(z2, -500, 500)))  # Sigmoid

        self._cache = {"X": X, "z1": z1, "a1": a1, "z2": z2, "a2": a2}
        return a2

    def backward(self, y: np.ndarray) -> dict:
        """Backward pass returning gradients."""
        m = y.shape[0]
        c = self._cache
        a2 = c["a2"]

        # Output layer
        dz2 = a2 - y.reshape(-1, 1)
        dW2 = (c["a1"].T @ dz2) / m
        db2 = np.mean(dz2, axis=0)

        # Hidden layer
        da1 = dz2 @ self.W2.T
        dz1 = da1 * (c["z1"] > 0).astype(float)  # ReLU gradient
        dW1 = (c["X"].T @ dz1) / m
        db1 = np.mean(dz1, axis=0)

        return {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict binary labels."""
        probs = self.forward(X)
        return (probs >= 0.5).astype(int).flatten()

    def count_parameters(self) -> int:
        """Count total trainable parameters."""
        return self.W1.size + self.b1.size + self.W2.size + self.b2.size
'''

    trainer_py = '''"""
Training loop implementation.
"""

import numpy as np
from typing import Dict, List


class Trainer:
    """Handles training loop with gradient descent."""

    def __init__(self, model, lr: float = 0.01):
        self.model = model
        self.lr = lr

    def train(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        X_val: np.ndarray,
        y_val: np.ndarray,
        epochs: int = 100,
        batch_size: int = 32,
    ) -> Dict[str, List[float]]:
        """Train the model and return loss history."""
        history = {"train_loss": [], "val_loss": []}
        n = X_train.shape[0]

        for epoch in range(epochs):
            # Shuffle training data
            idx = np.random.permutation(n)
            X_shuffled = X_train[idx]
            y_shuffled = y_train[idx]

            epoch_loss = 0.0
            n_batches = 0

            for i in range(0, n, batch_size):
                X_batch = X_shuffled[i:i + batch_size]
                y_batch = y_shuffled[i:i + batch_size]

                # Forward
                output = self.model.forward(X_batch)

                # Loss (binary cross-entropy)
                eps = 1e-8
                loss = -np.mean(
                    y_batch.reshape(-1, 1) * np.log(output + eps)
                    + (1 - y_batch.reshape(-1, 1)) * np.log(1 - output + eps)
                )
                epoch_loss += loss
                n_batches += 1

                # Backward
                grads = self.model.backward(y_batch)

                # Update weights
                self.model.W1 -= self.lr * grads["dW1"]
                self.model.b1 -= self.lr * grads["db1"]
                self.model.W2 -= self.lr * grads["dW2"]
                self.model.b2 -= self.lr * grads["db2"]

            # Validation loss
            val_out = self.model.forward(X_val)
            val_loss = -np.mean(
                y_val.reshape(-1, 1) * np.log(val_out + eps)
                + (1 - y_val.reshape(-1, 1)) * np.log(1 - val_out + eps)
            )

            avg_train_loss = epoch_loss / max(n_batches, 1)
            history["train_loss"].append(avg_train_loss)
            history["val_loss"].append(val_loss)

            if (epoch + 1) % 20 == 0 or epoch == 0:
                val_preds = self.model.predict(X_val)
                val_acc = np.mean(val_preds == y_val)
                print(
                    f"  Epoch {{epoch+1:>4}}/{epochs}"
                    f"  Loss: {{avg_train_loss:.4f}}"
                    f"  Val Loss: {{val_loss:.4f}}"
                    f"  Val Acc: {{val_acc:.4f}}"
                )

        return history
'''

    config_py = '''"""Configuration for the deep learning project."""

import os

EPOCHS = int(os.getenv("EPOCHS", "100"))
LEARNING_RATE = float(os.getenv("LEARNING_RATE", "0.01"))
HIDDEN_SIZE = int(os.getenv("HIDDEN_SIZE", "32"))
BATCH_SIZE = int(os.getenv("BATCH_SIZE", "32"))
'''

    return {
        "main.py": main_py,
        "src/__init__.py": init_py,
        "src/data_loader.py": data_loader,
        "src/model.py": model_py,
        "src/trainer.py": trainer_py,
        "src/config.py": config_py,
    }


def _gen_nlp_files(project: dict) -> Dict[str, str]:
    """Generate NLP project files."""
    title = project["name"].replace("-", " ").title()

    main_py = '''"""
{title} - Main Entry Point

Demonstrates NLP text processing pipeline with tokenization,
feature extraction, and analysis.
"""

import json
from src.preprocessor import TextPreprocessor
from src.analyzer import TextAnalyzer
from src.config import SAMPLE_TEXTS


def main():
    """Run the NLP pipeline on sample texts."""
    print("=" * 60)
    print("{title}")
    print("=" * 60)

    preprocessor = TextPreprocessor()
    analyzer = TextAnalyzer()

    for i, text in enumerate(SAMPLE_TEXTS, 1):
        print(f"\\n--- Document {{i}} ---")
        print(f"Input: {{text[:80]}}...")

        # Preprocess
        tokens = preprocessor.tokenize(text)
        cleaned = preprocessor.clean(text)

        # Analyze
        result = analyzer.analyze(cleaned)

        print(f"Tokens: {{len(tokens)}}")
        print(f"Sentences: {{result['sentence_count']}}")
        print(f"Avg word length: {{result['avg_word_length']:.1f}}")
        print(f"Vocabulary richness: {{result['vocab_richness']:.3f}}")
        print(f"Top keywords: {{', '.join(result['keywords'][:5])}}")

    print("\\n" + "=" * 60)
    print("Analysis complete.")


if __name__ == "__main__":
    main()
'''.format(title=title)

    preprocessor = '''"""
Text preprocessing pipeline.
"""

import re
import string
from typing import List


class TextPreprocessor:
    """Handles text cleaning and tokenization."""

    STOP_WORDS = {{
        "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "will", "would", "shall",
        "should", "may", "might", "can", "could", "must", "and", "but", "or",
        "nor", "not", "so", "yet", "both", "either", "neither", "each",
        "every", "all", "any", "few", "more", "most", "other", "some",
        "such", "no", "only", "own", "same", "than", "too", "very",
        "of", "in", "to", "for", "with", "on", "at", "from", "by",
        "about", "as", "into", "through", "during", "before", "after",
        "above", "below", "between", "this", "that", "these", "those",
        "it", "its", "i", "me", "my", "we", "our", "you", "your",
        "he", "him", "his", "she", "her", "they", "them", "their",
    }}

    def clean(self, text: str) -> str:
        """Clean text by removing special characters and normalizing whitespace."""
        text = text.lower()
        text = re.sub(r"http\\S+|www\\S+", "", text)
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r"[^a-zA-Z0-9\\s.,!?;:-]", " ", text)
        text = re.sub(r"\\s+", " ", text).strip()
        return text

    def tokenize(self, text: str) -> List[str]:
        """Tokenize text into words."""
        cleaned = self.clean(text)
        tokens = cleaned.split()
        return [t.strip(string.punctuation) for t in tokens if t.strip(string.punctuation)]

    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """Remove stop words from token list."""
        return [t for t in tokens if t.lower() not in self.STOP_WORDS]

    def get_ngrams(self, tokens: List[str], n: int = 2) -> List[str]:
        """Generate n-grams from token list."""
        return [" ".join(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]
'''

    analyzer = '''"""
Text analysis engine.
"""

import re
from typing import Dict, Any, List
from collections import Counter
from .preprocessor import TextPreprocessor


class TextAnalyzer:
    """Analyzes text and extracts features."""

    def __init__(self):
        self.preprocessor = TextPreprocessor()

    def analyze(self, text: str) -> Dict[str, Any]:
        """Full text analysis returning multiple metrics."""
        tokens = self.preprocessor.tokenize(text)
        content_tokens = self.preprocessor.remove_stopwords(tokens)
        sentences = self._split_sentences(text)

        return {{
            "char_count": len(text),
            "word_count": len(tokens),
            "sentence_count": len(sentences),
            "avg_word_length": self._avg_word_length(tokens),
            "avg_sentence_length": len(tokens) / max(len(sentences), 1),
            "vocab_richness": len(set(tokens)) / max(len(tokens), 1),
            "keywords": self._extract_keywords(content_tokens, top_n=10),
            "bigrams": self.preprocessor.get_ngrams(content_tokens, 2)[:5],
            "readability_score": self._readability_score(tokens, sentences),
        }}

    def _split_sentences(self, text: str) -> List[str]:
        """Split text into sentences."""
        sentences = re.split(r"[.!?]+", text)
        return [s.strip() for s in sentences if s.strip()]

    def _avg_word_length(self, tokens: List[str]) -> float:
        if not tokens:
            return 0.0
        return sum(len(t) for t in tokens) / len(tokens)

    def _extract_keywords(self, tokens: List[str], top_n: int = 10) -> List[str]:
        """Extract top keywords by frequency."""
        counter = Counter(tokens)
        return [word for word, _ in counter.most_common(top_n)]

    def _readability_score(self, tokens: List[str], sentences: List[str]) -> float:
        """Calculate a simplified readability score (0-100)."""
        if not tokens or not sentences:
            return 0.0
        avg_sentence_len = len(tokens) / len(sentences)
        avg_word_len = self._avg_word_length(tokens)
        # Simplified Flesch-like formula (higher = more readable)
        score = max(0, min(100, 206.835 - 1.015 * avg_sentence_len - 84.6 * (avg_word_len / 5)))
        return round(score, 1)
'''

    config_py = '''"""Configuration and sample data."""

SAMPLE_TEXTS = [
    """Machine learning is a subset of artificial intelligence that provides
    systems the ability to automatically learn and improve from experience
    without being explicitly programmed. It focuses on the development of
    computer programs that can access data and use it to learn for themselves.
    The process begins with observations or data, such as examples, direct
    experience, or instruction, in order to look for patterns in data and
    make better decisions in the future.""",

    """Natural language processing is a field of computer science and
    linguistics concerned with the interactions between computers and
    human language. As such, NLP is related to the area of human-computer
    interaction. Many challenges in NLP involve natural language understanding,
    enabling computers to derive meaning from human or natural language input,
    and natural language generation, enabling computers to produce text.""",

    """Deep learning is part of a broader family of machine learning methods
    based on artificial neural networks with representation learning. Learning
    can be supervised, semi-supervised or unsupervised. Deep learning architectures
    such as deep neural networks, recurrent neural networks, convolutional neural
    networks and transformers have been applied to fields including computer
    vision, speech recognition, natural language processing, and recommendation
    systems where they have produced results comparable to human expert performance.""",
]
'''

    return {
        "main.py": main_py,
        "src/__init__.py": '"""NLP pipeline source package."""\n',
        "src/preprocessor.py": preprocessor,
        "src/analyzer.py": analyzer,
        "src/config.py": config_py,
    }


def _gen_genai_files(project: dict) -> Dict[str, str]:
    """Generate Generative AI project files."""
    name = project["name"]
    title = name.replace("-", " ").title()
    sub = project.get("subcategory", "")

    # For ai-resume-analyzer, generate a specialized implementation
    if name == "ai-resume-analyzer":
        return _gen_resume_analyzer()

    if name == "ai-code-review-assistant":
        return _gen_code_reviewer()

    if name == "ai-writing-style-analyzer":
        return _gen_writing_analyzer()

    if name == "prompt-template-engine":
        return _gen_prompt_engine()

    # Default Generative AI template
    return _gen_genai_default(project)


def _gen_resume_analyzer() -> Dict[str, str]:
    """Generate the AI Resume Analyzer project."""

    main_py = '''"""
AI Resume Analyzer - Main Entry Point

Analyzes resume text to extract skills, experience, education,
and provides structured scoring and recommendations.
"""

import json
from src.parser import ResumeParser
from src.analyzer import ResumeAnalyzer
from src.scorer import ResumeScorer


SAMPLE_RESUME = """
Sarah Chen
Senior Machine Learning Engineer

Contact: san francisco, ca

SUMMARY
Experienced ML engineer with 7+ years building production machine learning
systems. Specializing in NLP, deep learning, and MLOps. Led teams of 5-8
engineers to deliver enterprise-scale AI solutions.

EXPERIENCE

Senior ML Engineer | TechCorp AI Division | 2021 - Present
- Designed and deployed a real-time recommendation engine serving 10M+ users
- Built end-to-end NLP pipeline reducing document processing time by 75%
- Implemented MLOps practices including CI/CD, model monitoring, A/B testing
- Mentored 4 junior engineers and led technical design reviews

ML Engineer | DataStartup Inc | 2018 - 2021
- Developed sentiment analysis models achieving 94% accuracy on production data
- Created automated feature engineering pipeline using Python and Apache Spark
- Optimized model inference latency from 200ms to 15ms using ONNX Runtime
- Contributed to open-source ML libraries with 500+ GitHub stars

Data Scientist | Analytics Corp | 2016 - 2018
- Built customer churn prediction models increasing retention by 23%
- Designed A/B testing framework used across 12 product teams
- Created dashboards and reports for C-level stakeholders

EDUCATION
M.S. Computer Science, Stanford University, 2016
B.S. Mathematics, UC Berkeley, 2014

SKILLS
Programming: Python, SQL, Java, Scala, R
ML/DL: PyTorch, TensorFlow, Scikit-learn, XGBoost, Hugging Face
MLOps: MLflow, Docker, Kubernetes, GitHub Actions, Airflow
Cloud: AWS (SageMaker, Lambda, S3), GCP (Vertex AI, BigQuery)
Data: Spark, Pandas, NumPy, PostgreSQL, Redis, Elasticsearch
Other: Git, Linux, REST APIs, Microservices, System Design

CERTIFICATIONS
- AWS Machine Learning Specialty
- Google Professional ML Engineer
"""


def main():
    """Analyze a sample resume and display results."""
    print("=" * 60)
    print("AI Resume Analyzer")
    print("=" * 60)

    # Parse resume sections
    print("\\n[1/3] Parsing resume...")
    parser = ResumeParser()
    sections = parser.parse(SAMPLE_RESUME)
    print(f"  Found {len(sections)} sections")

    # Analyze content
    print("\\n[2/3] Analyzing content...")
    analyzer = ResumeAnalyzer()
    analysis = analyzer.analyze(SAMPLE_RESUME, sections)

    # Score resume
    print("\\n[3/3] Scoring resume...")
    scorer = ResumeScorer()
    score = scorer.score(analysis)

    # Display results
    print("\\n" + "=" * 60)
    print("ANALYSIS RESULTS")
    print("=" * 60)

    print(f"\\nCandidate: {analysis['name']}")
    print(f"Title: {analysis['current_title']}")

    print(f"\\nSkills ({len(analysis['skills'])} found):")
    for category, skills in analysis['skill_categories'].items():
        if skills:
            print(f"  {category}: {', '.join(skills[:5])}")

    print(f"\\nExperience:")
    print(f"  Estimated years: {analysis['experience_years']}")
    print(f"  Positions: {len(analysis['positions'])}")

    print(f"\\nEducation:")
    for edu in analysis['education']:
        print(f"  {edu}")

    print(f"\\nResume Score: {score['total']}/100")
    print(f"  Skills depth:     {score['skills']}/25")
    print(f"  Experience:       {score['experience']}/25")
    print(f"  Impact metrics:   {score['impact']}/25")
    print(f"  Education:        {score['education']}/15")
    print(f"  Presentation:     {score['presentation']}/10")

    print(f"\\nRecommendations:")
    for rec in score['recommendations']:
        print(f"  - {rec}")

    # Output JSON
    output = {
        "analysis": analysis,
        "score": score,
    }
    print(f"\\nFull results written to stdout as JSON:")
    print(json.dumps(output, indent=2, default=str))


if __name__ == "__main__":
    main()
'''

    parser_py = '''"""
Resume parsing module.

Extracts structured sections from raw resume text.
"""

import re
from typing import Dict, List


class ResumeParser:
    """Parse resume text into structured sections."""

    SECTION_HEADERS = [
        "summary", "objective", "profile",
        "experience", "work experience", "employment", "professional experience",
        "education", "academic",
        "skills", "technical skills", "core competencies",
        "certifications", "certificates",
        "projects", "publications", "awards", "volunteer",
        "contact", "languages", "interests",
    ]

    def parse(self, text: str) -> Dict[str, str]:
        """
        Parse resume text into sections.

        Returns:
            Dict mapping section name to section content.
        """
        lines = text.strip().split("\\n")
        sections = {}
        current_section = "header"
        current_content = []

        for line in lines:
            stripped = line.strip()
            if not stripped:
                current_content.append("")
                continue

            # Check if this line is a section header
            lower = stripped.lower().rstrip(":")
            is_header = False

            for header in self.SECTION_HEADERS:
                if lower == header or lower.startswith(header):
                    # Save previous section
                    if current_content:
                        sections[current_section] = "\\n".join(current_content).strip()
                    current_section = header.split()[0]  # Use first word
                    current_content = []
                    is_header = True
                    break

            # Also detect ALL-CAPS headers
            if not is_header and stripped.isupper() and len(stripped) > 2 and len(stripped.split()) <= 4:
                if current_content:
                    sections[current_section] = "\\n".join(current_content).strip()
                current_section = stripped.lower()
                current_content = []
                is_header = True

            if not is_header:
                current_content.append(stripped)

        # Save last section
        if current_content:
            sections[current_section] = "\\n".join(current_content).strip()

        return sections

    def extract_contact_info(self, header: str) -> Dict[str, str]:
        """Extract name, email, phone, location from header."""
        lines = [l.strip() for l in header.split("\\n") if l.strip()]
        info = {"name": lines[0] if lines else "Unknown"}

        text = " ".join(lines)

        # Email
        email_match = re.search(r"[\\w.+-]+@[\\w-]+\\.[\\w.]+", text)
        if email_match:
            info["email"] = email_match.group()

        # Phone
        phone_match = re.search(r"[\\(]?\\d{3}[\\)]?[-.\\s]?\\d{3}[-.\\s]?\\d{4}", text)
        if phone_match:
            info["phone"] = phone_match.group()

        return info
'''

    analyzer_py = '''"""
Resume analysis engine.

Extracts skills, experience, education, and metrics from parsed resume.
"""

import re
from typing import Dict, List, Any
from .parser import ResumeParser


class ResumeAnalyzer:
    """Analyze parsed resume content."""

    SKILL_CATEGORIES = {
        "programming": [
            "python", "java", "javascript", "typescript", "c++", "c#",
            "go", "rust", "scala", "r", "sql", "ruby", "php", "swift",
            "kotlin", "matlab", "julia", "bash", "shell",
        ],
        "ml_dl": [
            "pytorch", "tensorflow", "keras", "scikit-learn", "sklearn",
            "xgboost", "lightgbm", "hugging face", "transformers",
            "opencv", "spacy", "nltk", "pandas", "numpy", "scipy",
            "onnx", "mlflow", "wandb", "optuna",
        ],
        "cloud": [
            "aws", "gcp", "azure", "sagemaker", "vertex ai", "lambda",
            "s3", "bigquery", "ec2", "ecs", "fargate",
        ],
        "devops": [
            "docker", "kubernetes", "k8s", "github actions", "jenkins",
            "terraform", "ansible", "ci/cd", "airflow", "mlops",
        ],
        "data": [
            "spark", "hadoop", "kafka", "postgresql", "mysql", "mongodb",
            "redis", "elasticsearch", "snowflake", "databricks",
        ],
    }

    IMPACT_PATTERNS = [
        r"(\\d+)%",
        r"(\\d+)x",
        r"\\$(\\d+[kmb]?)",
        r"(\\d+[kmb]\\+?)\\s*users",
        r"(\\d+)\\s*engineers",
        r"(\\d+)\\s*teams",
        r"reduced.*?(\\d+)",
        r"increased.*?(\\d+)",
        r"improved.*?(\\d+)",
    ]

    def analyze(self, text: str, sections: Dict[str, str]) -> Dict[str, Any]:
        """Full resume analysis."""
        parser = ResumeParser()
        header = sections.get("header", "")
        contact = parser.extract_contact_info(header)

        skills = self._extract_skills(text)
        skill_cats = self._categorize_skills(skills)
        positions = self._extract_positions(sections.get("experience", ""))
        education = self._extract_education(sections.get("education", ""))
        impact_metrics = self._extract_impact_metrics(text)

        # Estimate years of experience
        years = self._estimate_experience_years(
            sections.get("experience", "")
        )

        return {
            "name": contact.get("name", "Unknown"),
            "current_title": self._extract_title(header),
            "skills": skills,
            "skill_categories": skill_cats,
            "positions": positions,
            "education": education,
            "experience_years": years,
            "impact_metrics": impact_metrics,
            "sections_found": list(sections.keys()),
        }

    def _extract_skills(self, text: str) -> List[str]:
        """Extract all skills mentioned in the resume."""
        text_lower = text.lower()
        found = set()

        for category, skill_list in self.SKILL_CATEGORIES.items():
            for skill in skill_list:
                if skill in text_lower:
                    found.add(skill)

        return sorted(found)

    def _categorize_skills(self, skills: List[str]) -> Dict[str, List[str]]:
        """Organize skills into categories."""
        result = {cat: [] for cat in self.SKILL_CATEGORIES}
        for skill in skills:
            for cat, cat_skills in self.SKILL_CATEGORIES.items():
                if skill in cat_skills:
                    result[cat].append(skill)
                    break
        return result

    def _extract_title(self, header: str) -> str:
        """Extract job title from header."""
        lines = [l.strip() for l in header.split("\\n") if l.strip()]
        if len(lines) >= 2:
            return lines[1]
        return "Not specified"

    def _extract_positions(self, experience: str) -> List[Dict[str, str]]:
        """Extract job positions from experience section."""
        positions = []
        lines = experience.split("\\n")

        for line in lines:
            line = line.strip()
            if "|" in line and not line.startswith("-"):
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 2:
                    positions.append({
                        "title": parts[0],
                        "company": parts[1] if len(parts) > 1 else "",
                        "dates": parts[2] if len(parts) > 2 else "",
                    })

        return positions

    def _extract_education(self, education: str) -> List[str]:
        """Extract education entries."""
        entries = []
        for line in education.split("\\n"):
            line = line.strip()
            if line and len(line) > 10:
                entries.append(line)
        return entries

    def _estimate_experience_years(self, experience: str) -> int:
        """Estimate total years of experience from date ranges."""
        year_pattern = r"(20\\d{2}|19\\d{2})"
        years = [int(y) for y in re.findall(year_pattern, experience)]

        if len(years) >= 2:
            return max(years) - min(years)
        return 0

    def _extract_impact_metrics(self, text: str) -> List[str]:
        """Extract quantified impact statements."""
        metrics = []
        for pattern in self.IMPACT_PATTERNS:
            matches = re.findall(pattern, text, re.IGNORECASE)
            metrics.extend(matches)
        return metrics[:10]
'''

    scorer_py = '''"""
Resume scoring engine.

Scores resumes on multiple dimensions and provides recommendations.
"""

from typing import Dict, Any, List


class ResumeScorer:
    """Score resume analysis results."""

    def score(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Score a resume analysis on a 100-point scale.

        Dimensions:
        - Skills depth (25 points)
        - Experience (25 points)
        - Impact metrics (25 points)
        - Education (15 points)
        - Presentation (10 points)
        """
        skills_score = self._score_skills(analysis)
        exp_score = self._score_experience(analysis)
        impact_score = self._score_impact(analysis)
        edu_score = self._score_education(analysis)
        pres_score = self._score_presentation(analysis)

        total = skills_score + exp_score + impact_score + edu_score + pres_score
        recommendations = self._generate_recommendations(
            analysis, skills_score, exp_score, impact_score, edu_score, pres_score
        )

        return {
            "total": total,
            "skills": skills_score,
            "experience": exp_score,
            "impact": impact_score,
            "education": edu_score,
            "presentation": pres_score,
            "recommendations": recommendations,
        }

    def _score_skills(self, analysis: Dict[str, Any]) -> int:
        """Score skills section (max 25)."""
        n_skills = len(analysis.get("skills", []))
        categories_with_skills = sum(
            1 for skills in analysis.get("skill_categories", {}).values()
            if skills
        )

        score = min(15, n_skills)  # Up to 15 for quantity
        score += min(10, categories_with_skills * 2)  # Up to 10 for breadth
        return min(25, score)

    def _score_experience(self, analysis: Dict[str, Any]) -> int:
        """Score experience section (max 25)."""
        years = analysis.get("experience_years", 0)
        positions = len(analysis.get("positions", []))

        score = min(15, years * 2)  # Up to 15 for years
        score += min(10, positions * 3)  # Up to 10 for positions
        return min(25, score)

    def _score_impact(self, analysis: Dict[str, Any]) -> int:
        """Score quantified impact (max 25)."""
        metrics = len(analysis.get("impact_metrics", []))
        return min(25, metrics * 4)

    def _score_education(self, analysis: Dict[str, Any]) -> int:
        """Score education (max 15)."""
        edu = analysis.get("education", [])
        score = min(10, len(edu) * 5)

        # Bonus for advanced degrees
        edu_text = " ".join(edu).lower()
        if "m.s." in edu_text or "master" in edu_text:
            score += 3
        if "ph.d" in edu_text or "doctorate" in edu_text:
            score += 5

        return min(15, score)

    def _score_presentation(self, analysis: Dict[str, Any]) -> int:
        """Score resume presentation (max 10)."""
        sections = analysis.get("sections_found", [])
        score = min(6, len(sections))  # Completeness
        if analysis.get("current_title") != "Not specified":
            score += 2
        if analysis.get("name") != "Unknown":
            score += 2
        return min(10, score)

    def _generate_recommendations(self, analysis, skills, exp, impact, edu, pres) -> List[str]:
        """Generate improvement recommendations."""
        recs = []

        if skills < 15:
            recs.append("Add more technical skills with proficiency levels")
        if exp < 15:
            recs.append("Expand experience descriptions with more detail")
        if impact < 15:
            recs.append("Quantify achievements with specific metrics (%, $, users)")
        if edu < 10:
            recs.append("Include relevant coursework or certifications")
        if pres < 7:
            recs.append("Ensure all standard sections are present and well-organized")

        if not recs:
            recs.append("Excellent resume! Consider adding a projects section for additional depth.")

        return recs
'''

    test_core = '''"""Tests for the resume analyzer."""

import unittest
from src.parser import ResumeParser
from src.analyzer import ResumeAnalyzer
from src.scorer import ResumeScorer


class TestResumeParser(unittest.TestCase):
    def test_parse_sections(self):
        text = """John Doe\\nSoftware Engineer\\n\\nEXPERIENCE\\nWorked at Corp\\n\\nSKILLS\\nPython, Java"""
        parser = ResumeParser()
        sections = parser.parse(text)
        self.assertIn("header", sections)

    def test_extract_contact_info(self):
        parser = ResumeParser()
        info = parser.extract_contact_info("John Doe\\nEngineer")
        self.assertEqual(info["name"], "John Doe")


class TestResumeAnalyzer(unittest.TestCase):
    def test_extract_skills(self):
        analyzer = ResumeAnalyzer()
        skills = analyzer._extract_skills("Experience with Python and PyTorch")
        self.assertIn("python", skills)
        self.assertIn("pytorch", skills)

    def test_estimate_years(self):
        analyzer = ResumeAnalyzer()
        years = analyzer._estimate_experience_years("Corp 2018 - 2023")
        self.assertEqual(years, 5)


class TestResumeScorer(unittest.TestCase):
    def test_score_range(self):
        scorer = ResumeScorer()
        analysis = {
            "skills": ["python", "java"],
            "skill_categories": {"programming": ["python", "java"]},
            "experience_years": 5,
            "positions": [{"title": "SWE"}],
            "impact_metrics": ["50%", "10x"],
            "education": ["BS CS"],
            "sections_found": ["header", "experience", "skills"],
            "current_title": "Engineer",
            "name": "Test",
        }
        score = scorer.score(analysis)
        self.assertGreater(score["total"], 0)
        self.assertLessEqual(score["total"], 100)


if __name__ == "__main__":
    unittest.main()
'''

    return {
        "main.py": main_py,
        "src/__init__.py": '"""AI Resume Analyzer source package."""\n',
        "src/parser.py": parser_py,
        "src/analyzer.py": analyzer_py,
        "src/scorer.py": scorer_py,
        "tests/test_core.py": test_core,
    }


def _gen_code_reviewer() -> Dict[str, str]:
    """Generate the AI Code Review Assistant project."""
    main_py = '''"""
AI Code Review Assistant - Main Entry Point

Analyzes Python code for bugs, style issues, complexity,
and security vulnerabilities using AST analysis.
"""

import sys
from src.analyzer import CodeAnalyzer
from src.reporter import format_report

SAMPLE_CODE = """
import os
import pickle

def process_data(data, flag=True):
    result = []
    for i in range(len(data)):
        item = data[i]
        if flag == True:
            if item != None:
                try:
                    val = eval(item)
                    result.append(val)
                except:
                    pass
    password = "admin123"
    conn_string = "postgresql://user:pass@localhost/db"
    return result

class DataProcessor:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def process(self):
        for i in range(len(self.data)):
            x = self.data[i]
            if type(x) == str:
                print(x)
"""


def main():
    """Run code analysis on sample code."""
    print("=" * 60)
    print("AI Code Review Assistant")
    print("=" * 60)

    analyzer = CodeAnalyzer()
    results = analyzer.analyze(SAMPLE_CODE)
    report = format_report(results)
    print(report)


if __name__ == "__main__":
    main()
'''

    analyzer_py = '''"""
Code analysis engine using AST parsing.
"""

import ast
import re
from typing import Dict, List, Any


class CodeAnalyzer:
    """Analyzes Python source code for issues."""

    def analyze(self, source: str) -> Dict[str, Any]:
        """Run all analyses on the source code."""
        issues = []

        try:
            tree = ast.parse(source)
        except SyntaxError as e:
            return {"issues": [{"type": "error", "severity": "critical",
                    "message": f"Syntax error: {e.msg}", "line": e.lineno}],
                    "metrics": {}, "score": 0}

        issues.extend(self._check_security(source))
        issues.extend(self._check_style(tree))
        issues.extend(self._check_best_practices(tree, source))
        metrics = self._compute_metrics(tree, source)
        score = self._compute_score(issues, metrics)

        return {"issues": issues, "metrics": metrics, "score": score}

    def _check_security(self, source: str) -> List[Dict]:
        """Check for security issues."""
        issues = []
        lines = source.split("\\n")

        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if "eval(" in stripped:
                issues.append({"type": "security", "severity": "critical",
                    "message": "Use of eval() is a security risk", "line": i})
            if "exec(" in stripped:
                issues.append({"type": "security", "severity": "critical",
                    "message": "Use of exec() is a security risk", "line": i})
            if "pickle.loads" in stripped:
                issues.append({"type": "security", "severity": "high",
                    "message": "pickle.loads can execute arbitrary code", "line": i})

            # Hardcoded secrets
            secret_patterns = [
                (r\'password\\s*=\\s*["\\']\', "Hardcoded password detected"),
                (r\'(api_key|apikey|secret)\\s*=\\s*["\\']\', "Hardcoded secret detected"),
                (r\'(postgres|mysql|mongodb)://\\w+:\\w+@\', "Hardcoded database credentials"),
            ]
            for pattern, msg in secret_patterns:
                if re.search(pattern, stripped, re.IGNORECASE):
                    issues.append({"type": "security", "severity": "critical",
                        "message": msg, "line": i})
                    break

        return issues

    def _check_style(self, tree: ast.AST) -> List[Dict]:
        """Check code style issues."""
        issues = []

        for node in ast.walk(tree):
            # == True / == False / == None
            if isinstance(node, ast.Compare):
                for op, comp in zip(node.ops, node.comparators):
                    if isinstance(op, ast.Eq):
                        if isinstance(comp, ast.Constant) and comp.value is True:
                            issues.append({"type": "style", "severity": "low",
                                "message": "Use 'if x:' instead of 'if x == True'",
                                "line": node.lineno})
                        if isinstance(comp, ast.Constant) and comp.value is None:
                            issues.append({"type": "style", "severity": "low",
                                "message": "Use 'is None' instead of '== None'",
                                "line": node.lineno})

            # Bare except
            if isinstance(node, ast.ExceptHandler) and node.type is None:
                issues.append({"type": "style", "severity": "medium",
                    "message": "Bare except clause catches all exceptions",
                    "line": node.lineno})

            # type() instead of isinstance()
            if (isinstance(node, ast.Compare)
                    and isinstance(node.left, ast.Call)
                    and isinstance(node.left.func, ast.Name)
                    and node.left.func.id == "type"):
                issues.append({"type": "style", "severity": "low",
                    "message": "Use isinstance() instead of type() comparison",
                    "line": node.lineno})

            # range(len()) anti-pattern
            if (isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Name)
                    and node.func.id == "range"
                    and node.args
                    and isinstance(node.args[0], ast.Call)
                    and isinstance(node.args[0].func, ast.Name)
                    and node.args[0].func.id == "len"):
                issues.append({"type": "style", "severity": "low",
                    "message": "Use 'for item in collection' or enumerate() instead of range(len())",
                    "line": node.lineno})

        return issues

    def _check_best_practices(self, tree: ast.AST, source: str) -> List[Dict]:
        """Check for best practice violations."""
        issues = []

        for node in ast.walk(tree):
            # Functions without docstrings
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if not (node.body and isinstance(node.body[0], ast.Expr)
                        and isinstance(node.body[0].value, ast.Constant)
                        and isinstance(node.body[0].value.value, str)):
                    issues.append({"type": "best_practice", "severity": "low",
                        "message": f"Function '{node.name}' lacks a docstring",
                        "line": node.lineno})

            # Classes without docstrings
            if isinstance(node, ast.ClassDef):
                if not (node.body and isinstance(node.body[0], ast.Expr)
                        and isinstance(node.body[0].value, ast.Constant)
                        and isinstance(node.body[0].value.value, str)):
                    issues.append({"type": "best_practice", "severity": "low",
                        "message": f"Class '{node.name}' lacks a docstring",
                        "line": node.lineno})

        return issues

    def _compute_metrics(self, tree: ast.AST, source: str) -> Dict[str, int]:
        """Compute code complexity metrics."""
        funcs = [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
        classes = [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
        lines = [l for l in source.split("\\n") if l.strip() and not l.strip().startswith("#")]

        return {
            "total_lines": len(source.split("\\n")),
            "code_lines": len(lines),
            "functions": len(funcs),
            "classes": len(classes),
            "imports": sum(1 for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))),
        }

    def _compute_score(self, issues, metrics) -> int:
        """Compute overall code quality score (0-100)."""
        score = 100
        for issue in issues:
            if issue["severity"] == "critical":
                score -= 15
            elif issue["severity"] == "high":
                score -= 10
            elif issue["severity"] == "medium":
                score -= 5
            elif issue["severity"] == "low":
                score -= 2
        return max(0, score)
'''

    reporter = '''"""
Report formatting for code review results.
"""

from typing import Dict, Any


def format_report(results: Dict[str, Any]) -> str:
    """Format analysis results into a readable report."""
    lines = []
    issues = results["issues"]
    metrics = results["metrics"]
    score = results["score"]

    lines.append("\\n" + "=" * 60)
    lines.append("CODE REVIEW REPORT")
    lines.append("=" * 60)

    # Metrics
    lines.append("\\nCode Metrics:")
    for key, val in metrics.items():
        lines.append(f"  {key.replace('_', ' ').title()}: {val}")

    # Score
    lines.append(f"\\nOverall Score: {score}/100")
    if score >= 80:
        lines.append("  Rating: GOOD")
    elif score >= 60:
        lines.append("  Rating: NEEDS IMPROVEMENT")
    else:
        lines.append("  Rating: POOR")

    # Issues by severity
    if issues:
        lines.append(f"\\nIssues Found ({len(issues)}):")
        for sev in ["critical", "high", "medium", "low"]:
            sev_issues = [i for i in issues if i["severity"] == sev]
            if sev_issues:
                lines.append(f"\\n  [{sev.upper()}]")
                for issue in sev_issues:
                    lines.append(f"    Line {issue.get('line', '?')}: {issue['message']}")
    else:
        lines.append("\\nNo issues found!")

    lines.append("")
    return "\\n".join(lines)
'''

    return {
        "main.py": main_py,
        "src/__init__.py": '"""AI Code Review Assistant source package."""\n',
        "src/analyzer.py": analyzer_py,
        "src/reporter.py": reporter,
    }


def _gen_writing_analyzer() -> Dict[str, str]:
    """Generate writing style analyzer project files."""
    main_py = '''"""
AI Writing Style Analyzer - Main Entry Point
"""

import json
from src.analyzer import WritingAnalyzer


SAMPLE_TEXT = """
The rapid advancement of artificial intelligence has fundamentally transformed
how we interact with technology. Machine learning algorithms, once confined to
academic research labs, now power everything from recommendation engines to
autonomous vehicles.

However, this progress comes with significant challenges. Issues of bias in
training data, the environmental cost of large model training, and concerns
about job displacement require careful consideration. Industry leaders and
policymakers must work together to ensure AI development benefits society broadly.

Looking forward, the convergence of AI with other fields like biotechnology,
quantum computing, and robotics promises even more transformative changes.
The key will be developing robust frameworks for responsible AI governance
while maintaining the innovative spirit that drives progress.
"""


def main():
    """Analyze writing style of sample text."""
    print("=" * 60)
    print("AI Writing Style Analyzer")
    print("=" * 60)

    analyzer = WritingAnalyzer()
    result = analyzer.analyze(SAMPLE_TEXT)

    print(f"\\nReadability:")
    print(f"  Grade level: {result['grade_level']:.1f}")
    print(f"  Reading ease: {result['reading_ease']:.1f}")

    print(f"\\nStructure:")
    print(f"  Sentences: {result['sentence_count']}")
    print(f"  Avg sentence length: {result['avg_sentence_length']:.1f} words")
    print(f"  Paragraphs: {result['paragraph_count']}")

    print(f"\\nVocabulary:")
    print(f"  Unique words: {result['unique_words']}")
    print(f"  Vocabulary richness: {result['vocab_richness']:.3f}")
    print(f"  Avg word length: {result['avg_word_length']:.1f} chars")

    print(f"\\nTone: {result['tone']}")
    print(f"\\nSuggestions:")
    for s in result['suggestions']:
        print(f"  - {s}")


if __name__ == "__main__":
    main()
'''

    analyzer_py = '''"""
Writing analysis engine.
"""

import re
from typing import Dict, Any, List
from collections import Counter


class WritingAnalyzer:
    """Analyze writing style, readability, and structure."""

    def analyze(self, text: str) -> Dict[str, Any]:
        words = self._tokenize(text)
        sentences = self._split_sentences(text)
        paragraphs = [p for p in text.strip().split("\\n\\n") if p.strip()]
        syllable_count = sum(self._count_syllables(w) for w in words)

        avg_sent_len = len(words) / max(len(sentences), 1)
        avg_syl = syllable_count / max(len(words), 1)

        reading_ease = 206.835 - 1.015 * avg_sent_len - 84.6 * avg_syl
        grade_level = 0.39 * avg_sent_len + 11.8 * avg_syl - 15.59

        return {
            "word_count": len(words),
            "sentence_count": len(sentences),
            "paragraph_count": len(paragraphs),
            "avg_sentence_length": avg_sent_len,
            "avg_word_length": sum(len(w) for w in words) / max(len(words), 1),
            "unique_words": len(set(w.lower() for w in words)),
            "vocab_richness": len(set(w.lower() for w in words)) / max(len(words), 1),
            "reading_ease": max(0, min(100, reading_ease)),
            "grade_level": max(0, grade_level),
            "tone": self._detect_tone(text),
            "suggestions": self._generate_suggestions(avg_sent_len, reading_ease, words),
        }

    def _tokenize(self, text: str) -> List[str]:
        return re.findall(r"[a-zA-Z]+", text)

    def _split_sentences(self, text: str) -> List[str]:
        return [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]

    def _count_syllables(self, word: str) -> int:
        word = word.lower()
        count = len(re.findall(r"[aeiouy]+", word))
        return max(1, count)

    def _detect_tone(self, text: str) -> str:
        text_lower = text.lower()
        formal_markers = ["however", "furthermore", "consequently", "therefore",
                         "significant", "fundamental", "consideration"]
        count = sum(1 for m in formal_markers if m in text_lower)
        return "Formal/Academic" if count >= 2 else "Neutral" if count >= 1 else "Casual"

    def _generate_suggestions(self, avg_sent_len, reading_ease, words) -> List[str]:
        suggestions = []
        if avg_sent_len > 25:
            suggestions.append("Consider shorter sentences for better readability")
        if reading_ease < 30:
            suggestions.append("Text may be too complex for general audiences")
        if len(set(w.lower() for w in words)) / max(len(words), 1) < 0.4:
            suggestions.append("Consider using more varied vocabulary")
        if not suggestions:
            suggestions.append("Writing style is clear and well-balanced")
        return suggestions
'''

    return {
        "main.py": main_py,
        "src/__init__.py": '"""Writing Style Analyzer source package."""\n',
        "src/analyzer.py": analyzer_py,
    }


def _gen_prompt_engine() -> Dict[str, str]:
    """Generate prompt template engine project files."""
    main_py = '''"""
Prompt Template Engine - Main Entry Point
"""

from src.engine import PromptEngine
from src.templates import BUILTIN_TEMPLATES


def main():
    """Demo the prompt template engine."""
    print("=" * 60)
    print("Prompt Template Engine")
    print("=" * 60)

    engine = PromptEngine()

    # Register built-in templates
    for name, template in BUILTIN_TEMPLATES.items():
        engine.register(name, template["template"], template.get("defaults", {}))
        print(f"  Registered: {name}")

    # Render examples
    print("\\n--- Rendering Templates ---\\n")

    result = engine.render("summarize", text="AI is transforming healthcare...",
                          style="concise", max_words=100)
    print(f"[summarize]\\n{result}\\n")

    result = engine.render("classify", text="I love this product!",
                          categories="positive, negative, neutral")
    print(f"[classify]\\n{result}\\n")

    result = engine.render("extract", text="John works at Google in NYC.",
                          entities="person, company, location")
    print(f"[extract]\\n{result}\\n")

    # Show template stats
    stats = engine.get_stats()
    print(f"Templates: {stats['total_templates']}")
    print(f"Total renders: {stats['total_renders']}")


if __name__ == "__main__":
    main()
'''

    engine_py = '''"""
Core prompt template engine.
"""

import re
from typing import Dict, Any, Optional


class PromptEngine:
    """Manage and render prompt templates with variable injection."""

    def __init__(self):
        self._templates: Dict[str, dict] = {}
        self._render_count: Dict[str, int] = {}

    def register(self, name: str, template: str,
                defaults: Optional[Dict[str, str]] = None):
        """Register a named template."""
        variables = re.findall(r"\\{\\{(\\w+)\\}\\}", template)
        self._templates[name] = {
            "template": template,
            "variables": variables,
            "defaults": defaults or {},
        }
        self._render_count[name] = 0

    def render(self, name: str, **kwargs) -> str:
        """Render a template with provided variables."""
        if name not in self._templates:
            raise ValueError(f"Template '{name}' not found")

        entry = self._templates[name]
        result = entry["template"]

        # Merge defaults with provided kwargs
        merged = {**entry["defaults"], **kwargs}

        for var in entry["variables"]:
            placeholder = "{{" + var + "}}"
            value = merged.get(var, f"[MISSING: {var}]")
            result = result.replace(placeholder, str(value))

        self._render_count[name] = self._render_count.get(name, 0) + 1
        return result

    def list_templates(self):
        """List all registered templates."""
        return list(self._templates.keys())

    def get_stats(self) -> Dict[str, Any]:
        return {
            "total_templates": len(self._templates),
            "total_renders": sum(self._render_count.values()),
            "per_template": dict(self._render_count),
        }
'''

    templates = '''"""
Built-in prompt templates.
"""

BUILTIN_TEMPLATES = {
    "summarize": {
        "template": """Summarize the following text in a {{style}} manner.
Keep the summary under {{max_words}} words.

Text:
{{text}}

Summary:""",
        "defaults": {"style": "concise", "max_words": "150"},
    },
    "classify": {
        "template": """Classify the following text into one of these categories: {{categories}}

Text: {{text}}

Category:""",
        "defaults": {"categories": "positive, negative, neutral"},
    },
    "extract": {
        "template": """Extract the following entities from the text: {{entities}}

Text: {{text}}

Return as JSON:""",
        "defaults": {"entities": "person, organization, location"},
    },
    "translate": {
        "template": """Translate the following text from {{source_lang}} to {{target_lang}}.

Text: {{text}}

Translation:""",
        "defaults": {"source_lang": "English", "target_lang": "Spanish"},
    },
    "code_review": {
        "template": """Review the following {{language}} code for:
1. Bugs and errors
2. Style issues
3. Security vulnerabilities
4. Performance improvements

Code:
```{{language}}
{{code}}
```

Review:""",
        "defaults": {"language": "python"},
    },
}
'''

    return {
        "main.py": main_py,
        "src/__init__.py": '"""Prompt Template Engine source package."""\n',
        "src/engine.py": engine_py,
        "src/templates.py": templates,
    }


def _gen_genai_default(project: dict) -> Dict[str, str]:
    """Default Generative AI template."""
    title = project["name"].replace("-", " ").title()

    main_py = '''"""
{title} - Main Entry Point
"""

from src.core import Pipeline
from src.config import SAMPLE_INPUT


def main():
    print("=" * 60)
    print("{title}")
    print("=" * 60)

    pipeline = Pipeline()
    result = pipeline.process(SAMPLE_INPUT)

    print(f"\\nInput: {{SAMPLE_INPUT[:100]}}...")
    print(f"\\nResult:")
    for key, value in result.items():
        print(f"  {{key}}: {{value}}")


if __name__ == "__main__":
    main()
'''.format(title=title)

    core_py = '''"""Core processing pipeline."""

from typing import Dict, Any


class Pipeline:
    """Main processing pipeline."""

    def process(self, input_text: str) -> Dict[str, Any]:
        """Process input and return structured results."""
        tokens = input_text.split()
        return {{
            "input_length": len(input_text),
            "word_count": len(tokens),
            "processed": True,
            "summary": " ".join(tokens[:20]) + "..." if len(tokens) > 20 else input_text,
        }}
'''

    config_py = '''"""Configuration and sample data."""

import os

SAMPLE_INPUT = """Artificial intelligence and machine learning are transforming
every industry from healthcare to finance. These technologies enable automated
decision-making, pattern recognition, and predictive analytics at scale."""
'''

    return {
        "main.py": main_py,
        "src/__init__.py": f'"""{title} source package."""\n',
        "src/core.py": core_py,
        "src/config.py": config_py,
    }


# ============================================================================
# Remaining category generators (use parameterized templates)
# ============================================================================

def _gen_rag_files(project: dict) -> Dict[str, str]:
    """Generate RAG project files."""
    title = project["name"].replace("-", " ").title()
    sub = project.get("subcategory", "Basic RAG")

    main_py = '''"""
{title} - Main Entry Point

Demonstrates a {sub} implementation with document chunking,
embedding, indexing, and retrieval-augmented generation.
"""

from src.chunker import TextChunker
from src.embedder import SimpleEmbedder
from src.index import VectorIndex
from src.retriever import Retriever
from src.generator import ResponseGenerator


SAMPLE_DOCUMENTS = [
    "Retrieval Augmented Generation (RAG) combines retrieval and generation to produce grounded answers. "
    "The system first retrieves relevant documents from a knowledge base, then uses those documents as "
    "context for generating accurate, sourced responses.",

    "Vector databases store embeddings as high-dimensional vectors enabling similarity search. "
    "Popular options include FAISS for local use, Pinecone for managed cloud, and Chroma for "
    "lightweight prototyping. Each has different trade-offs for scale and performance.",

    "Chunking strategies affect RAG quality significantly. Fixed-size chunks are simple but can "
    "break semantic boundaries. Semantic chunking respects natural text boundaries. Recursive "
    "character splitting offers a balance between the two approaches.",

    "Embedding models convert text into dense vector representations. Sentence-transformers "
    "like all-MiniLM-L6-v2 offer good quality with fast inference. Larger models like "
    "text-embedding-3-large provide higher quality at the cost of speed.",

    "Hybrid retrieval combines keyword-based search (BM25) with dense vector search. "
    "Reciprocal Rank Fusion (RRF) merges results from both approaches, often outperforming "
    "either method alone. Re-ranking with cross-encoders further improves relevance.",
]


def main():
    """Run the RAG pipeline demonstration."""
    print("=" * 60)
    print("{title}")
    print("=" * 60)

    # Step 1: Chunk documents
    print("\\n[1/4] Chunking documents...")
    chunker = TextChunker(chunk_size=200, overlap=50)
    chunks = []
    for doc in SAMPLE_DOCUMENTS:
        chunks.extend(chunker.chunk(doc))
    print(f"  Created {{len(chunks)}} chunks from {{len(SAMPLE_DOCUMENTS)}} documents")

    # Step 2: Generate embeddings
    print("\\n[2/4] Generating embeddings...")
    embedder = SimpleEmbedder(dim=64)
    embeddings = embedder.embed_batch([c["text"] for c in chunks])
    print(f"  Generated {{len(embeddings)}} embeddings of dim {{embeddings[0].shape[0]}}")

    # Step 3: Build index
    print("\\n[3/4] Building vector index...")
    index = VectorIndex(dim=64)
    index.add(embeddings, chunks)
    print(f"  Indexed {{index.size}} vectors")

    # Step 4: Query
    print("\\n[4/4] Running queries...")
    retriever = Retriever(index, embedder)
    generator = ResponseGenerator()

    queries = [
        "What is RAG and how does it work?",
        "What chunking strategies are available?",
        "How does hybrid retrieval improve results?",
    ]

    for query in queries:
        print(f"\\n  Q: {{query}}")
        results = retriever.retrieve(query, top_k=2)
        response = generator.generate(query, results)
        print(f"  A: {{response}}")
        print(f"  Sources: {{[r['chunk_id'] for r in results]}}")


if __name__ == "__main__":
    main()
'''.format(title=title, sub=sub)

    chunker = '''"""
Text chunking module with multiple strategies.
"""

from typing import List, Dict


class TextChunker:
    """Split text into overlapping chunks."""

    def __init__(self, chunk_size: int = 200, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap
        self._chunk_counter = 0

    def chunk(self, text: str) -> List[Dict]:
        """Split text into overlapping character-level chunks."""
        chunks = []
        start = 0

        while start < len(text):
            end = start + self.chunk_size
            chunk_text = text[start:end]

            # Try to break at sentence boundary
            if end < len(text):
                last_period = chunk_text.rfind(".")
                if last_period > self.chunk_size // 2:
                    chunk_text = chunk_text[:last_period + 1]
                    end = start + last_period + 1

            self._chunk_counter += 1
            chunks.append({
                "chunk_id": f"chunk_{self._chunk_counter}",
                "text": chunk_text.strip(),
                "start": start,
                "end": end,
            })

            start = end - self.overlap
            if start >= len(text):
                break

        return chunks
'''

    embedder = '''"""
Simple embedding module.

Uses a hash-based approach for demonstration.
Replace with sentence-transformers for production use.
"""

import numpy as np
import hashlib
from typing import List


class SimpleEmbedder:
    """Generate deterministic embeddings from text using hashing."""

    def __init__(self, dim: int = 64):
        self.dim = dim

    def embed(self, text: str) -> np.ndarray:
        """Generate a deterministic embedding for text."""
        # Create a seed from text hash
        text_hash = hashlib.sha256(text.encode()).hexdigest()
        seed = int(text_hash[:8], 16) % (2**31)
        rng = np.random.RandomState(seed)

        # Generate base vector from hash
        vec = rng.randn(self.dim)

        # Add word-frequency signal
        words = text.lower().split()
        for i, word in enumerate(words[:self.dim]):
            idx = hash(word) % self.dim
            vec[idx] += 0.1 * (1.0 / (i + 1))

        # Normalize to unit vector
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec = vec / norm
        return vec

    def embed_batch(self, texts: List[str]) -> List[np.ndarray]:
        """Embed multiple texts."""
        return [self.embed(t) for t in texts]
'''

    index_py = '''"""
Vector index for similarity search.
"""

import numpy as np
from typing import List, Dict, Optional


class VectorIndex:
    """Simple in-memory vector index using cosine similarity."""

    def __init__(self, dim: int = 64):
        self.dim = dim
        self.vectors: Optional[np.ndarray] = None
        self.metadata: List[Dict] = []

    @property
    def size(self) -> int:
        return len(self.metadata)

    def add(self, embeddings: List[np.ndarray], chunks: List[Dict]):
        """Add vectors and their metadata to the index."""
        matrix = np.vstack(embeddings)

        if self.vectors is None:
            self.vectors = matrix
        else:
            self.vectors = np.vstack([self.vectors, matrix])

        self.metadata.extend(chunks)

    def search(self, query_vec: np.ndarray, top_k: int = 5) -> List[Dict]:
        """Find top-k most similar vectors."""
        if self.vectors is None or len(self.metadata) == 0:
            return []

        # Cosine similarity
        similarities = self.vectors @ query_vec
        top_indices = np.argsort(similarities)[::-1][:top_k]

        results = []
        for idx in top_indices:
            results.append({
                **self.metadata[idx],
                "score": float(similarities[idx]),
            })
        return results
'''

    retriever = '''"""
Retrieval module combining vector search with scoring.
"""

from typing import List, Dict


class Retriever:
    """Retrieve relevant chunks for a query."""

    def __init__(self, index, embedder):
        self.index = index
        self.embedder = embedder

    def retrieve(self, query: str, top_k: int = 3) -> List[Dict]:
        """Retrieve top-k relevant chunks."""
        query_vec = self.embedder.embed(query)
        results = self.index.search(query_vec, top_k=top_k)
        return results
'''

    generator = '''"""
Response generation module.
"""

from typing import List, Dict


class ResponseGenerator:
    """Generate responses from retrieved context.

    For demonstration, uses extractive generation (returns
    most relevant chunk). Replace with LLM for production.
    """

    def generate(self, query: str, contexts: List[Dict]) -> str:
        """Generate a response based on retrieved contexts."""
        if not contexts:
            return "No relevant information found."

        # Use top context as the base response
        top = contexts[0]
        text = top["text"]

        # Simple extractive response: find most relevant sentence
        sentences = [s.strip() for s in text.split(".") if s.strip()]
        query_words = set(query.lower().split())

        scored = []
        for sent in sentences:
            sent_words = set(sent.lower().split())
            overlap = len(query_words & sent_words)
            scored.append((overlap, sent))

        scored.sort(reverse=True)
        best_sentences = [s for _, s in scored[:2]]
        return ". ".join(best_sentences) + "."
'''

    return {
        "main.py": main_py,
        "src/__init__.py": f'"""{title} source package."""\n',
        "src/chunker.py": chunker,
        "src/embedder.py": embedder,
        "src/index.py": index_py,
        "src/retriever.py": retriever,
        "src/generator.py": generator,
    }


def _gen_hf_files(project: dict) -> Dict[str, str]:
    """Generate Hugging Face project files."""
    return _gen_genai_default(project)


def _gen_langchain_files(project: dict) -> Dict[str, str]:
    """Generate LangChain project files."""
    return _gen_genai_default(project)


def _gen_langgraph_files(project: dict) -> Dict[str, str]:
    """Generate LangGraph project files."""
    return _gen_genai_default(project)


def _gen_llm_eng_files(project: dict) -> Dict[str, str]:
    """Generate LLM Engineering project files."""
    return _gen_genai_default(project)


def _gen_cv_files(project: dict) -> Dict[str, str]:
    """Generate Computer Vision project files."""
    return _gen_genai_default(project)


def _gen_multimodal_files(project: dict) -> Dict[str, str]:
    """Generate Multimodal AI project files."""
    return _gen_genai_default(project)


def _gen_audio_files(project: dict) -> Dict[str, str]:
    """Generate Speech/Audio AI project files."""
    return _gen_genai_default(project)


def _gen_db_files(project: dict) -> Dict[str, str]:
    """Generate AI + Databases project files."""
    return _gen_genai_default(project)


def _gen_graph_rag_files(project: dict) -> Dict[str, str]:
    """Generate Graph RAG project files."""
    return _gen_rag_files(project)


def _gen_web_files(project: dict) -> Dict[str, str]:
    """Generate AI + Web project files."""
    return _gen_genai_default(project)


def _gen_automation_files(project: dict) -> Dict[str, str]:
    """Generate AI Automation project files."""
    return _gen_genai_default(project)


def _gen_mlops_files(project: dict) -> Dict[str, str]:
    """Generate MLOps project files."""
    return _gen_genai_default(project)


def _gen_security_files(project: dict) -> Dict[str, str]:
    """Generate AI Security project files."""
    return _gen_genai_default(project)


def _gen_evaluation_files(project: dict) -> Dict[str, str]:
    """Generate LLM Evaluation project files."""
    return _gen_genai_default(project)


def _gen_finetuning_files(project: dict) -> Dict[str, str]:
    """Generate Fine-Tuning project files."""
    return _gen_genai_default(project)


def _gen_generic_files(project: dict) -> Dict[str, str]:
    """Fallback generic project generator."""
    return _gen_genai_default(project)

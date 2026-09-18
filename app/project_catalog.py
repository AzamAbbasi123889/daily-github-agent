"""
Project catalog for Daily GitHub Agent.

Contains 50+ AI/ML project templates across 19 categories.
Each entry defines metadata and technology stack.
The content_generators module handles actual file generation.
"""


PROJECT_CATALOG = [
    # =========================================================================
    # MACHINE LEARNING (1-6)
    # =========================================================================
    {
        "name": "advanced-fraud-detection-system",
        "description": "Real-time fraud detection pipeline using ensemble methods with XGBoost, isolation forests, and SHAP-based model explainability for transaction analysis.",
        "category": "Machine Learning",
        "subcategory": "Anomaly Detection",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "XGBoost", "Scikit-learn", "SHAP", "Pandas", "NumPy"],
    },
    {
        "name": "customer-churn-predictor",
        "description": "End-to-end customer churn prediction system with feature engineering, model comparison, hyperparameter tuning via Optuna, and SHAP explanations.",
        "category": "Machine Learning",
        "subcategory": "Classification",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "Scikit-learn", "XGBoost", "LightGBM", "Optuna", "SHAP", "Pandas"],
    },
    {
        "name": "time-series-forecasting-engine",
        "description": "Multi-model time series forecasting engine comparing ARIMA, Prophet-style decomposition, and gradient boosting approaches with walk-forward validation.",
        "category": "Machine Learning",
        "subcategory": "Time Series",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Scikit-learn", "XGBoost", "Pandas", "NumPy", "Statsmodels"],
    },
    {
        "name": "smart-feature-engineering-toolkit",
        "description": "Automated feature engineering toolkit that generates polynomial, interaction, time-based, and statistical features with importance ranking.",
        "category": "Machine Learning",
        "subcategory": "Feature Engineering",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "Scikit-learn", "Pandas", "NumPy", "SHAP"],
    },
    {
        "name": "ml-model-comparison-framework",
        "description": "Framework for systematic comparison of ML models with cross-validation, statistical significance testing, and automated performance reports.",
        "category": "Machine Learning",
        "subcategory": "Model Evaluation",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "Scikit-learn", "XGBoost", "LightGBM", "Pandas", "NumPy"],
    },
    {
        "name": "recommendation-engine-collaborative",
        "description": "Hybrid recommendation engine combining collaborative filtering, content-based filtering, and matrix factorization for item recommendations.",
        "category": "Machine Learning",
        "subcategory": "Recommendation Systems",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Scikit-learn", "Pandas", "NumPy", "SciPy"],
    },

    # =========================================================================
    # DEEP LEARNING (7-10)
    # =========================================================================
    {
        "name": "neural-style-transfer-engine",
        "description": "Neural style transfer system using VGG19 feature extraction with content and style loss optimization for artistic image transformation.",
        "category": "Deep Learning",
        "subcategory": "Transfer Learning",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "PyTorch", "TorchVision", "PIL", "NumPy"],
    },
    {
        "name": "lstm-text-generator",
        "description": "Character-level and word-level LSTM text generation model with temperature-controlled sampling and beam search decoding.",
        "category": "Deep Learning",
        "subcategory": "RNN/LSTM",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "PyTorch", "NumPy"],
    },
    {
        "name": "autoencoder-anomaly-detector",
        "description": "Variational autoencoder for unsupervised anomaly detection in tabular data with reconstruction error thresholding and latent space visualization.",
        "category": "Deep Learning",
        "subcategory": "Autoencoders",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "PyTorch", "Scikit-learn", "Pandas", "NumPy"],
    },
    {
        "name": "vision-transformer-classifier",
        "description": "Vision Transformer (ViT) implementation for image classification with patch embedding, multi-head attention, and transfer learning from pretrained weights.",
        "category": "Deep Learning",
        "subcategory": "Vision Transformers",
        "difficulty": "Expert",
        "tech_stack": ["Python", "PyTorch", "TorchVision", "PIL", "NumPy"],
    },

    # =========================================================================
    # NLP (11-15)
    # =========================================================================
    {
        "name": "semantic-document-search",
        "description": "Semantic search engine using sentence transformers for document embedding, FAISS indexing, and BM25 hybrid retrieval with re-ranking.",
        "category": "NLP",
        "subcategory": "Semantic Search",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "Sentence-Transformers", "FAISS", "NumPy", "Pandas"],
    },
    {
        "name": "named-entity-extraction-api",
        "description": "REST API for named entity recognition combining spaCy's pipeline with custom entity rules and confidence scoring.",
        "category": "NLP",
        "subcategory": "Named Entity Recognition",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "spaCy", "FastAPI", "Pydantic"],
    },
    {
        "name": "extractive-text-summarizer",
        "description": "Extractive text summarization using TextRank algorithm with sentence embeddings, graph-based ranking, and configurable compression ratios.",
        "category": "NLP",
        "subcategory": "Text Summarization",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "Sentence-Transformers", "NetworkX", "NumPy", "NLTK"],
    },
    {
        "name": "multilingual-sentiment-analyzer",
        "description": "Multi-language sentiment analysis pipeline supporting 50+ languages using multilingual transformer models with aspect-based extraction.",
        "category": "NLP",
        "subcategory": "Text Classification",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Transformers", "Torch", "Pandas"],
    },
    {
        "name": "topic-modeling-pipeline",
        "description": "Advanced topic modeling system using BERTopic with UMAP dimensionality reduction, HDBSCAN clustering, and interactive topic visualization.",
        "category": "NLP",
        "subcategory": "Topic Modeling",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "BERTopic", "Sentence-Transformers", "UMAP", "HDBSCAN", "Pandas"],
    },

    # =========================================================================
    # HUGGING FACE (16-20)
    # =========================================================================
    {
        "name": "hf-lora-fine-tuning-pipeline",
        "description": "Parameter-efficient fine-tuning pipeline using LoRA/QLoRA with Hugging Face PEFT, TRL, and automated evaluation on custom datasets.",
        "category": "Hugging Face",
        "subcategory": "Fine-Tuning",
        "difficulty": "Expert",
        "tech_stack": ["Python", "Transformers", "PEFT", "TRL", "Datasets", "Accelerate", "BitsAndBytes"],
    },
    {
        "name": "hf-embedding-benchmark",
        "description": "Systematic benchmark of sentence embedding models from Hugging Face comparing retrieval accuracy, semantic similarity, and inference speed.",
        "category": "Hugging Face",
        "subcategory": "Embeddings",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "Sentence-Transformers", "Datasets", "NumPy", "Pandas"],
    },
    {
        "name": "hf-text-classification-trainer",
        "description": "End-to-end text classification training pipeline with Hugging Face Trainer, dataset preprocessing, class balancing, and evaluation metrics.",
        "category": "Hugging Face",
        "subcategory": "Text Classification",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "Transformers", "Datasets", "Scikit-learn", "Accelerate"],
    },
    {
        "name": "hf-dataset-processor",
        "description": "Scalable dataset processing pipeline for Hugging Face Datasets with cleaning, deduplication, quality filtering, and format conversion.",
        "category": "Hugging Face",
        "subcategory": "Datasets",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "Datasets", "Pandas", "NumPy"],
    },
    {
        "name": "hf-model-evaluator",
        "description": "Comprehensive model evaluation framework for Hugging Face models with perplexity, BLEU, ROUGE, and custom metric computation.",
        "category": "Hugging Face",
        "subcategory": "Model Evaluation",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Transformers", "Datasets", "Evaluate", "NumPy"],
    },

    # =========================================================================
    # GENERATIVE AI (21-26)
    # =========================================================================
    {
        "name": "ai-resume-analyzer",
        "description": "Intelligent resume analysis system that extracts skills, experience, education using NLP pattern matching and scoring algorithms.",
        "category": "Generative AI",
        "subcategory": "Document Intelligence",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "spaCy", "Pandas"],
    },
    {
        "name": "structured-output-generator",
        "description": "LLM-powered structured data extraction with JSON schema validation, retry logic, and output parsing for reliable structured generation.",
        "category": "Generative AI",
        "subcategory": "Structured Output",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "OpenAI", "Pydantic", "JSONSchema"],
    },
    {
        "name": "ai-code-review-assistant",
        "description": "Automated code review assistant that analyzes Python code for bugs, style issues, security vulnerabilities, and provides improvement suggestions.",
        "category": "Generative AI",
        "subcategory": "Code Analysis",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "AST", "Radon", "Pylint"],
    },
    {
        "name": "multi-model-llm-router",
        "description": "Intelligent LLM request router that selects optimal model based on query complexity, cost, latency constraints, and fallback strategies.",
        "category": "Generative AI",
        "subcategory": "Model Routing",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "OpenAI", "FastAPI", "Pydantic"],
    },
    {
        "name": "ai-writing-style-analyzer",
        "description": "Writing style analysis tool that profiles text for readability, tone, complexity, vocabulary richness, and provides style recommendations.",
        "category": "Generative AI",
        "subcategory": "Text Analysis",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "NLTK", "TextBlob", "Pandas"],
    },
    {
        "name": "prompt-template-engine",
        "description": "Dynamic prompt template engine with variable injection, few-shot example management, chain-of-thought scaffolding, and A/B testing support.",
        "category": "Generative AI",
        "subcategory": "Prompt Engineering",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "Jinja2", "Pydantic", "YAML"],
    },

    # =========================================================================
    # RAG (27-33)
    # =========================================================================
    {
        "name": "hybrid-rag-search-engine",
        "description": "Hybrid RAG system combining BM25 keyword search with dense vector retrieval, reciprocal rank fusion, and cross-encoder re-ranking.",
        "category": "RAG",
        "subcategory": "Hybrid RAG",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "FAISS", "Sentence-Transformers", "Rank-BM25", "NumPy"],
    },
    {
        "name": "corrective-rag-system",
        "description": "Self-correcting RAG pipeline that evaluates retrieval quality, rewrites queries on low confidence, and validates answers against source documents.",
        "category": "RAG",
        "subcategory": "Corrective RAG",
        "difficulty": "Expert",
        "tech_stack": ["Python", "FAISS", "Sentence-Transformers", "OpenAI", "Pydantic"],
    },
    {
        "name": "multi-document-rag-analyst",
        "description": "Multi-document RAG system with document-level metadata filtering, cross-document citation, and source attribution tracking.",
        "category": "RAG",
        "subcategory": "Multi-Document RAG",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "ChromaDB", "Sentence-Transformers", "OpenAI", "Pandas"],
    },
    {
        "name": "conversational-rag-chatbot",
        "description": "Stateful conversational RAG with chat history compression, context window management, follow-up question handling, and citation display.",
        "category": "RAG",
        "subcategory": "Conversational RAG",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "FAISS", "Sentence-Transformers", "OpenAI"],
    },
    {
        "name": "citation-aware-rag-engine",
        "description": "RAG engine that generates answers with inline citations, source confidence scores, and verifiable reference links to original documents.",
        "category": "RAG",
        "subcategory": "Citation RAG",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Qdrant", "Sentence-Transformers", "OpenAI", "Pydantic"],
    },
    {
        "name": "code-rag-assistant",
        "description": "Code-specialized RAG system for searching and understanding codebases with AST-aware chunking, code embedding, and contextual code retrieval.",
        "category": "RAG",
        "subcategory": "Code RAG",
        "difficulty": "Expert",
        "tech_stack": ["Python", "FAISS", "Sentence-Transformers", "AST", "Tree-sitter"],
    },
    {
        "name": "multimodal-rag-pipeline",
        "description": "RAG pipeline handling text, images, and tables from documents using multimodal embeddings with layout-aware document parsing.",
        "category": "RAG",
        "subcategory": "Multimodal RAG",
        "difficulty": "Expert",
        "tech_stack": ["Python", "FAISS", "Sentence-Transformers", "PIL", "PyMuPDF", "Pandas"],
    },

    # =========================================================================
    # LANGCHAIN / LANGGRAPH (34-38)
    # =========================================================================
    {
        "name": "langchain-document-qa-pipeline",
        "description": "Document question-answering pipeline using LangChain with recursive text splitting, multi-retriever fusion, and answer grounding.",
        "category": "LangChain",
        "subcategory": "Document QA",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "LangChain", "FAISS", "OpenAI"],
    },
    {
        "name": "langgraph-research-agent",
        "description": "Multi-step research agent built with LangGraph featuring search, analysis, summarization nodes with human-in-the-loop checkpoints.",
        "category": "LangGraph",
        "subcategory": "Research Agent",
        "difficulty": "Expert",
        "tech_stack": ["Python", "LangGraph", "LangChain", "OpenAI"],
    },
    {
        "name": "langchain-sql-analytics-agent",
        "description": "Natural language to SQL agent using LangChain with schema introspection, query validation, result visualization, and safety guardrails.",
        "category": "LangChain",
        "subcategory": "SQL Agent",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "LangChain", "SQLAlchemy", "OpenAI", "Pandas"],
    },
    {
        "name": "langgraph-code-analysis-agent",
        "description": "Stateful code analysis agent using LangGraph with AST parsing, complexity analysis, dependency graphing, and refactoring suggestions.",
        "category": "LangGraph",
        "subcategory": "Code Agent",
        "difficulty": "Expert",
        "tech_stack": ["Python", "LangGraph", "LangChain", "AST", "Radon"],
    },
    {
        "name": "langgraph-planning-agent",
        "description": "Goal-oriented planning agent with LangGraph featuring task decomposition, dependency resolution, execution, and reflection loops.",
        "category": "LangGraph",
        "subcategory": "Planning Agent",
        "difficulty": "Expert",
        "tech_stack": ["Python", "LangGraph", "LangChain", "OpenAI", "Pydantic"],
    },

    # =========================================================================
    # LLM ENGINEERING (39-43)
    # =========================================================================
    {
        "name": "llm-prompt-optimizer",
        "description": "Systematic prompt optimization framework with A/B testing, performance tracking, version control, and automated prompt evaluation.",
        "category": "LLM Engineering",
        "subcategory": "Prompt Engineering",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "OpenAI", "Pydantic", "SQLite", "Pandas"],
    },
    {
        "name": "llm-output-guardrails",
        "description": "Output validation and guardrail system for LLMs with toxicity detection, PII filtering, JSON schema enforcement, and hallucination scoring.",
        "category": "LLM Engineering",
        "subcategory": "Guardrails",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Pydantic", "Regex", "Transformers"],
    },
    {
        "name": "llm-conversation-memory-manager",
        "description": "Conversation memory system with sliding window, summarization-based compression, entity tracking, and long-term memory retrieval.",
        "category": "LLM Engineering",
        "subcategory": "Memory",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "OpenAI", "FAISS", "Sentence-Transformers", "Pydantic"],
    },
    {
        "name": "llm-evaluation-harness",
        "description": "Comprehensive LLM evaluation framework measuring accuracy, relevance, faithfulness, latency, token usage, and cost across multiple models.",
        "category": "LLM Engineering",
        "subcategory": "Evaluation",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "OpenAI", "Pandas", "NumPy", "Pydantic"],
    },
    {
        "name": "llm-rate-limiter-cache",
        "description": "Production-grade LLM request manager with token-aware rate limiting, semantic caching, request deduplication, and cost tracking.",
        "category": "LLM Engineering",
        "subcategory": "Infrastructure",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Redis", "OpenAI", "Pydantic", "AsyncIO"],
    },

    # =========================================================================
    # COMPUTER VISION (44-47)
    # =========================================================================
    {
        "name": "document-ocr-extraction-pipeline",
        "description": "Document OCR pipeline with image preprocessing, text region detection, multi-engine OCR, and structured data extraction from forms and invoices.",
        "category": "Computer Vision",
        "subcategory": "OCR",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "OpenCV", "Tesseract", "PIL", "Pandas", "NumPy"],
    },
    {
        "name": "image-similarity-search-engine",
        "description": "Visual similarity search using deep feature extraction, FAISS indexing, and efficient nearest neighbor retrieval for image collections.",
        "category": "Computer Vision",
        "subcategory": "Visual Search",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "PyTorch", "TorchVision", "FAISS", "PIL", "NumPy"],
    },
    {
        "name": "real-time-object-detection-api",
        "description": "REST API for object detection using YOLO with image preprocessing, confidence filtering, NMS, and bounding box visualization.",
        "category": "Computer Vision",
        "subcategory": "Object Detection",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Ultralytics", "FastAPI", "OpenCV", "PIL"],
    },
    {
        "name": "image-classification-transfer-learning",
        "description": "Transfer learning image classifier using pretrained ResNet/EfficientNet with custom dataset support, augmentation, and Grad-CAM explanations.",
        "category": "Computer Vision",
        "subcategory": "Image Classification",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "PyTorch", "TorchVision", "PIL", "NumPy"],
    },

    # =========================================================================
    # MULTIMODAL AI (48-49)
    # =========================================================================
    {
        "name": "multimodal-document-analyzer",
        "description": "Document analysis combining OCR, layout detection, table extraction, and text understanding for automated document intelligence.",
        "category": "Multimodal AI",
        "subcategory": "Document Intelligence",
        "difficulty": "Expert",
        "tech_stack": ["Python", "PyTorch", "Transformers", "PIL", "OpenCV", "Pandas"],
    },
    {
        "name": "visual-question-answering-system",
        "description": "VQA system that answers natural language questions about images using vision-language models with attention visualization.",
        "category": "Multimodal AI",
        "subcategory": "VQA",
        "difficulty": "Expert",
        "tech_stack": ["Python", "Transformers", "PIL", "Torch"],
    },

    # =========================================================================
    # SPEECH / AUDIO AI (50-51)
    # =========================================================================
    {
        "name": "meeting-transcription-summarizer",
        "description": "Meeting intelligence pipeline using Whisper for transcription with speaker-aware segmentation and extractive/abstractive summarization.",
        "category": "Speech/Audio AI",
        "subcategory": "Transcription",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Whisper", "Transformers", "Torch", "Pandas"],
    },
    {
        "name": "audio-event-classification-system",
        "description": "Audio event classifier using mel-spectrogram features with CNN/transformer models for environmental sound recognition.",
        "category": "Speech/Audio AI",
        "subcategory": "Audio Classification",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Torch", "Torchaudio", "Transformers", "NumPy"],
    },

    # =========================================================================
    # AI + DATABASES (52-54)
    # =========================================================================
    {
        "name": "natural-language-sql-query-engine",
        "description": "Natural language to SQL translation engine with schema understanding, query validation, execution, and result formatting.",
        "category": "AI + Databases",
        "subcategory": "NL2SQL",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "SQLAlchemy", "SQLite", "OpenAI", "Pandas"],
    },
    {
        "name": "knowledge-graph-builder",
        "description": "Automated knowledge graph construction from text using entity extraction, relation detection, and graph storage with Neo4j/NetworkX.",
        "category": "AI + Databases",
        "subcategory": "Knowledge Graphs",
        "difficulty": "Expert",
        "tech_stack": ["Python", "spaCy", "NetworkX", "Pandas"],
    },
    {
        "name": "vector-search-microservice",
        "description": "Production-ready vector similarity search microservice with FAISS backend, REST API, batch indexing, and metadata filtering.",
        "category": "AI + Databases",
        "subcategory": "Vector Search",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "FAISS", "FastAPI", "NumPy", "Pydantic"],
    },

    # =========================================================================
    # GRAPH RAG (55)
    # =========================================================================
    {
        "name": "graph-rag-knowledge-system",
        "description": "Graph-based RAG system combining knowledge graph traversal with vector retrieval for entity-relationship aware question answering.",
        "category": "Graph RAG",
        "subcategory": "Hybrid Graph-Vector",
        "difficulty": "Expert",
        "tech_stack": ["Python", "NetworkX", "FAISS", "Sentence-Transformers", "spaCy", "Pandas"],
    },

    # =========================================================================
    # AI + WEB (56-57)
    # =========================================================================
    {
        "name": "ai-research-dashboard",
        "description": "Interactive research dashboard with document upload, semantic search, summarization, and knowledge graph visualization using Streamlit.",
        "category": "AI + Web",
        "subcategory": "Dashboard",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Streamlit", "Sentence-Transformers", "FAISS", "Pandas", "Plotly"],
    },
    {
        "name": "model-comparison-dashboard",
        "description": "ML model comparison dashboard for tracking experiments, comparing metrics, and visualizing performance across different models and datasets.",
        "category": "AI + Web",
        "subcategory": "Dashboard",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "Streamlit", "Scikit-learn", "Pandas", "Plotly"],
    },

    # =========================================================================
    # AI AUTOMATION (58)
    # =========================================================================
    {
        "name": "ai-data-pipeline-orchestrator",
        "description": "Data pipeline orchestration system with DAG-based task scheduling, data validation, transformation, and ML model trigger integration.",
        "category": "AI Automation",
        "subcategory": "Pipeline",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Pandas", "SQLite", "Pydantic", "AsyncIO"],
    },

    # =========================================================================
    # MLOPS (59-60)
    # =========================================================================
    {
        "name": "ml-experiment-tracker",
        "description": "Lightweight experiment tracking system with metric logging, parameter versioning, artifact management, and comparison dashboards.",
        "category": "MLOps",
        "subcategory": "Experiment Tracking",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "SQLite", "FastAPI", "Pandas", "Pydantic"],
    },
    {
        "name": "model-serving-api",
        "description": "Production model serving API with health checks, request validation, batch prediction, A/B testing, and monitoring metrics.",
        "category": "MLOps",
        "subcategory": "Model Serving",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "FastAPI", "Scikit-learn", "Pydantic", "Prometheus-Client"],
    },

    # =========================================================================
    # AI SECURITY (61-63)
    # =========================================================================
    {
        "name": "prompt-injection-detector",
        "description": "Prompt injection detection system using pattern matching, embedding-based similarity, and classifier ensemble for LLM input security.",
        "category": "AI Security",
        "subcategory": "Prompt Injection",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Scikit-learn", "Sentence-Transformers", "Regex", "Pydantic"],
    },
    {
        "name": "pii-detection-anonymizer",
        "description": "PII detection and anonymization pipeline using regex patterns, NER models, and context-aware masking for text data privacy compliance.",
        "category": "AI Security",
        "subcategory": "PII Detection",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "spaCy", "Regex", "Pandas", "Pydantic"],
    },
    {
        "name": "llm-red-team-evaluator",
        "description": "LLM safety evaluation framework with adversarial prompt generation, jailbreak testing, output toxicity scoring, and vulnerability reporting.",
        "category": "AI Security",
        "subcategory": "Red Teaming",
        "difficulty": "Expert",
        "tech_stack": ["Python", "OpenAI", "Transformers", "Pandas", "Pydantic"],
    },

    # =========================================================================
    # LLM EVALUATION (64-65)
    # =========================================================================
    {
        "name": "rag-evaluation-framework",
        "description": "RAG evaluation framework measuring retrieval precision, answer faithfulness, groundedness, relevance, and hallucination rate.",
        "category": "LLM Evaluation",
        "subcategory": "RAG Evaluation",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Sentence-Transformers", "OpenAI", "Pandas", "NumPy", "Pydantic"],
    },
    {
        "name": "llm-benchmark-suite",
        "description": "Multi-dimensional LLM benchmark suite testing reasoning, coding, instruction following, factuality, and safety across models.",
        "category": "LLM Evaluation",
        "subcategory": "Benchmarking",
        "difficulty": "Expert",
        "tech_stack": ["Python", "OpenAI", "Transformers", "Pandas", "NumPy", "Pydantic"],
    },

    # =========================================================================
    # FINE-TUNING (66-67)
    # =========================================================================
    {
        "name": "lora-text-classifier-trainer",
        "description": "LoRA-based text classification fine-tuning pipeline with dataset preparation, training loop, evaluation, and model export.",
        "category": "Fine-Tuning",
        "subcategory": "LoRA",
        "difficulty": "Expert",
        "tech_stack": ["Python", "Transformers", "PEFT", "Datasets", "Torch", "Accelerate"],
    },
    {
        "name": "instruction-tuning-data-pipeline",
        "description": "Instruction tuning dataset creation pipeline with data formatting, quality filtering, deduplication, and SFT-ready output generation.",
        "category": "Fine-Tuning",
        "subcategory": "SFT",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Datasets", "Pandas", "NLTK", "Pydantic"],
    },
]


def get_catalog():
    """Return the full project catalog."""
    return PROJECT_CATALOG


def get_project_by_name(name: str):
    """Look up a project by its name."""
    for project in PROJECT_CATALOG:
        if project["name"] == name:
            return project
    return None


def get_projects_by_category(category: str):
    """Return all projects in a given category."""
    return [p for p in PROJECT_CATALOG if p["category"] == category]


def get_categories():
    """Return a sorted list of unique categories."""
    return sorted(set(p["category"] for p in PROJECT_CATALOG))


LEARNING_TOPICS = {
    "python": "Python basics: variables, loops, functions, lists and dictionaries",
    "java": "Java basics: classes, objects and collections",
    "c++": "C++ basics: syntax, pointers and OOP",
    "c#": "C# basics: syntax, classes and .NET fundamentals",
    "javascript": "JavaScript basics: variables, functions and the DOM",
    "sql": "SQL: SELECT, WHERE, GROUP BY and JOINs",
    "mongodb": "MongoDB: documents, collections and basic queries",
    "excel": "Excel: formulas, pivot tables and charts",
    "power bi": "Power BI: loading data and building a dashboard",
    "tableau": "Tableau: connecting data and building charts",
    "git": "Git and GitHub: commit, push, branches",
    "streamlit": "Streamlit: build a simple web app in Python",
    "pandas": "Pandas: DataFrames, cleaning data, groupby",
    "numpy": "NumPy: arrays and fast maths",
    "statistics": "Statistics: mean, variance, probability, hypothesis tests",
    "matplotlib": "Matplotlib: line, bar and scatter plots",
    "plotly": "Plotly: interactive charts",
    "machine learning": "Machine learning basics: regression, classification, train/test split",
    "deep learning": "Deep learning: neural networks, layers, backpropagation",
    "scikit-learn": "scikit-learn: build, train and evaluate models",
    "tensorflow": "TensorFlow: build and train a simple neural network",
    "pytorch": "PyTorch: tensors and training loops",
    "keras": "Keras: build neural networks quickly",
    "cnn": "CNNs: convolution layers for image tasks",
    "nlp": "NLP basics: tokenization, TF-IDF, text classification",
    "transformers": "Transformers: attention and how BERT/GPT work",
    "hugging face": "Hugging Face: use pretrained models with the transformers library",
    "spacy": "spaCy: tokens, named entities and pipelines",
    "llm": "LLMs: prompting and calling a model through an API",
    "rag": "RAG: embeddings, vector search and answering from your own documents",
    "langchain": "LangChain: chains and simple LLM apps",
    "opencv": "OpenCV: read, resize and process images",
    "yolo": "YOLO: object detection with a pretrained model",
    "fastapi": "FastAPI basics: build a small API and test it",
    "flask": "Flask: routes and a small web app",
    "django": "Django: models, views and templates",
    "rest api": "REST APIs: GET/POST requests and JSON",
    "docker": "Docker fundamentals: images, containers and a Dockerfile",
    "mlflow": "MLflow: track experiments and models",
    "aws": "AWS basics: S3, EC2 and deploying a small app",
    "azure": "Azure basics: deploying a small app",
    "gcp": "Google Cloud basics: storage and deploying a small app",
}


def generate_roadmap(missing_skills):
    """One skill per week, in the order the role lists them. Returns [(week, text)]."""
    roadmap = []
    for week, skill in enumerate(missing_skills, start=1):
        topic = LEARNING_TOPICS.get(skill, f"Learn the basics of {skill}")
        roadmap.append((f"Week {week}", topic))
    return roadmap
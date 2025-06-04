# Dynamic-k Retrieval Dataset

This repository provides question-answer pairs and utilities for experimenting with dynamic-k retrieval for RAG (Retrieval-Augmented Generation).

## Dataset

The dataset contains conversational QA pairs focused on computer science topics. It was derived from an existing corpus and split into train/validation/test files using `dyanmic-k-data-prep.ipynb`.

| Split | File | Entries |
|-------|------|--------|
| Train | `cs_qa_train.jsonl` | 277 |
| Validation | `cs_qa_val.jsonl` | 35 |
| Test | `cs_qa_test.jsonl` | 35 |

Each line in these JSONL files has the following keys:

```json
{"question": "...", "answer": "...", "tag": "..."}
```

The dataset is intended for building a retrieval index of facts and experimenting with variable `k` values when fetching context.

## Environment check

Run `env_check.py` to verify Torch, FAISS and model dependencies:

```bash
python env_check.py
```

The script loads a Llama model from a local path and prints library versions. Make sure the required weights are available or adjust `MODEL_PATH` in the script.

## Notebook

`dyanmic-k-data-prep.ipynb` demonstrates the full preprocessing pipeline:

1. Loading the original dataset
2. Converting to JSONL
3. Splitting into train/val/test
4. Building a fact corpus and computing embeddings

Open the notebook with Jupyter:

```bash
jupyter notebook dyanmic-k-data-prep.ipynb
```

## Requirements

- Python 3.12
- `torch`
- `faiss`
- `sentence-transformers`
- `transformers`
- `fastapi`
- `pandas`
- `scikit-learn`

Install packages via `pip install -r requirements.txt` if such a file is provided, or install them individually.


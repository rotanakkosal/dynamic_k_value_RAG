# Dynamic-K RAG Data Prep

This repository contains utilities for preparing a small QA dataset and testing
retrieval with dynamic `k` values.  Paths in the notebook and helper scripts rely
on the environment variables below to locate data or model weights.

## Environment Variables

- `DATA_DIR` – path to the directory containing all dataset files
  (defaults to the project root).  Expected files include:
  - `Computer_Science_Theory_QA.json`
  - `Computer_Science_Theory_QA.csv`
  - `cs_qa_train.jsonl`, `cs_qa_val.jsonl`, `cs_qa_test.jsonl`
  - `facts.jsonl`, `facts_hnsw.index`, `fact_id_map.pkl`
  - `dynamic_k_labels.jsonl`
- `MODEL_PATH` – optional path to a local HuggingFace model directory used by
  `env_check.py` (defaults to `Llama-2-7b-chat-hf`).

A minimal directory layout looks like:

```
project/
├── dyanmic-k-data-prep.ipynb
├── env_check.py
├── README.md
├── <dataset files>
└── <model directory>
```

Set `DATA_DIR` and `MODEL_PATH` in your environment or modify them in the
scripts before running the notebook or `env_check.py`.

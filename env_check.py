import torch
import faiss
from sentence_transformers import SentenceTransformer
from transformers import LlamaTokenizer, LlamaForCausalLM
from fastapi import FastAPI

MODEL_PATH = ("/home/kosal/AI/Dynamic_K_RAG/Llama-2-7b-chat-hf")

print("Torch:", torch.__version__, "| GPU available:", torch.cuda.is_available())
print("FAISS:", faiss.__version__)
print("SentenceTransformer load:", SentenceTransformer("all-MiniLM-L6-v2").get_sentence_embedding_dimension())

tokenizer = LlamaTokenizer.from_pretrained(MODEL_PATH)
model = LlamaForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float16,
    device_map="auto",
    local_files_only=True,
    low_cpu_mem_usage=True
)

print("LLaMA tokenizer & model loaded")
app = FastAPI()
print("FastAPI imported:", FastAPI)


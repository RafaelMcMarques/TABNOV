""" Taken from https://github.com/A-Chicharito-S/FoMo-0D/blob/main/ReadMe.md """

import os
from pathlib import Path
import sys

# FoMo and its modified PFN package are bundled sources, not installed packages.
FOMO_ROOT = Path(__file__).resolve().parents[3] / "models" / "FoMo-0D"
sys.path.insert(0, str(FOMO_ROOT))

# Configure the model process before importing PyTorch or Hugging Face.
# Weights are downloaded on first run and cached inside this Python environment.
environment = Path(sys.prefix)
os.environ.update(
    OMP_NUM_THREADS="4",
    MKL_NUM_THREADS="4",
    HF_HUB_CACHE=str(environment / "huggingface" / "hub"),
    HF_XET_CACHE=str(environment / "huggingface" / "xet"),
    HF_HUB_DISABLE_XET="1",
)

import torch
from fomo_hub import FoMo0DHub   # the HuggingFace hub-aware class wrapper for FoMo-0D

def main():
    # 1) Download + rebuild the model from the Hub
    repo_id = "YuchenShen/FoMo-0D"
    model = FoMo0DHub.from_pretrained(repo_id, map_location="cpu").eval()

    print("Model loaded successfully from Hub.")

    # 2) Create dummy input matching FoMo-0D’s expected shape (seq_len, batch_size, num_features)
    # For example: (seq_len=10, batch=3, num_features=100)
    bs = 3
    train_x = torch.randn(5000, bs, model.config["num_features"])
    test_x = torch.randn(10, bs, model.config["num_features"])


    # 3) Run forward pass
    with torch.no_grad():
        out = model(train_x=train_x, test_x=test_x)  # (test_x_seq_len=10, batch_size, num_classes=2)

    print(f"Output shape: {out.shape} and type: {type(out)}")
    # would be: "Output shape: torch.Size([10, 3, 2]) and type: <class 'torch.Tensor'>"

if __name__ == "__main__":
    main()

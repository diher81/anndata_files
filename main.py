import numpy as np
import pandas as pd
import anndata as ad
import scanpy as sc
from scipy.sparse import csr_matrix

# Load file
adata = sc.read_h5ad("/Users/diher/Library/CloudStorage/OneDrive-WageningenUniversity&Research/InternshipTBB/Files/mouse-tchic-gene-level.filter.h5ad")

# Basic overview
print(adata)
print("Shape:", adata.shape)
print("Cells:", adata.n_obs)
print("Genes:", adata.n_vars)

# Inspect cell metadata
print("cell metadata:\n", adata.obs.head())
print("cell metadata - keys:\n", adata.obs.keys())

# Inspect gene metadata
print("gene metadata:\n", adata.var.head())
print("gene metadata - keys:\n", adata.var.keys())

# List available analysis results and matrices
print("Layers:", list(adata.layers.keys()))
print("Obsm:", list(adata.obsm.keys()))
print("Obsp:", list(adata.obsp.keys()))
print("Unstructured data:", list(adata.uns.keys()))

# matrix
print("adata.X:\n", adata.X)

# data
print("Unstructured data - keys:\n", list(adata.uns.keys()))
print("Unstructured data - values:\n", list(adata.uns.values()))

# layers
print("Main matrix:", adata.X.shape)
for name in adata.layers:
    layer = adata.layers[name]
    print(
        f"Layer: {name}, "
        f"Type: {type(layer)}, "
        f"Shape: {layer.shape}"
    )
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

# List available analysis results and matrices
print("Layers:", list(adata.layers.keys()))
print("Obsm:", list(adata.obsm.keys()))
print("Obsp:", list(adata.obsp.keys()))
print("Unstructured data:", list(adata.uns.keys()))

# matrix
print("adata.X:\n", adata.X)
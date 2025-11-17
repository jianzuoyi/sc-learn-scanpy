import scanpy as sc

breakpoint()
adata = sc.datasets.krumsiek11()
adata.obs_names_make_unique()
#sc.pp.filter_cells(adata, min_genes=3)
sc.pp.filter_genes(adata, min_cells=3)
adata

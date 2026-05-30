#!/usr/bin/env python3
"""Feasibility + timing probe for ESMFold on this CPU before committing to
six full-length (710 aa) refolds. Loads esmfold_v1 (downloads ~2.8 GB on first
use), folds a short peptide and a medium fragment, prints timing so we can
extrapolate the 710-aa cost. Does NOT fold the full protein."""
import sys, types, time

def main():
    import torch
    # ESMFold needs the openfold CUDA attention ext; mock it so it falls back
    # to pure-PyTorch attention on CPU (same trick the MCP runner uses).
    sys.modules.setdefault("attn_core_inplace_cuda", types.ModuleType("attn_core_inplace_cuda"))
    torch.set_num_threads(max(1, (torch.get_num_threads() or 4)))
    print(f"[env] torch {torch.__version__}  threads={torch.get_num_threads()}  cuda={torch.cuda.is_available()}", flush=True)

    import esm
    t = time.time()
    model = esm.pretrained.esmfold_v1().eval()
    print(f"[load] esmfold_v1 loaded in {time.time()-t:.1f}s", flush=True)

    for label, seq in [("pep25", "MKTAYIAKQRQISFVKSHFSRQLEE"),
                       ("frag60", "MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQAPILSRVGDGTQDNLSGAEKAVQVKVK")]:
        t = time.time()
        with torch.no_grad():
            pdb = model.infer_pdb(seq)
        print(f"[fold] {label} ({len(seq)} aa) in {time.time()-t:.1f}s  pdb_bytes={len(pdb)}", flush=True)

    print("[ok] ESMFold runs on CPU. Extrapolate ~O(L^2) for 710 aa.", flush=True)

if __name__ == "__main__":
    main()

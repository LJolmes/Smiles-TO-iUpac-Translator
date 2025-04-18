# -*- coding: utf-8 -*-

"""
STOUT Python Package.
This repository contains STOUT-V2,
The second version of STOUT: SMILES TO IUPAC Translator.
Which is built using the same concept as a Neural Machine Translation(NMT) using Transformers.


Typical usage example:

from stout import translate_forward, translate_reverse

# SMILES to IUPAC translation
smiles = "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"
iupac_name = translate_forward(SMILES)
print(iupac_name)

# IUPAC to SMILES translation
iupac_name = "1,3,7-trimethylpurine-2,6-dione"
SMILES = translate_reverse(iupac_name)
print(SMILES)

For comments, bug reports or feature ideas,
please raise a issue on the Github repository.

"""

import os

# Use Keras 2 instead of 3, see
# https://blog.tensorflow.org/2024/03/whats-new-in-tensorflow-216.html
os.environ["TF_USE_LEGACY_KERAS"] = "1"
del os

__version__ = "2.1.0"

__all__ = [
    "STOUT",
]


from .stout import translate_forward, translate_reverse

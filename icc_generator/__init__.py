#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the advanced GUI version of the Windows Command Line script
that does the ICC Profile creation.

Workflow:

from icc_generator.api import ICCGenerator
ig = ICCGenerator()

# Set Printer Details
ig.printer_brand
ig.printer_model

# Set Paper Details
ig.paper_brand
ig.paper_model
ig.paper_finish
ig.paper_size

# Set Ink Details
ig.ink_brand

# Profiling workflow, run the following commands in the given order:
ig.generate_target()
ig.generate_tif()
ig.print_charts()
ig.read_charts()
ig.generate_profile()
ig.check_profile(True)

# Optional
# To fix misread patches (patches with too high dE values)
# re-read the chart in resume mode
ig.read_charts(resume=True, read_mode=0) # use read_mode=1 for patch-by-patch

# Finally install the profile
ig.install_profile()
"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


__version__ = "0.3.1"



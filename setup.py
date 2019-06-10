#!/usr/bin/env python

from distutils.core import setup
import os
home = os.path.expanduser('~')
config = os.path.join(home,'.config/ant_config')
setup(
      name='pyrosetta_helper',
      description='Ambiguous Nucleotide Tool (ANT), software for generating and evaluating degenerate codons for natural and expanded genetic codes.',
      author='Martin Engqvist',
      author_email='martin_engqvist@hotmail.com',
      version='0.2',
      data_files=[(config,['settings.txt'])],
      packages=['ANT'])

# Copyright (c) 2020, RTE (https://www.rte-france.com)
# See AUTHORS.txt
# This Source Code Form is subject to the terms of the Mozilla Public License, version 2.0.
# If a copy of the Mozilla Public License, version 2.0 was not distributed with this file,
# you can obtain one at http://mozilla.org/MPL/2.0/.
# SPDX-License-Identifier: MPL-2.0
# This file is part of L2RPN Baselines, L2RPN Baselines a repository to host baselines for l2rpn competitions.

import setuptools
from setuptools import setup
__version__ = "0.6.0.post1"


pkgs = {
    "required": [
        "grid2op",
        "statsmodels>=0.11.1",
        "scipy>=1.4.1",
        "numpy",
        "gym>=0.17.2"
    ],
    "extras": {
        "docs": [
            "numpydoc>=0.9.2",
            "sphinx>=2.4.4",
            "sphinx-rtd-theme>=0.4.3",
            "sphinxcontrib-trio>=1.1.0",
            "autodocsumm>=0.2.7",
            "cvxpy"
        ],
        "optional": ["grid2op[optional]>=1.6.5",
                     "tensorflow>=2.2.0",
                     "Keras>=2.3.1",
                     "torch>=1.4.0",
                     "scikit-learn>=0.22.2",
                     ],
        "PPO_RLLIB": ["ray[rllib]",
                      "jsonpickle",
                      "lightsim2grid"],
        "PPO_SB3": ["stable_baselines3", "lightsim2grid"]
    }
}

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    

setup(name='l2rpn_baselines',
      version=__version__,
      description='L2RPN Baselines a repository to host ' \
      'baselines for l2rpn competitions.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
          "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "Intended Audience :: Science/Research",
          "Natural Language :: English"
      ],
      keywords='ML powergrid optmization RL power-systems',
      author='Benjamin DONNOT',
      author_email='benjamin.donnot@rte-france.com',
      url="https://github.com/rte-france/L2RPN_Baselines",
      license='MPL',
      packages=setuptools.find_packages(),
      include_package_data=True,
      install_requires=pkgs["required"],
      extras_require=pkgs["extras"],
      zip_safe=False,
      entry_points={}
      )

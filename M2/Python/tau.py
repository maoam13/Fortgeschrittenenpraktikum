# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 00:50:36 2019

@author: Moritz
"""

import numpy as np
import matplotlib.pyplot as plt
import Praktikummo2 as p
from scipy.interpolate import interp1d
import scipy.constants as c
import scipy.optimize as opt

m = 0.057*c.m_e
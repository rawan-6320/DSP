from Task1 import *
from TestFile import *


# ==========================================
# Test 1: Addition - Signal1 + Signal2
# ==========================================

indices, samples = add_signals(
    signals,
    ['Signal1', 'Signal2']
)

AddSignalSamplesAreEqual(
    'Signal1.txt',
    'Signal2.txt',
    indices,
    samples
)


# ==========================================
# Test 2: Addition - Signal1 + Signal3
# ==========================================

indices, samples = add_signals(
    signals,
    ['Signal1', 'signal3']
)

AddSignalSamplesAreEqual(
    'Signal1.txt',
    'Signal3.txt',
    indices,
    samples
)


# ==========================================
# Test 3: Multiplication - Signal1 * 5
# ==========================================

indices = signals['Signal1']['indices'].copy()

samples = [
    sample * 5
    for sample in signals['Signal1']['samples']
]

MultiplySignalByConst(
    5,
    indices,
    samples
)


# ==========================================
# Test 4: Multiplication - Signal2 * 10
# ==========================================

indices = signals['Signal2']['indices'].copy()

samples = [
    sample * 10
    for sample in signals['Signal2']['samples']
]

MultiplySignalByConst(
    10,
    indices,
    samples
)
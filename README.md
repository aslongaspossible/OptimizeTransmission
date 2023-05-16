# OptimizeTransmission

Returns optimal transport window for thermoelectric materials, given lattice thermal conductance $\beta$ and any density of modes (DoM).

You can define your own DoM function, and get optimal transport window as

```python
from linear.equation import solve4beta
results = solve4beta(<your_DoM>) 
```

The result is a table; each row is for different $\beta$, and columns are

- $1/\beta$, 
- start position of transport window, 
- end position of transport window, 
- figure of merit, 
- power factor (in the unit of $k_B^2/h$), 
- Seebeck coefficient (in the unit of $k_B/e$),

successively.

More demo scripts can be seen in `linear/*.ipynb`.
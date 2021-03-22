func = @(x)(x - 1) * (x - 2) * (x - 3) * (x - 4) - 10^(-6) * x^6

fzero(func, 4)

import torch
x = torch.arange(12, dtype=torch.float32)
print(x)
print(x.numel())

X = x.reshape(3, 4)
print(X)


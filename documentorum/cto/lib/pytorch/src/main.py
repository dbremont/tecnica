import torch
from rich import print

x = torch.arange(12, dtype=torch.float32)

print(x)
print(type(x))
print(x.shape)
print(x.reshape(3, 4))
print(torch.zeros((2, 3, 4)))
print(torch.ones((2, 3, 4)))
print(torch.randn(3, 4))
print(torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]]))
print(x[2:5])
x[1] = 17
print(x)

## Some Operations
print(x + 2)
print(x * 2)
print(x ** 2)
print(x.sum())
print(x.mean()) 
print(x.max())
print(x.min())
print(x.argmax())
print(x.argmin())
print(torch.exp(x))


## Torch Fynctions

## Broadcasting
a = torch.tensor([[1], [2], [3]])  # Shape: (3, 1)
b = torch.tensor([10, 20, 30])     # Shape: (3,)
print(a + b)  # Broadcasting: (3, 1) + (3,) -> (3, 3)

## Saving Memory

c = torch.zeros_like(b)

print(id)
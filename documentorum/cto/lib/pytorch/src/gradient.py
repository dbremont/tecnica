import torch
from  rich import print

x = torch.arange(4.0)
x.requires_grad_(True)
y = 2 * torch.dot(x, x)

print(y)
print(x)
print(x.grad)
y.backward()
print(x.grad)  # Should print the gradient of y with respect to x

print(y)


"""
import torch

x = torch.tensor(2.0, requires_grad=True)
y = x ** 2            # y = x²
y.backward()          # Compute dy/dx

print(x.grad)         # Output: tensor(4.)
"""
import torch

# creiamo un tensore da un array
new_tensor = torch.Tensor([[1, 2], [3, 4]])

# creiamo un tensore 2x3 con valori random
empty_tensor = torch.Tensor(2, 3)

# creiamo un tensore 2x3 con valori random -1 e 1
uniform_tensor = torch.Tensor(2, 3).uniform_(-1, 1)

# creiamo un tensore 2x3 con valori random distribuiti nell'intervallo [0, 1)
rand_tensor = torch.rand(2, 3)

# creiamo un tensore 2x3 con valori a zero
zero_tensor = torch.zeros(2, 3)
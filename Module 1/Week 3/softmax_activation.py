import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        """Initialize the Softmax module without any additional parameters."""
        super().__init__()

    def forward(self, data):
        """Compute the softmax of a tensor by exponentiating and normalizing.

        Args:
            data (Tensor): The input tensor for which the softmax is to be computed.

        Returns:
            Tensor: A tensor where each value is transformed into the range (0, 1) representing a probability distribution.
        """
        exp_data = torch.exp(data)
        exp_sum = torch.sum(exp_data)
        return exp_data / exp_sum


class StableSoftmax(nn.Module):
    def __init__(self):
        """Initialize the StableSoftmax module without any additional parameters."""
        super().__init__()

    def forward(self, data):
        """Compute a numerically stable softmax by shifting the input values.

        This method improves numerical stability by subtracting the maximum input value before exponentiation.

        Args:
            data (Tensor): The input tensor for which the stable softmax is to be computed.

        Returns:
            Tensor: A tensor where each value is transformed into a normalized range, adjusted for numerical stability.
        """
        max_value = torch.max(data)
        stable_exp = torch.exp(data - max_value)
        exp_sum = torch.sum(stable_exp, dim=-1, keepdim=True)
        return stable_exp / exp_sum


# Example usage of the Softmax and StableSoftmax modules
data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print("Softmax output:", output)

data = torch.Tensor([1, 2, 3])
softmax_stable = StableSoftmax()
output = softmax_stable(data)
print("Stable Softmax output:", output)

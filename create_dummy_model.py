import torch
import torch.nn as nn
import os

# Make sure model directory exists
os.makedirs("model", exist_ok=True)

# Define a simple model
class GenericModel(nn.Module):
    def __init__(self, input_dim=1, output_dim=1):
        super().__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.linear(x)

# Instantiate the model
model = GenericModel()
model.eval()  # set to evaluation mode

# Create a dummy input for tracing
example_input = torch.randn(1, 1)

# Convert to TorchScript using tracing
traced_model = torch.jit.trace(model, example_input)

# Save the TorchScript model
traced_model.save("model/model.pt")
print("TorchScript model saved to model/model.pt")

import torch

def preprocess(data: dict) -> torch.Tensor:
    """
    Convert input JSON to tensor.
    Example: data = {"inputs": [1.0, 2.0, 3.0]}
    """
    inputs = data.get("inputs")
    if inputs is None:
        raise ValueError("Missing 'inputs' key")
    return torch.tensor(inputs, dtype=torch.float32)

def postprocess(output: torch.Tensor) -> dict:
    """
    Convert tensor output to JSON serializable.
    """
    return {"outputs": output.detach().cpu().numpy().tolist()}


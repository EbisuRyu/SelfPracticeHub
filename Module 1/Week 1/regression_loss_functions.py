import math
import random

def is_integer(value):
    """Check if the input value is an integer."""
    try:
        int(value)
        return True
    except ValueError:
        return False

def mae(predictions, targets):
    """Mean Absolute Error (MAE) loss function."""
    if isinstance(predictions, list):
        return sum(abs(p - t) for p, t in zip(predictions, targets)) / len(predictions)
    return abs(predictions - targets)

def mse(predictions, targets):
    """Mean Squared Error (MSE) loss function."""
    if isinstance(predictions, list):
        return sum((p - t) ** 2 for p, t in zip(predictions, targets)) / len(predictions)
    return (predictions - targets) ** 2

def rmse(predictions, targets):
    """Root Mean Squared Error (RMSE) loss function."""
    return math.sqrt(mse(predictions, targets))

def apply_loss_function():
    """Prompt user for input, generate samples, and apply the selected loss function."""
    num_samples = input('Input number of samples (integer number) which are generated: ')
    
    if not is_integer(num_samples):
        print('Number of samples must be an integer.')
        return 0
    
    num_samples = int(num_samples)
    loss_name = input('Input loss name (MAE|MSE|RMSE): ')
    
    loss_functions = {
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse
    }
    
    if loss_name not in loss_functions:
        print(f'{loss_name} is not a supported loss function.')
        return 0
    
    loss_function = loss_functions[loss_name]
    
    predictions = [random.random() * 10 for _ in range(num_samples)]
    targets = [random.random() * 10 for _ in range(num_samples)]
    
    for i, (prediction, target) in enumerate(zip(predictions, targets)):
        loss = loss_function(prediction, target)
        print(f'Loss name: {loss_name}, Sample: {i}, Prediction: {prediction}, Target: {target}, Loss: {loss}')
    
    final_loss = loss_function(predictions, targets)
    print(f'Final {loss_name}: {final_loss}')
    
    return 0

# Test the function
apply_loss_function()
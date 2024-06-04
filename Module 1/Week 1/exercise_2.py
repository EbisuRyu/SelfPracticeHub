import math

def is_number(n):
    """Check if the input is a number."""
    try:
        float(n)
        return True
    except ValueError:
        return False

def relu(x):
    """ReLU activation function."""
    return max(0, x)

def sigmoid(x):
    """Sigmoid activation function."""
    return 1 / (1 + math.exp(-x))

def elu(x, alpha=0.01):
    """ELU activation function."""
    return alpha * (math.exp(x) - 1) if x <= 0 else x

def apply_activation_function():
    """Prompt user for input and apply the selected activation function."""
    x = input('Input x = ')
    if not is_number(x):
        print('x must be a number')
        return 0

    x = float(x)
    activation_function = input('Input activation function (sigmoid|relu|elu): ')
    
    if activation_function not in ['sigmoid', 'relu', 'elu']:
        print(f'{activation_function} is not supported')
        return 0

    activation_function_value = None
    if activation_function == 'relu':
        activation_function_value = relu(x)
    elif activation_function == 'sigmoid':
        activation_function_value = sigmoid(x)
    elif activation_function == 'elu':
        activation_function_value = elu(x)

    print(f'{activation_function}: f({x}) = {activation_function_value}')
    return 0

# Test the function
apply_activation_function()
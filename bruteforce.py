import itertools

def brute_force_password(password):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    attempts = 0

    for length in range(1, len(password) + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return (guess, attempts)

# Example usage:
password = 'secret'
result = brute_force_password(password)
print(f"Password: {result[0]}")
print(f"Attempts: {result[1]}")

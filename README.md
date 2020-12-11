## My own implementation of DES algorithm

### Example usage of DES

```python
%load_ext autoreload
%autoreload 2

from des import DES, DEFAULT_KEY
```

```python
print('Default key = ')
for i in range(len(DEFAULT_KEY)):
    if i % 8 == 0:
        print()
    print(DEFAULT_KEY[i], " ", end='')
```

    Default key = 
    
    0  1  1  0  0  0  1  1  
    0  1  1  1  0  0  1  0  
    0  1  1  0  1  0  0  1  
    0  1  1  0  1  1  0  1  
    0  1  1  0  1  0  0  1  
    0  1  1  0  1  1  1  0  
    0  1  1  0  0  0  0  1  
    0  1  1  0  1  1  0  0  


```python
from scripts.text_utils import bits_to_text

message = 'Testing DES algorithm'

d = DES()
encrypted_message = d.encrypt(message)
print('Encrypting: {}'.format(message))
print('Output: ')
for x in encrypted_message:
    print(bits_to_text(x).hex())
```

    Encrypting: Testing DES algorithm
    Output: 
    8648efda9281fd22
    c87953be6c52dfb9
    3fa3125e95bae469
    


```python
print('Decryption: ')
output = []
for x in encrypted_message:
    decrypted_message = d.decrypt(x)
    output.append(decrypted_message)
    print(decrypted_message)

print('Output: {}'.format(''.join(map(lambda x: x.decode('ascii'), output))))

```

    Decryption: 
    b'Testing '
    b'DES algo'
    b'rithm   '
    Output: Testing DES algorithm   
    

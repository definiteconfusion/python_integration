# Python Binary Wrapper

Simple Python script to allow for interoperability with low-level languages  

## Syntax

### Python

```python
# May want to change source file
from main import Binary

# `Binary` class to setup with executable
Output = Binary(
    './<path to binary subfile>',
    exampleArg1,
    exampleArg2,
    exampleArg3
).get()
print(Output)
```

### Rust

```rust
// Needed for argument collection
let args: Vec<String> = env::args().collect();
// use arguments as needed
let exampleOutput: String = "Hello World"
println!("{}", exampleOutput)
```

### Terminal

```bash
# Commands
cargo build
python3 playground.py

# Output
['Hello', 'World']
```

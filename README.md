# Recycling Used Parts for Fun and Profit

The only classifier that's finished is the MLP.

There's a Makefile with some utility tasks for running the programs.

The nets/ and imgs/ directories need to exist in order to run the programs
without errors

```sh
# Run MLP training on the train_data.csv set and generate network files under
nets directory.

$ make train_mlp
```

```sh
# Run the MLP with many epochs of trining on the given data file.

$ EPOCHS=100 DATA_FILE=test_data.csv make execute_mlp
```

```sh
# Run the MLP with many epochs of trining on the given data file.

$ EPOCHS=100 DATA_FILE=test_data.csv make execute_mlp
```

The plotting routines are pretty self-explanatory from the Makefile.

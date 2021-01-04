# Python Asymmetric Encryption CLI

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/mdcg/python-asymmetric-encryption-cli/blob/main/LICENSE)

:lock: *A CLI to illustrate the steps of asymmetric cryptography.*

This is a CLI written in Python to illustrate the use of asymmetric cryptography. Basically, we are using the RSA algorithm in the whole process, which goes from the generation of public and private keys, to the encryption and decryption of text files.

## First steps

Using this CLI is very simple, especially if you are using a Linux-based environment. It is interesting that you have Python installed on your machine, preferably versions 3.6 or higher.

To generate the CLI executable, use the following command:

```
make compile
```

The above command will generate two folders: `build` and` dist`. The executable will be located in the `dist` folder. Go to the executable directory (it will be called `cli`) and run the following command:

```
./cli
```

After executing the above command, you will see output like this:

```
Usage: cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  decrypt
  encrypt
  key-gen
```

You can check the details of each of the commands using `cli <COMMAND> --help`. For example:

```
[mdcg@minerva dist]$ ./cli key-gen --help
Usage: cli key-gen [OPTIONS]

Options:
  --keys_path TEXT  Path to save the public and private key.
  --help            Show this message and exit.
```

## Contributing

Feel free to do whatever you want with this project. :-)
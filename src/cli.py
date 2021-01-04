import os

import click

from src.decrypt import decrypt_data
from src.encrypt import encrypt_data
from src.key_gen import generate_public_key


def default_keys_path():
    return os.path.join(os.environ.get("HOME", "."), "keys")


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--keys_path",
    default=default_keys_path(),
    help="Path to save the public and private key.",
)
def key_gen(keys_path):
    try:
        generate_public_key(keys_path)
    except Exception as err:
        click.echo(err)


@cli.command()
@click.option(
    "--public_key",
    default=f"{os.path.join(default_keys_path(), 'public.pem')}",
    help="Public key path.",
)
@click.argument("filename")
def encrypt(public_key, filename):
    try:
        encrypt_data(filename, public_key)
    except Exception as err:
        click.echo(err)


@cli.command()
@click.option(
    "--private_key",
    default=f"{os.path.join(default_keys_path(), 'private.pem')}",
    help="Private key path.",
)
@click.argument("filename")
@click.argument("new_filename")
def decrypt(private_key, filename, new_filename):
    # try:
    decrypt_data(filename, new_filename, private_key)
    # except Exception as err:
    #     click.echo(err)


if __name__ == "__main__":
    cli()

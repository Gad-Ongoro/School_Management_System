import click

@click.command()
@click.option("--count", default=1, help="Number of print()s.")
@click.option("--name", prompt="Name")
@click.option("--age", prompt="Age", type=int)

def hello(count, name, age):
    """Sample program"""
    # age = click.prompt('Please enter your age', type=int)
    for _ in range(count):
        click.echo("Hello, %s!" % name)
        click.echo("You are %s years old" % age)

if __name__ == '__main__':
    hello()
    
import click


@click.command()
@click.option('--input',
              type=click.File('rb'),
              required=True,
              nargs=1,
              help='The path of scan file needs to be recognize the character')
@click.option('--output',
              type=click.File('wb'),
              required=True,
              nargs=1,
              help='The path of the output file has recognized the character')
@click.option('--verbose', is_flag=True, help='The verbose mode')
def cli(input, output, verbose):
    if verbose:
        click.echo('In the verbose mode!')

    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(chunk)
        output.flush()

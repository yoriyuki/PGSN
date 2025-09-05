# pgsn_cli.py
import os.path
from pickle import FALSE

import click
import importlib.util
import sys
from pathlib import Path
import tempfile

# GSNのタイプとgraphvizのshapeを対応付ける辞書
default_layout = {
    "rankdir": "TB",
    "splines": "spline",
    "nodesep": "0.6",
    "ranksep": "1.2"
}

# (Imports and file loading function remain the same)
try:
    from pgsn import dsl
    from pgsn import gsn
    from pgsn.pgsn_term import Term
except ImportError as e:
    print(f"Error: Could not import PGSN modules: {e}")
    print("Please ensure gsn.py, dsl.py, and pgsn_term.py are accessible.")
    sys.exit(1)


def load_term_from_py_file(file_path: str, term_name: str) -> Term:
    # ... (This function's implementation is unchanged)
    path = Path(file_path).resolve()
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None:
        raise ImportError(f"Could not create a module spec from '{path}'.")

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    term_object = getattr(module, term_name, None)
    if term_object is None:
        raise AttributeError(f"Object '{term_name}' not found in module '{spec.name}'.")

    return term_object


# ===============================================================
# The Command-Line Interface
# ===============================================================

@click.group()
def cli():
    """A command-line tool for Programmable GSN (PGSN)."""
    pass


@cli.command()
@click.argument('input_file', type=click.Path(exists=True, dir_okay=False))
@click.option('--term-name', default='main', help='The name of the Term object to evaluate in the Python file.')
@click.option('--doc-type', '-d', default='plain', type=click.Choice(['plain', 'json']),
              help='The output image format.')
@click.option('--output', '-o', default=None, help='The output filename (without extension).')
@click.option('--steps', '-s', help='maximum number of steps of evaluation', type=int, default=1000000)
def doc(input_file, term_name, doc_type, output, steps):
    """Evaluates a PGSN term and output doc in a specified format."""

    click.echo(f"Generating '{output}' from '{input_file}'", err=True)

    try:
        if input_file.endswith('.py'):
            term = load_term_from_py_file(input_file, term_name)
            click.echo(f"Evaluating term '{term_name}'...", err=True)
            evaluated_gsn = term.fully_eval(steps=steps)

        elif input_file.endswith('.json'):
            with open(input_file, 'r', encoding='utf-8') as f:
                json_str = f.read()

            click.echo("Validating and parsing JSON file...", err=True)
            term = dsl.json_loads(json_str)
            evaluated_gsn = term.fully_eval(steps=steps)

        else:
            click.echo(f"Error: Unsupported file type for '{input_file}'. Please use .py or .json.", err=True)
            return

        tree = gsn.gsn_tree(evaluated_gsn)

        if doc_type == 'plain':
            document = tree.show(stdout=False)
        elif doc_type == 'json':
            document = tree.to_json()
        else:
            click.echo(f"Error: Unsupported document type. Please use plain or json.", err=True)
            return

        if output:
            if output == '-':
                # The user explicitly asked for stdout
                click.echo(document)
            else:
                with open(output, 'w', encoding='utf-8') as f:
                    f.write(document)
        else:
                click.echo(document)

        click.echo("Done.", err=True)

    except Exception as e:
        click.echo(f"Error: {e}", err=True)


@cli.command()
@click.argument('input_file', type=click.Path(exists=True, dir_okay=False))
@click.option('--term-name', default='main', help='The name of the Term object to evaluate in the Python file.')
@click.option('--output', '-o', default=None, help='The output filename (without extension).')
@click.option('--format', '-f', 'image_format', type=click.Choice(['svg', 'png', 'pdf']), default='svg',
              help='The output image format.')
@click.option('--steps', '-s', help='maximum number of steps of evaluation', type=int, default=1000000)
@click.option('--layout', '-l', type=dict[str, str], default={}, help='layout option')
def render(input_file, term_name, output, image_format, steps, layout):
    """Evaluates a PGSN term and renders it as a graph."""

    click.echo(f"Processing '{input_file}' to render a graph...", err=True)

    try:
        if input_file.endswith('.py'):
            term = load_term_from_py_file(input_file, term_name)
            click.echo(f"Evaluating term '{term_name}'...", err=True)
            evaluated_gsn = term.fully_eval(steps=steps)

        elif input_file.endswith('.json'):
            with open(input_file, 'r', encoding='utf-8') as f:
                json_str = f.read()

            click.echo("Validating and parsing JSON file...", err=True)
            term = dsl.json_loads(json_str)
            evaluated_gsn = term.fully_eval(steps=steps)

        else:
            click.echo(f"Error: Unsupported file type for '{input_file}'. Please use .py or .json.", err=True)
            return

        dot = gsn.gsn_dot(evaluated_gsn, layout_attrs=layout)

        if output:
            if output == '-':
                # The user explicitly asked for stdout
                dot = gsn.gsn_dot(evaluated_gsn)

                graph_data = dot.pipe(format=image_format)
                click.echo(graph_data)
            else:
                # The user specified a file name
                click.echo(f"Saving graph to '{output}.{image_format}'...", err=True)
                dot.render(filename=output, view=False, cleanup=True)

        else:
            # No output file was specified, so we check the context
            if sys.stdout.isatty():
                # Display the diagram
                    dot.view(cleanup=True)
            else:
                # We are in a pipe or redirection. Follow the Unix philosophy.
                graph_data = dot.pipe(format=image_format)
                click.echo(graph_data)

        click.echo("Done.", err=True)

    except Exception as e:
        click.echo(f"Error: {e}", err=True)


@cli.command()
@click.argument('python_file', type=click.Path(exists=True, dir_okay=False))
@click.option('--term-name', default='main', help='The name of the Term object to evaluate.')
@click.option('--output', '-o', default=None, help='The output JSON filename.')
def compile(python_file, term_name, output, eval, steps):
    """Compiles a trusted PGSN (.py) file into a secure JSON format."""
    click.echo(f"Compiling '{python_file}' to JSON...", err=True)

    try:
        term = load_term_from_py_file(python_file, term_name)

        click.echo(f"Saving JSON to '{output}'...", err=True)
        json_str = dsl.json_dumps(term, indent=None, separators=(',', ':'))

        with open(output, 'w', encoding='utf-8') as f:
            f.write(json_str)

        click.echo("Done.")

    except Exception as e:
        click.echo(f"Error: {e}", err=True)


if __name__ == '__main__':
    cli()
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from notes.models import Base, Note, Category

engine = create_engine('sqlite:///notes.db')
Session = sessionmaker(bind=engine)

@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj['Session'] = Session()

@cli.command()
@click.argument('title')
@click.argument('content')
@click.pass_context
def add(ctx, title, content):
    session = ctx.obj['Session']
    note = Note(title=title, content=content)
    session.add(note)
    session.commit()
    click.echo(f"Added note: {title}\nContent: {content}")

@cli.command()
@click.pass_context
def list(ctx):
    session = ctx.obj['Session']
    notes = session.query(Note).all()
    click.echo("Listing all notes:")
    for note in notes:
        click.echo(f"{note.title}: {note.content}")

@cli.command()
@click.argument('title')
@click.pass_context
def delete(ctx, title):
    session = ctx.obj['Session']
    note = session.query(Note).filter_by(title=title).first()
    if note:
        session.delete(note)
        session.commit()
        click.echo(f"Deleted note: {title}")
    else:
        click.echo(f"Note '{title}' not found.")

@cli.command()
@click.argument('keyword')
@click.pass_context
def search(ctx, keyword):
    session = ctx.obj['Session']
    notes = session.query(Note).filter(Note.title.ilike(f'%{keyword}%') | Note.content.ilike(f'%{keyword}%')).all()
    click.echo("Search results:")
    for note in notes:
        click.echo(f"{note.title}: {note.content}")

@cli.command()
@click.argument('category')
@click.pass_context
def search_category(ctx, category):
    session = ctx.obj['Session']
    notes = session.query(Note).join(Note.category).filter(Category.name.ilike(f'%{category}%')).all()
    click.echo("Search results by category:")
    for note in notes:
        click.echo(f"{note.title}: {note.content}")


if __name__ == "__main__":
    cli(obj={})

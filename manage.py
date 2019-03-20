import click
import certificates


@click.group()
def db():
    pass


@db.command()
def init():
    app = certificates.create_app()
    with app.app_context():
        certificates.connection.db.create_all()
    click.echo("Initialized database")


if __name__ == '__main__':
    db()

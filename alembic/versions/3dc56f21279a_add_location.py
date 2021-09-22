"""add location

Revision ID: 3dc56f21279a
Revises: 31da296bfbc5
Create Date: 2021-09-22 15:48:02.818043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3dc56f21279a'
down_revision = '31da296bfbc5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "location",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("title", sa.String),
            sa.Column("content", sa.String),
            sa.Column("html_render", sa.String, server_default=""))


def downgrade():
    op.drop_table("location", "html_render")
"""Create manuals

Revision ID: 31da296bfbc5
Revises: 36cd29044d6f
Create Date: 2021-09-16 17:36:02.108833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31da296bfbc5'
down_revision = '36cd29044d6f'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
            "manual",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("title", sa.String),
            sa.Column("content", sa.String),
            sa.Column("html_render", sa.String, server_default=""))


def downgrade():
    op.drop_table("manual", "html_render")
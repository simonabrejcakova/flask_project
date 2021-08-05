"""add

Revision ID: 34ce280bf81
Revises: 7ca8415e7e9b
Create Date: 2021-08-05 14:49:21.057836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34ce280bf81'
down_revision = '7ca8415e7e9b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("article",
            sa.Column("html_render", sa.String, server_default=""))


def downgrade():
    op.drop_column("article", "html_render")

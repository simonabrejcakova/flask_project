"""adds newsletter

Revision ID: 36cd29044d6f
Revises: 34ce280bf81
Create Date: 2021-08-06 18:18:26.782945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36cd29044d6f'
down_revision = '34ce280bf81'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "newsletter",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("email", sa.String, unique=True))


def downgrade():
    op.drop_table("newsletter")

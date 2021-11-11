"""add column typ

Revision ID: 41de4377114b
Revises: 40424646ccb9
Create Date: 2021-11-11 18:27:04.878457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41de4377114b'
down_revision = '40424646ccb9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("shift",
            sa.Column("typ", sa.String, server_default=""))



def downgrade():
    op.drop_column("shift", "typ")

"""Create shift table

Revision ID: 40424646ccb9
Revises: 4f5008ab1a14
Create Date: 2021-11-11 14:09:44.756567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40424646ccb9'
down_revision = '4f5008ab1a14'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "shift",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("username", sa.String),
            sa.Column("truck", sa.String),
            sa.Column("date", sa.String),
            sa.Column("start_time", sa.String),
            sa.Column("end_time", sa.String),
            sa.Column("notes", sa.String))


def downgrade():
    op.drop_table("shift")

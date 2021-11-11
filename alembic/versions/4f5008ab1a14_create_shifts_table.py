"""Create shifts table

Revision ID: 4f5008ab1a14
Revises: 40c4c2ef12f9
Create Date: 2021-11-11 12:02:46.969098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f5008ab1a14'
down_revision = '40c4c2ef12f9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "shifts",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("username", sa.String),
            sa.Column("truck", sa.String),
            sa.Column("date", sa.String),
            sa.Column("start_time", sa.String),
            sa.Column("end_time", sa.String),
            sa.Column("notes", sa.String))



def downgrade():
    op.drop_table("shifts")

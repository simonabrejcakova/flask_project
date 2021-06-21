"""create user table

Revision ID: 7ca8415e7e9b
Revises: 
Create Date: 2021-06-21 13:40:50.502138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ca8415e7e9b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "user",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("username", sa.String),
            sa.Column("password", sa.String))


def downgrade():
    op.drop_table("user")

"""empty message

Revision ID: 5396f23bc379
Revises: 078dadcce1cf
Create Date: 2024-11-11 12:53:02.181206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5396f23bc379'
down_revision = '078dadcce1cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('sex',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=20),
               existing_nullable=False)
        batch_op.alter_column('job',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=150),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('job',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('sex',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)

    # ### end Alembic commands ###

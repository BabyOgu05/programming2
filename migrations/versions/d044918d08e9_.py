"""empty message

Revision ID: d044918d08e9
Revises: 59cb490a3ef2
Create Date: 2024-12-05 18:21:39.467666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd044918d08e9'
down_revision = '59cb490a3ef2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('result', schema=None) as batch_op:
        batch_op.alter_column('economy',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.Boolean(),
               existing_nullable=True)
        batch_op.alter_column('welfare',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.Boolean(),
               existing_nullable=True)
        batch_op.alter_column('security',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.Boolean(),
               existing_nullable=True)
        batch_op.alter_column('environment',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.Boolean(),
               existing_nullable=True)
        batch_op.alter_column('political_reform',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.Boolean(),
               existing_nullable=True)
        batch_op.alter_column('technology',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.Boolean(),
               existing_nullable=True)
        batch_op.alter_column('human_rights',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.Boolean(),
               existing_nullable=True)
        batch_op.alter_column('defense',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.Boolean(),
               existing_nullable=True)
        batch_op.alter_column('legislation',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.Boolean(),
               existing_nullable=True)
        batch_op.alter_column('total',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.Boolean(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('result', schema=None) as batch_op:
        batch_op.alter_column('total',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=150),
               existing_nullable=True)
        batch_op.alter_column('legislation',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=150),
               existing_nullable=True)
        batch_op.alter_column('defense',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=150),
               existing_nullable=True)
        batch_op.alter_column('human_rights',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=150),
               existing_nullable=True)
        batch_op.alter_column('technology',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=150),
               existing_nullable=True)
        batch_op.alter_column('political_reform',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=150),
               existing_nullable=True)
        batch_op.alter_column('environment',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=150),
               existing_nullable=True)
        batch_op.alter_column('security',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=150),
               existing_nullable=True)
        batch_op.alter_column('welfare',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=150),
               existing_nullable=True)
        batch_op.alter_column('economy',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(length=150),
               existing_nullable=True)

    # ### end Alembic commands ###

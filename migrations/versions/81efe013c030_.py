"""empty message

Revision ID: 81efe013c030
Revises: 8f892418c3af
Create Date: 2024-12-03 15:51:00.836370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81efe013c030'
down_revision = '8f892418c3af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('economy', sa.Boolean(), nullable=True),
    sa.Column('welfare', sa.Boolean(), nullable=True),
    sa.Column('security', sa.Boolean(), nullable=True),
    sa.Column('environment', sa.Boolean(), nullable=True),
    sa.Column('political_reform', sa.Boolean(), nullable=True),
    sa.Column('technology', sa.Boolean(), nullable=True),
    sa.Column('human_rights', sa.Boolean(), nullable=True),
    sa.Column('defense', sa.Boolean(), nullable=True),
    sa.Column('legislation', sa.Boolean(), nullable=True),
    sa.Column('total', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('result')
    # ### end Alembic commands ###
"""empty message

Revision ID: c487f33e6392
Revises: 
Create Date: 2025-06-09 11:29:36.805978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c487f33e6392'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pet',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('animal_type', sa.String(), nullable=False),
    sa.Column('personality', sa.String(), nullable=False),
    sa.Column('color', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pets_table')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pets_table',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('animal_type', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('personality', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('color', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pets_table_pkey')
    )
    op.drop_table('pet')
    # ### end Alembic commands ###

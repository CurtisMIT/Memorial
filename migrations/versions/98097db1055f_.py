"""empty message

Revision ID: 98097db1055f
Revises: fa37caf08444
Create Date: 2020-02-02 03:44:24.841454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98097db1055f'
down_revision = 'fa37caf08444'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('milestones', sa.Column('end', sa.String(), nullable=True))
    op.add_column('milestones', sa.Column('start', sa.String(), nullable=True))
    op.drop_column('milestones', 'year')
    op.drop_column('milestones', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('milestones', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('milestones', sa.Column('year', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('milestones', 'start')
    op.drop_column('milestones', 'end')
    # ### end Alembic commands ###

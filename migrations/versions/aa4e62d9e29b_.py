"""empty message

Revision ID: aa4e62d9e29b
Revises: 0ac025b8ec66
Create Date: 2020-02-01 15:47:41.689712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa4e62d9e29b'
down_revision = '0ac025b8ec66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('bio', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('people', 'bio')
    # ### end Alembic commands ###

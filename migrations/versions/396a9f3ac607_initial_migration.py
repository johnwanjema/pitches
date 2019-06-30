"""Initial Migration

Revision ID: 396a9f3ac607
Revises: 8d33fec3b35a
Create Date: 2019-06-30 20:51:26.817617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '396a9f3ac607'
down_revision = '8d33fec3b35a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    # ### end Alembic commands ###

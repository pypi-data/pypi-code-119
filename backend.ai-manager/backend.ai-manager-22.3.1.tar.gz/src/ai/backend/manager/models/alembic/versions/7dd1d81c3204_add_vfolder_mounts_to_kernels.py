"""add-vfolder-mounts-to-kernels

Revision ID: 7dd1d81c3204
Revises: 60a1effa77d2
Create Date: 2022-03-09 16:41:48.304128

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7dd1d81c3204'
down_revision = '60a1effa77d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kernels', sa.Column('vfolder_mounts', sa.JSON(), nullable=True))
    op.create_index('ix_keypairs_resource_policy', 'keypairs', ['resource_policy'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_keypairs_resource_policy', table_name='keypairs')
    op.drop_column('kernels', 'vfolder_mounts')
    # ### end Alembic commands ###

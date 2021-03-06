"""empty message

Revision ID: 04b3030c6e07
Revises: 2d45bf9db48b
Create Date: 2019-01-16 16:46:28.979378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04b3030c6e07'
down_revision = '2d45bf9db48b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('district', sa.Column('sn_name', sa.String(length=1024), nullable=True))
    op.add_column('district', sa.Column('sn_province', sa.String(length=1024), nullable=True))
    op.add_column('district', sa.Column('tm_name', sa.String(length=1024), nullable=True))
    op.add_column('district', sa.Column('tm_province', sa.String(length=1024), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('district', 'tm_province')
    op.drop_column('district', 'tm_name')
    op.drop_column('district', 'sn_province')
    op.drop_column('district', 'sn_name')
    # ### end Alembic commands ###

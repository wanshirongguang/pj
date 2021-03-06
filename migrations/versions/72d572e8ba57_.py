"""empty message

Revision ID: 72d572e8ba57
Revises: cc74994fc101
Create Date: 2018-09-28 21:55:36.039327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72d572e8ba57'
down_revision = 'cc74994fc101'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('postnum', table_name='board')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('postnum', 'board', ['postnum'], unique=True)
    # ### end Alembic commands ###

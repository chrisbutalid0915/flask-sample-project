"""added disabled column at user model.

Revision ID: 2d486dc82d7d
Revises: 34177b95ec6c
Create Date: 2024-05-25 11:46:38.055992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d486dc82d7d'
down_revision = '34177b95ec6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('disabled', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('disabled')

    # ### end Alembic commands ###

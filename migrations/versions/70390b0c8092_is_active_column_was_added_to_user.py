"""is_active column was added to user

Revision ID: 70390b0c8092
Revises: a45dbafd4392
Create Date: 2023-06-02 16:48:48.574943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70390b0c8092'
down_revision = 'a45dbafd4392'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###

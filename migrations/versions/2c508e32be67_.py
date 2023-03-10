"""empty message

Revision ID: 2c508e32be67
Revises: 3ecd262f893f
Create Date: 2022-12-20 12:50:57.321962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c508e32be67'
down_revision = '3ecd262f893f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('packages', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=160),
               type_=sa.String(length=256),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('packages', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=160),
               existing_nullable=True)

    # ### end Alembic commands ###

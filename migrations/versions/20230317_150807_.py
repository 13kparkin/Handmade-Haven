"""empty message

Revision ID: c063969bb399
Revises: ffdc0a98111c
Create Date: 2023-03-17 15:08:07.384221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c063969bb399'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('images', schema=None) as batch_op:
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.alter_column('total_price',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
        batch_op.alter_column('date',
               existing_type=sa.DATETIME(),
               type_=sa.Date(),
               existing_nullable=False)

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
        batch_op.create_unique_constraint(None, ['name'])
        batch_op.create_unique_constraint(None, ['description'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('price',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.Date(),
               type_=sa.DATETIME(),
               existing_nullable=False)
        batch_op.alter_column('total_price',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    with op.batch_alter_table('images', schema=None) as batch_op:
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###
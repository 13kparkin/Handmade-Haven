"""add reviews table

Revision ID: 37988859022d
Revises: ffdc0a98111c
Create Date: 2023-03-10 18:21:59.097794

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")
# revision identifiers, used by Alembic.
revision = '37988859022d'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column("product_id",sa.Integer(),nullable=False),
    sa.Column('comment', sa.String(length=500), nullable=False),
    sa.Column('stars', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(["user_id"],["users.id"]))
    
    if environment == "production":
        op.execute(f"ALTER TABLE reviews SET SCHEMA {SCHEMA}")
        
def downgrade():
  op.drop_table("reviews")
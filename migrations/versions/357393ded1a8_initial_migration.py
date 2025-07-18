"""Initial migration

Revision ID: 357393ded1a8
Revises: 
Create Date: 2025-06-27 11:22:23.291408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '357393ded1a8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('author', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('reviewer', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.create_index('idx_reviews_book_id', ['book_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.drop_index('idx_reviews_book_id')

    op.drop_table('review')
    op.drop_table('book')
    # ### end Alembic commands ###

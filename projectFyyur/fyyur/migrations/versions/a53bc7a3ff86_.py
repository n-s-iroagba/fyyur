"""empty message

Revision ID: a53bc7a3ff86
Revises: 
Create Date: 2022-06-22 09:57:03.886907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a53bc7a3ff86'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('date',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('state',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_name', sa.String(), nullable=False),
    sa.Column('artist_photo', sa.String(), nullable=False),
    sa.Column('artist_phone', sa.String(length=20), nullable=False),
    sa.Column('talent', sa.Boolean(), nullable=True),
    sa.Column('state_id', sa.Integer(), nullable=False),
    sa.Column('book_from', sa.Time(), nullable=True),
    sa.Column('book_to', sa.Time(), nullable=True),
    sa.ForeignKeyConstraint(['state_id'], ['state.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('artist_name'),
    sa.UniqueConstraint('artist_phone')
    )
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('state_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['state_id'], ['state.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('time',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.String(), nullable=False),
    sa.Column('date_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['date_id'], ['date.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('venue_phone', sa.String(length=14), nullable=False),
    sa.Column('venue_photo', sa.String(), nullable=False),
    sa.Column('talent', sa.Boolean(), nullable=True),
    sa.Column('state_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['state_id'], ['state.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('venue_phone')
    )
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('artist_genre',
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], )
    )
    op.create_table('previous_show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('photo', sa.String(), nullable=False),
    sa.Column('date_id', sa.Integer(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['date_id'], ['date.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('show_name', sa.String(), nullable=False),
    sa.Column('show_cover_photo', sa.String(), nullable=False),
    sa.Column('date_id', sa.Integer(), nullable=True),
    sa.Column('show_artist_id', sa.Integer(), nullable=True),
    sa.Column('show_venue_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['date_id'], ['date.id'], ),
    sa.ForeignKeyConstraint(['show_artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['show_venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('show_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('show')
    op.drop_table('previous_show')
    op.drop_table('artist_genre')
    op.drop_table('address')
    op.drop_table('venue')
    op.drop_table('time')
    op.drop_table('city')
    op.drop_table('artist')
    op.drop_table('state')
    op.drop_table('genre')
    op.drop_table('date')
    # ### end Alembic commands ###

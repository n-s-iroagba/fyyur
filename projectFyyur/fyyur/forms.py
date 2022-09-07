from re import M
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,SelectField,TimeField,DateField
from wtforms.validators import DataRequired
from wtforms.fields import FileField,BooleanField,DateField,TimeField



class SearchForm(FlaskForm):
    searched=StringField("",validators=[DataRequired()])
    search= SubmitField('search')


class Artist_Form(FlaskForm):
    artist_name=StringField("Name",validators=[DataRequired()])
    artist_photo=FileField("Cover photo",validators=[DataRequired()])
    city=StringField("City",validators=[DataRequired()])
    artist_state=StringField("State",validators=[DataRequired()])
    artist_phone=IntegerField("Phone number",validators=[DataRequired()])
    talent=BooleanField("Seeking talent?")
    genre1=StringField("Genre",validators=[DataRequired()])
    genre2=StringField("Genre")
    genre3=StringField("Genre")
    book_from=TimeField("book me from")
    book_to=TimeField("to")
    create= SubmitField('Register artist')

class Uartist_Form(FlaskForm):
    artist_name=StringField("Name",validators=[DataRequired()])
    artist_photo=FileField("Cover photo",validators=[DataRequired()])
    artist_city=StringField("City",validators=[DataRequired()])
    artist_state=StringField("State",validators=[DataRequired()])
    artist_phone=IntegerField("Phone number",validators=[DataRequired()])
    talent=BooleanField("Seeking talent?")
    genre1=StringField("Genre",validators=[DataRequired()])
    genre2=StringField("Genre")
    genre3=StringField("Genre")
    book_from=TimeField("book me from")
    book_to=TimeField("to")
    update= SubmitField('Update artist')

class Venue_Form(FlaskForm):
    venue_name=StringField("Venue's name",validators=[DataRequired()])
    address=StringField("Address",validators=[DataRequired()])
    city=StringField("City",validators=[DataRequired()])
    venue_state=StringField("State",validators=[DataRequired()])
    venue_phone=IntegerField("Phone number",validators=[DataRequired()])
    venue_photo=FileField("Venues's photo",validators=[DataRequired()])
    talent=BooleanField("Seeking talent?")
    create= SubmitField('register venue')


class Uvenue_Form(FlaskForm):
    venue_name=StringField("Venue's name",validators=[DataRequired()])
    address=StringField("Address",validators=[DataRequired()])
    venue_city=StringField("City",validators=[DataRequired()])
    venue_state=StringField("State",validators=[DataRequired()])
    venue_phone=IntegerField("Phone number",validators=[DataRequired()])
    venue_photo=FileField("Venues's photo",validators=[DataRequired()])
    talent=BooleanField("Seeking talent?")
    update= SubmitField('Update venue')

class Show_Form(FlaskForm):
    show_name=StringField("Show's name",validators=[DataRequired()])
    time=TimeField("Time",format="%H:%M",validators=[DataRequired()])
    show_cover_photo=FileField("Show's cover picture")
    show_artist_name=SelectField("Artist's name",choices=[],validators=[DataRequired()])
    show_date=DateField("Show's date",format='%m/%d/%y',validators=[DataRequired()])
    show_venue_name=SelectField("Show's venue",choices=[],validators=[DataRequired()])
    create= SubmitField('register show')


class Search(FlaskForm):
    searched=StringField('search',validators=[DataRequired()])
    search=SubmitField('search')
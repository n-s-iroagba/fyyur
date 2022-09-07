from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from typing import Literal
from random import choices
from forms import Uvenue_Form,Uartist_Form,Venue_Form,SearchForm,Show_Form,Artist_Form
from flask import request, session
import sys
from datetime import datetime
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker
from werkzeug.utils import secure_filename
from datetime import date
import uuid
import os
from datetime import datetime
from flask import Flask,render_template, redirect, url_for,flash
from flask_bootstrap import Bootstrap
fyyur = Flask(__name__,static_folder='static',template_folder='templates')
Bootstrap(fyyur)
db=SQLAlchemy(fyyur)
fyyur.config['SECRET_KEY']='chocho'
fyyur.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:97chocho@localhost:5432/fdb' 
fyyur.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
migrate=Migrate(fyyur,db)
#MODELS
artist_genre=db.Table('artist_genre',
        db.Column('artist_id',db.Integer,db.ForeignKey('artist.id')),
        db.Column('genre_id',db.Integer,db.ForeignKey('genre.id'))
        )

class Artists (db.Model):
    __tablename__ = 'artist'
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(),nullable=False,unique=True)
    artist_photo =db.Column(db.String(),nullable=False)
    artist_phone = db.Column(db.String(20),nullable=False,unique=True)
    talent=db.Column(db.Boolean())
    state_id= db.Column(db.Integer,db.ForeignKey('state.id'),nullable = False)
    book_from=db.Column(db.Time)
    book_to=db.Column(db.Time)
    genre=db.relationship('Genres', secondary=artist_genre, backref = 'artist' )
    shows=db.relationship('Shows', cascade="all",backref = 'artist' )
    previous_shows=db.relationship('Previous_shows', cascade="all",backref = 'artist')

class Genres (db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(),nullable=False)

class Shows (db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    show_name = db.Column(db.String(),nullable=False,unique=True)
    show_cover_photo = db.Column(db.String(),nullable=False)
    date_id= db.Column(db.Integer,db.ForeignKey('date.id'))
    show_artist_id= db.Column(db.Integer,db.ForeignKey('artist.id'))
    show_venue_id= db.Column(db.Integer,db.ForeignKey('venue.id'))

class Venues (db.Model):
    __tablename__ = 'venue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),nullable=False,unique=True)
    venue_phone = db.Column(db.String(14),nullable=False,unique=True)
    venue_photo = db.Column(db.String(),nullable=False)
    talent=db.Column(db.Boolean())
    state_id= db.Column(db.Integer,db.ForeignKey('state.id'),nullable = False)
    shows=db.relationship('Shows', cascade="all",backref = 'venue')
    previous_shows=db.relationship('Previous_shows', cascade="all",backref = 'venue')


class Previous_shows (db.Model):
    __tablename__ = 'previous_show'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(),nullable=False,unique=True)
    photo = db.Column(db.String(),nullable=False)
    date_id= db.Column(db.Integer,db.ForeignKey('date.id'))
    artist_id= db.Column(db.Integer,db.ForeignKey('artist.id'))
    venue_id= db.Column(db.Integer,db.ForeignKey('venue.id'))

class States (db.Model):
    __tablename__ = 'state'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(),nullable=False)
    artist=db.relationship('Artists', cascade="all,delete",backref = 'state' )
    venues=db.relationship('Venues', cascade="all,delete",backref = 'state' )
    city=db.relationship('City', cascade="all,delete",backref = 'state')

    
class City (db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(),nullable=False)
    state_id= db.Column(db.Integer,db.ForeignKey('state.id'),nullable = False)
    address=db.relationship('Address', cascade="all,delete",backref = 'city')

class Address (db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(),nullable=False)
    city_id= db.Column(db.Integer,db.ForeignKey('city.id'),nullable = False)
    
class Date (db.Model):
    __tablename__ = 'date'
    id = db.Column(db.Integer, primary_key=True)
    date=db.Column(db.Date)
    shows=db.relationship('Shows', cascade="all,delete",backref = 'date' )
    previous_shows=db.relationship('Previous_shows', cascade="all,delete",backref = 'date' )
    time=db.relationship('Time', cascade="all,delete",backref = 'date' )

class Time (db.Model):
    __tablename__ = 'time'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(),nullable=False)
    date_id= db.Column(db.Integer,db.ForeignKey('date.id'))
    




Session = sessionmaker()
session=Session()
session.expire_on_commit= False 

UPLOAD_FOLDER="static/images/"
fyyur.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

#ROUTES
@fyyur.route('/')
def index():
    #shows=Shows.query.all()
    #for show in shows:
        #if show.date()<datetime.now():
            #name=show.show_name
            #artist=show.artist
            #venue=show.venue
            #date=show.date
            #photo=show.show_cover_photo
            #try:
                #previous_show= Previous_shows(name=name,photo=photo)
                #previous_show.artist=artist
                #previous_show.venue=venue
                #previous_show.date=date
                #db.session.add(previous_show)
                #db.session.commit()
            #except:
                #db.session.rollback()
            #finally:
                #db.session.close()

    return render_template('pages/index.html')
#ALL ARTISTS
@fyyur.route('/artists')
def artists():
    artists=Artists.query.all()
    return render_template('pages/artists.html',artists=artists)


#ALL SHOWS
@fyyur.route('/shows')
def shows():
    shows=Shows.query.all()
    return render_template('pages/shows.html',shows=shows)

    
#ALL VENUES
@fyyur.route('/venues')
def venues():
    venues=Venues.query.all()
    return render_template('pages/venues.html',venues=venues)

# NEW ARTIST
@fyyur.route('/newartists',methods=['GET','POST'])
def newartist():
    naform = Artist_Form()
    if request.method=="POST":
        name=naform.artist_name.data
        photo=naform.artist_photo.data
        city=naform.city.data
        state=naform.artist_state.data
        phone=naform.artist_phone.data
        talent=naform.talent.data
        genre1=naform.genre1.data
        genre2=naform.genre2.data
        genre3=naform.genre3.data
        book_from=naform.book_from.data
        book_to=naform.book_to.data
        pic_filename=secure_filename(photo.filename)
        pic_name=str(uuid.uuid1()) + '_'+ pic_filename
        photo.save(os.path.join(fyyur.config['UPLOAD_FOLDER'],pic_name))
        artist_photo=pic_name
        try:
            artist=Artists(artist_name=name,artist_photo=artist_photo,artist_phone=phone,talent=talent,book_from=book_from,book_to=book_to)
            genre1=Genres(name=genre1)
            genre2=Genres(name=genre2)
            genre3=Genres(name=genre3)
            state=States(name=state)
            city=City(name=city)
            artist.state=state
            city.state=state
            artist.genre.append(genre1)
            artist.genre.append(genre2)
            artist.genre.append(genre3)
            db.session.add_all([artist,genre1,genre2,genre3,state,city])
            db.session.commit()
            flash(name +" " +'was added ')
            artists=Artists.query.all()
            return render_template('pages/artists.html',artists=artists)
        except:
            db.session.rollback()
            error=True
            print(sys.exc_info())
            flash(name +" "+ "could not be added")
            return render_template('forms/createartist.html',form=naform)
        finally:
            db.session.close()
        
    return render_template('forms/createartist.html',form=naform)
    




#CREATE SHOWS
@fyyur.route('/create/show', methods=['GET','POST'])
def cshows():
    sform=Show_Form()
    artists=list(Artists.query.all())
    artist_choices=[]
    for a in artists: artist_choices.append(a.artist_name)
    sform.show_artist_name.choices=artist_choices

    venues=list(Venues.query.all())
    venue_choices=[]
    for v in venues: venue_choices.append(v.name)
    sform.show_venue_name.choices=venue_choices
    if request.method=="POST":
        name=sform.show_name.data
        show_date=sform.show_date.data
        show_time=sform.time.data
        artist_name=sform.show_artist_name.data
        cover_photo=sform.show_cover_photo.data
        venue_name=sform.show_venue_name.data
        pic_filename=secure_filename(cover_photo.filename)
        pic_name=str(uuid.uuid1()) + '_'+ pic_filename
        cover_photo.save(os.path.join(fyyur.config['UPLOAD_FOLDER'],pic_name))
        cover_photo=pic_name
        artist=Artists.query.filter(Artists.artist_name==artist_name).first()
        venue=Venues.query.filter(Venues.name==venue_name).first()
        try:
            show=Shows(show_name=name,show_cover_photo=cover_photo)
            show.venue=venue
            show.artist=artist
            date=Date(date=show_date)
            time=Time(time=show_time)
            time.date=date
            show.date=date
            db.session.add_all([show,time,date])
            db.session.commit()
            flash('Awesome!,show is registered','good')
            return redirect(url_for('shows'))
        except Exception as exc:
            db.session.rollback()
            print(sys.exc_info())
            raise RuntimeError("could not register show") from exc
            
        finally:
            db.session.close()
    return render_template('forms/createshow.html',form=sform)


#CREATE VENUE
@fyyur.route('/newvenue', methods=['GET','POST'])
def cvenues():
    venues= Venues.query.all()
    vform = Venue_Form()
    if request.method=="POST":
        venue_name=vform.venue_name.data
        address=vform.address.data
        city=vform.city.data
        venue_state=vform.venue_state.data
        talent=vform.talent.data
        venue_photo=vform.venue_photo.data
        venue_phone=vform.venue_phone.data
        pic_filename=secure_filename(venue_photo.filename)
        pic_name=str(uuid.uuid1()) + '_'+ pic_filename
        venue_photo.save(os.path.join(fyyur.config['UPLOAD_FOLDER'],pic_name))
        venue_photo=pic_name
        try:
            venue=Venues(name=venue_name,venue_photo=venue_photo,venue_phone=venue_phone,talent=talent)
            address=Address(location=address)
            city=City(name=city)
            state=States(name=venue_state)
            address.city=city
            venue.state=state
            city.state=state
            db.session.add_all([venue,state,city,address])
            db.session.commit()
            flash('Awesome!,'+ vform.venue_name.data +'is registered,good!')
        except:
            error=True
            db.session.rollback()
            print(sys.exc_info())
            flash(vform.venue_name.data +" "+'is already taken')
                
        finally:
            db.session.close()
            return redirect (url_for('venues'))
        
    return render_template('forms/createvenue.html',form=vform)
                
            
#VIEW PARTICULAR ARTIST
@fyyur.route('/artist/<artist_id>',methods=['GET'])
def particular_artist(artist_id):
    partist=Artists.query.get(artist_id)
    genres=partist.genre

    state_and_city=db.session.query(States,City).\
        select_from(States).join(City).join(Artists).filter(Artists.id==artist_id)

    shows_details=db.session.query(Shows,Venues).\
        select_from(Shows).join(Venues).join(Artists).filter(Artists.id==artist_id)

    previous_shows_details=db.session.query(Previous_shows,Venues).\
        select_from(Previous_shows).join(Artists).join(Venues).filter(Artists.id==artist_id)
    
    return render_template('pages/artist.html',sc=state_and_city,artist=partist,shows=shows_details,previous_shows=previous_shows_details,genres=genres)


#DELETE PARTICLAR ARTIST
@fyyur.route('/artist/<artist_id>',methods=['DELETE'])
def delete_artist(artist_id):
    partist=Artists.query.get(artist_id)
    if request.method=='DELETE':
        try:
            db.session.delete(partist)
            db.session.commit()
            flash("artist was deleted!")
        except:
            db.session.rollback()
            error=True
            print(sys.exc_info())
            flash("artist could not be deleted!") 
        finally:
            return redirect (url_for('index'))

#DELETE PARTICULAR VENUE
@fyyur.route('/venue/<venue_id>',methods=['DELETE'])
def delete_venue(venue_id):
    venue=Venues.query.get(venue_id)
    if request.method=='DELETE':
        try:
            db.session.delete(venue)
            flash("venue was deleted!")
        except:
            db.session.rollback()
            error=True
            print(sys.exc_info())
            flash("venue could not be deleted!")
        finally:
            return url_for('index')


    
#VIEW PARTICULAR VENUE
@fyyur.route('/venue/<venue_id>',methods=['GET'])
def particular_venue(venue_id):
    venue=Venues.query.get(venue_id)
    venue_full_address=db.session.query(States,City).\
        select_from(States).join(City).join(Venues).filter(Venues.id==venue_id)

    shows_details=db.session.query(Shows,Artists).\
        select_from(Shows).join(Artists).join(Venues).filter(Venues.id==venue_id)

    previous_shows_details=db.session.query(Previous_shows,Artists).\
        select_from(Previous_shows).join(Artists).join(Venues).filter(Venues.id==venue_id)
    return render_template('pages/venue.html',venue=venue,previous_shows=previous_shows_details,shows=shows_details,complete_address=venue_full_address)


#VIEW AND DELETE PARTICULAR SHOW
@fyyur.route('/show/<show_id>',methods=['GET','DELETE'])
def particular_show(show_id):
    show=Shows.query.get(show_id)
    shows=Shows.query.all()
    venue= show.venue
    artist=show.artist
    if request.method =='DELETE':
        try:
            db.session.delete(show)
            flash('show was deleted')
            db.session.commit()
        except:
            db.session.rollback()
            flash( 'show was not deleted')
        finally:
                db.session.close()
        return render_template('pages/shows.html',shows=shows)
    return render_template('pages/show.html',show=show,venue=venue,artist=artist)
    
#NEW SHOWS
@fyyur.route('/newlycreatedshows')
def new_shows():
    new_shows=Shows.query.order_by(desc(Shows.id)).filter().limit(10).all()
    return render_template('newlyCreated/newshows.html',shows = new_shows)
#NEW ARTISTS
@fyyur.route('/newlycreatedartists')
def new_artists():



    new_artists=Artists.query.order_by(desc(Artists.id)).filter().limit(10).all()
    return render_template('newlyCreated/newartists.html',artists=new_artists)
#NEW VENUES
@fyyur.route('/newlycreatedvenues')
def new_venues():
    new_venues=Venues.query.order_by(desc(Venues.id)).filter().limit(10).all()
    return render_template('newlyCreated/newvenues.html',venues=new_venues)
 
 #PASS FORM TO NAVBAR  
@fyyur.context_processor
def form():
    seform=SearchForm()
    return dict(seform=seform)

#SEARCH
fyyur.route('/searched', methods=["POST"])
def search():
    if request.method=="POST":
        seform=SearchForm()
        searched=seform.searched.data()
        nvenue=Venues.query.filter(Venues.name.like('%' + searched.lower() +' %')).all()
        svenue=Venues.query.filter(Venues.venue_state.like('%' + searched.lower() +' %')).all()
        nshow=Shows.query.filter(Shows.show_name.like('%' + searched.lower() +' %')).all()
        nartist=Artists.query.filter(Artists.artist_name.like('%' + searched.lower() +' %')).all()
        sartist=Artists.query.filter(Artists.artist_state.like('%' + searched.lower() +' %')).all()
        return render_template('pages/searched.html',nvenue=nvenue,svenue=svenue,nartist=nartist,sartist=sartist,nshow=nshow)
    else:
        pass


#EDIT VENUE
@fyyur.route("/venue/<venue_id>/edit",methods=['GET','PATCH'])
def edit_venue(venue_id):
    venue= Venues.query.filter_by(Venues.id==venue_id)
    vform = Uvenue_Form()
    venue_name=venue.name
    if request.method=="PATCH":
        venue_city=vform.venue_city.data
        venue_state=vform.venue_state.data
        venue_address=vform.venue_address.data
        venue_photo=vform.venue_photo.data
        venue_phone=vform.venue_phone.data
        pic_filename=secure_filename(venue_photo.filename)
        pic_name=str(uuid.uuid1()) + '_'+ pic_filename
        venue_photo.save(os.path.join(fyyur.config['UPLOAD_FOLDER'],pic_name))
        venue_photo=pic_name
        venues=Venues.query.all()
        try:
            venue.venue_city=venue_city
            venue.venue_state=venue_state
            venue.venue_address=venue_address
            venue.venue_photo=venue_photo
            venue.venue_phone=venue_photo
            db.session.commit()
            flash(venue_name + 'updated')
        except:
            db.session.rollback()
            flash(venue_name + "could not be updated!")
        finally:
            db.session.close()
        return render_template('venues.html',venues=venues)
    return render_template('venueupdate.html',form =vform)


#UPDATE ARTIST
@fyyur.route('/artist/<artist_id>/edit',methods=['GET','PATCH'])
def edit_artist(artist_id):
    artist=Artists.query.filter(Artists.id==artist_id)
    aform = Uartist_Form()
    state=artist.state
    genres=artist.genre
    if request.method=="PATCH":
        artist_photo=aform.artist_photo.data
        city=aform.artist_city.data
        artist_state=aform.artist_state.data
        artist_phone=aform.artist_phone.data
        genre1=aform.genre1.data
        genre2=aform.genre2.data
        genre3=aform.genre3.data
        booking_hours_from=aform.booking_hours_from.data
        booking_hours_to=aform.booking_hours_to.data
        talent=aform.talent.data
        pic_filename=secure_filename(artist_photo.filename)
        pic_name=str(uuid.uuid1()) + '_'+ pic_filename
        artist_photo.save(os.path.join(fyyur.config['UPLOAD_FOLDER'],pic_name))
        artist_photo=pic_name
        artists=Artists.query.all()
        try:
            artist.artist_photo=artist_photo
            artist.artist_state=artist_state
            artist.artist_phone=artist_phone
            artist.booking_from=booking_hours_from
            artist.booking_to=booking_hours_to
            genres.genre1=genre1
            genres.genre3=genre2
            genres.genre2=genre3
            state.city=city
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return render_template('pages/artists.html',artists=artists)
    return render_template('forms/artistupdate.html',form=aform,artist=artist)


if __name__ == "__main__":
    fyyur.run(debug=True)
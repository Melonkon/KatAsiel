from core import app
from datetime import datetime
from .models import Cat, FeedingHistory
from flask import render_template, request, redirect, url_for, flash
from . import db


@app.route('/')
def list_cats():
    cats = Cat.query.all()
    return render_template('cats.html', cats=cats)

@app.route('/add', methods=['GET', 'POST'])
def add_cat():
    if request.method == 'POST':
        errors = []
        name = request.form['name']
        color = request.form['color']
        breed = request.form['breed']
        daily_food = request.form['daily_food']
        if not name or len(name) > 50:
            errors.append('Naam is verplicht en mag niet langer zijn dan 50 tekens.')

        if not color or color not in ['Zwart', 'Wit', 'Grijs', 'Oranje', 'Gestreept']:
            errors.append('Selecteer een geldige kleur.')

        if not breed or breed not in ['Bombay', 'Maine Coon', 'British Shorthair']:
            errors.append('Ras is verplicht en mag niet langer zijn dan 50 tekens.')

        try:
            daily_food = int(daily_food)
            if daily_food < 0:
                raise ValueError
        except ValueError:
            errors.append('Dagelijkse voeding moet een positief getal zijn.')

        if errors:
            for error in errors:
                flash(error)
                print(error)
            
        cat = Cat(
            name=request.form['name'],
            color=request.form['color'],
            breed=request.form['breed'],
            daily_food=request.form['daily_food']
        )
        
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for('list_cats'))
    return render_template('add_cat.html')

@app.route('/update/<int:cat_id>', methods=['GET', 'POST'])
def update_cat(cat_id):
    cat = Cat.query.get(cat_id)
    if request.method == 'POST':
        cat.name = request.form['name']
        cat.color = request.form['color']
        cat.breed = request.form['breed']
        cat.daily_food = request.form['daily_food']
        db.session.commit()
        return redirect(url_for('list_cats'))
    return render_template('update_cat.html', cat=cat)

@app.route('/delete/<int:cat_id>', methods=['GET', 'POST'])
def delete_cat(cat_id):
    cat = Cat.query.get(cat_id)
    
    if request.method == 'POST':

        if 'delete' in request.form:
            cat = Cat.query.get(cat_id)

            db.session.delete(cat)
            db.session.commit()
        
        return redirect(url_for('list_cats'))


    return render_template('delete.html', cat=cat)

@app.route('/cat/<int:cat_id>/food', methods=['GET', 'POST'])
def add_food(cat_id):
    cat = Cat.query.get_or_404(cat_id)
    if request.method == 'POST':
        errors = []

        date_str = request.form['date']
        food_consumed = request.form['food_consumed']

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            errors.append('Ongeldige datum. Gebruik het formaat JJJJ-MM-DD.')

        try:
            food_consumed = float(food_consumed)
            if food_consumed <= 0:
                raise ValueError
        except ValueError:
            errors.append('Gegeten voedsel moet een positief getal zijn.')

        if errors:
            for error in errors:
                flash(error)
            return redirect(url_for('add_food', cat_id=cat_id))

        existing_entry = FeedingHistory.query.filter_by(cat_id=cat.id, date=date).first()

        if existing_entry:
            existing_entry.food_consumed = food_consumed
            print(existing_entry.food_consumed)
        else:
            feeding_history_entry = FeedingHistory(cat_id=cat.id, food_consumed=food_consumed, date=date)
            db.session.add(feeding_history_entry)
        db.session.commit()
        
        return redirect(url_for('add_food', cat_id=cat_id))
    feeding_history = FeedingHistory.query.filter_by(cat_id=cat.id).order_by(FeedingHistory.date.desc()).all()
    return render_template('cat_food.html', cat=cat, feeding_history=feeding_history)

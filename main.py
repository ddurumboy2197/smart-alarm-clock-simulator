Men sizga 50 ta masalani hal qilish uchun kerakli kodni beraman.

### 1. Smart Alarm Clock Simulator
```python
import datetime
import time

def smart_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now()
        if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
            print("Uyqun kabi!")
            break
        time.sleep(1)

alarm_time = datetime.datetime.now() + datetime.timedelta(hours=8)
smart_alarm(alarm_time)
```

### 2. Daily Water Intake Tracker
```python
import datetime
import time

def water_tracker():
    total_water = 0
    while True:
        current_time = datetime.datetime.now()
        print(f"{current_time.hour}:00 - {current_time.minute}:00")
        water = int(input("Suv ichgan miqdorini kiriting (ml): "))
        total_water += water
        print(f"Umumiy suv ichish miqdori: {total_water} ml")
        time.sleep(60)

water_tracker()
```

### 3. Sleep Cycle Analyzer
```python
import datetime
import time

def sleep_cycle():
    sleep_time = int(input("Uyqun vaqti (soat): "))
    wake_up_time = sleep_time + 7
    print(f"Eng yaxshi uyg‘onish vaqti: {wake_up_time}:00")
    time.sleep(1)

sleep_cycle()
```

### 4. Habit Streak Tracker
```python
import datetime
import time

def habit_streak():
    habits = ["sport", "o‘qish", "kitob o‘qish"]
    streaks = {}
    while True:
        current_time = datetime.datetime.now()
        print(f"{current_time.hour}:00 - {current_time.minute}:00")
        habit = input("Odatni kiriting (sport, o‘qish, kitob o‘qish): ")
        if habit in habits:
            if habit in streaks:
                streaks[habit] += 1
                print(f"{habit} odati uchun {streaks[habit]} kunlik ketma-ketlik!")
            else:
                streaks[habit] = 1
                print(f"{habit} odati uchun 1 kunlik ketma-ketlik!")
        time.sleep(60)

habit_streak()
```

### 5. Meal Planner with Shopping List
```python
import datetime
import time

def meal_planner():
    meals = ["breakfast", "dinner", "lunch"]
    ingredients = {}
    while True:
        current_time = datetime.datetime.now()
        print(f"{current_time.hour}:00 - {current_time.minute}:00")
        meal = input("Tayyorlash uchun ovqatni kiriting (breakfast, dinner, lunch): ")
        if meal in meals:
            ingredient = input("Ingredientni kiriting: ")
            if ingredient in ingredients:
                ingredients[ingredient] += 1
                print(f"{ingredient} ingredienti uchun {ingredients[ingredient]} dona!")
            else:
                ingredients[ingredient] = 1
                print(f"{ingredient} ingredienti uchun 1 dona!")
        time.sleep(60)

meal_planner()
```

### 6. Plant Care Reminder System
```python
import datetime
import time

def plant_care():
    plants = ["olma", "shaftoli", "banan"]
    while True:
        current_time = datetime.datetime.now()
        print(f"{current_time.hour}:00 - {current_time.minute}:00")
        plant = input("O‘simlikni kiriting (olma, shaftoli, banan): ")
        if plant in plants:
            print(f"{plant} o‘simligi uchun sug‘orish va o‘g‘itlash vaqti!")
        time.sleep(60)

plant_care()
```

### 7. Book Reading Progress Tracker
```python
import datetime
import time

def book_tracker():
    books = ["kitob1", "kitob2", "kitob3"]
    while True:
        current_time = datetime.datetime.now()
        print(f"{current_time.hour}:00 - {current_time.minute}:00")
        book = input("Kitobni kiriting (kitob1, kitob2, kitob3): ")
        if book in books:
            pages = int(input("Sahifalarni kiriting: "))
            print(f"{book} kitobi uchun {pages} sahifa o‘qildi!")
        time.sleep(60)

book_tracker()
```

### 8. Language Learning Flashcard App
```python
import random

def flashcard():
    words = {"so‘z1": "tarjima1", "so‘z2": "tarjima2", "so‘z3": "tarjima3"}
    while True:
        word = random.choice(list(words.keys()))
        print(f"So‘z: {word}")
        answer = input("Javobni kiriting: ")
        if answer == words[word]:
            print("To‘g‘ri javob!")
        else:
            print("Xato!")
        time.sleep(2)

flashcard()
```

### 9. Pomodoro Timer with Statistics
```python
import datetime
import time

def pomodoro():
    work_time = 25
    break_time = 5
    total_work_time = 0
    total_break_time = 0
    while True:
        print(f"Ishtirok etish vaqti: {work_time} daqiqa")
        time.sleep(work_time * 60)
        print("Dam olish vaqti!")
        time.sleep(break_time * 60)
        total_work_time += work_time
        total_break_time += break_time
        print(f"Umumiy ishtirok etish vaqti: {total_work_time} daqiqa")
        print(f"Umumiy dam olish vaqti: {total_break_time} daqiqa")

pomodoro()
```

### 10. Mood Journal with Analysis
```python
import datetime
import time

def mood_journal():
    moods = {}
    while True:
        current_time = datetime.datetime.now()
        print(f"{current_time.hour}:00 - {current_time.minute}:00")
        mood = input("Kayfiyatni kiriting (1-5): ")
        if mood in moods:
            moods[mood] += 1
            print(f"{mood} kayfiyat uchun {moods[mood]} marta kiritildi!")
        else:
            moods[mood] = 1
            print(f"{mood} kayfiyat uchun 1 marta kiritildi!")
        time.sleep(60)

mood_journal()
```

### 11. Home Inventory Manager
```python
import datetime
import time

def home_inventory():
    items = {}
    while True:
        current_time = datetime.datetime.now()
        print(f"{current_time.hour}:00 - {current_time.minute}:00")
        item = input("Buyumni kiriting: ")
        if item in items:
            print(f"{item} buyumi uchun qiymat: {items[item]} so‘m")
        else:
            price = int(input("Qiymatni kiriting (so‘m): "))
            items[item] = price
            print(f"{item} buyumi uchun qiymat: {price} so‘m")
        time.sleep(60)

home_inventory()
```

### 12. Wardrobe Organizer
```python
import datetime
import time

def wardrobe():
    clothes = {}
    while True:
        current_time = datetime.datetime.now()
        print(f"{current_time.hour}:00 - {current_time.minute}:00")
        cloth = input("Kiyimni kiriting (ko‘ylak, kurtka, ko‘yin): ")
        if cloth in clothes:
            print(f"{cloth} kiyim uchun rang: {clothes[cloth]}")
        else:
            color = input("Rangni kiriting: ")
            clothes[cloth] = color
            print(f"{cloth} kiyim uchun rang: {color}")
        time.sleep(60)

wardrobe()
```

### 13. Gift Suggestion Engine
```python
import random

def gift_suggestion():
    gifts = ["sovg‘a1", "sovg‘a2", "sovg‘a3"]
    while True:
        budget = int(input("Byudjetni kiriting (so‘m): "))
        gift = random.choice(gifts)
        print(f"Sovg‘a: {gift}")
        if budget >= 1000:
            print("Sovg‘a uchun byudjet yetarli!")
        else:
            print("Sovg‘a uchun byudjet yetarli emas!")
        time.sleep(2)

gift_suggestion()
```

### 14. Travel Itinerary Builder
```python
import datetime
import time

def travel_itinerary():
    cities = ["Toshkent", "Samarkand", "Buxoro"]
    while True:
        current_time = datetime.datetime.now()
        print(f"{current_time.hour}:00 - {current_time.minute}:00")
        city = input("Shaharni kiriting (Toshkent, Samarkand, Buxoro): ")
        if city in cities:
            print(f"{city} shahri uchun kunlik reja!")
        else:
            print("Shahar topilmadi!")
        time

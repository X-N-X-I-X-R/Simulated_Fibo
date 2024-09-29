import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time
import math
import random
import tkinter as tk

# ודא שאתה משתמש ב-backend שתומך באנימציה אינטראקטיבית כמו 'TkAgg' או 'Qt5Agg'
matplotlib.use('TkAgg')

# פונקציה לחישוב רמות פיבונאצ'י
def calculate_fibonacci_levels(min_price, max_price):
    fib_levels = [0.0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0, 1.618, 2.618, 3.618]
    levels = {}
    for level in fib_levels:
        price_at_level = max_price - (level * (max_price - min_price))
        levels[level] = price_at_level
    return levels

# פונקציה שמדמה עליות וירידות במחיר עם תיקונים
def simulate_market_movement(start_price, min_price, max_price, total_steps=10, interval_minutes=1):
    current_price = start_price
    prices = [current_price]
    
    for step in range(total_steps):
        # שינוי רנדומלי גדול יותר בתנועה
        change = random.uniform(-5, 5)  # טווח רנדומלי גדול יותר
        # תנועה מחזורית רנדומלית: תדירות המחזור משתנה רנדומלית
        cycle = random.uniform(0.5, 1.5) * math.sin(step / random.uniform(1, 10)) * 10
        change += cycle

        # הוספת רעש רנדומלי קטן (רעשים קטנים נוספים)
        change += random.gauss(0, 1)

        # קפיצות חדות יותר בכל שלב אקראי
        if random.random() < 0.1:  # סיכוי של 10% לקפיצה משמעותית במחיר
            change += random.uniform(-20, 20)

        current_price += change

        # שמירה על הטווח של המחיר בין min_price ל-max_price
        current_price = max(min(current_price, max_price), min_price)
        prices.append(current_price)

        # המתנה של דקה לדימוי שוק ריאליסטי (במקום זמן אמיתי, נשנה ל-loop קצר)
        time.sleep(0.1)  # שינוי לשימוש בזמן מדומה כדי להאיץ את הסימולציה
        yield prices  # מחזיר את רשימת המחירים עד כה

# פונקציה לציור הגרף בתנועה
def plot_dynamic_graph(start_price, min_price, max_price, total_steps=10, interval_minutes=1):
    # יצירת חלון חדש עם tkinter להצגת המחיר הנוכחי
    root = tk.Tk()
    root.title("Current Price")
    root.geometry("200x100")

    # תווית להצגת המחיר הנוכחי
    price_label = tk.Label(root, text="Current Price: ", font=("Arial", 24))
    price_label.pack()

    # יצירת גרף עם matplotlib
    plt.ion()  # הפעלה של מצב אינטראקטיבי (עדכון בזמן אמת)
    fig, ax = plt.subplots(figsize=(20, 20))  # גודל מותאם של הגרף
    prices = []
    line, = ax.plot(prices, color='blue', label='Price', lw=2)

    ax.set_xlim(0, total_steps)
    ax.set_ylim(min_price, max_price)

    # כותרות הגרף והצירים
    ax.set_title("Simulated Market Movement with Fibonacci Levels", fontsize=14)
    ax.set_xlabel(f"Time Interval (minutes)", fontsize=12)
    ax.set_ylabel("Price", fontsize=12)

    # צבעים שונים לרמות הפיבונאצ'י
    fib_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'cyan', 'magenta', 'brown']

    fib_lines = []  # רשימה של קווי הפיבונאצ'י שנרשום כדי למחוק אותם מאוחר יותר

    for step, current_prices in enumerate(simulate_market_movement(start_price, min_price, max_price, total_steps, interval_minutes)):
        prices = current_prices
        line.set_xdata(np.arange(len(prices)))
        line.set_ydata(prices)
        ax.set_xlim(0, len(prices))  # עדכון טווח x
        ax.set_ylim(min(prices) - 10, max(prices) + 10)  # עדכון טווח y

        # מחיקת קווי הפיבונאצ'י הישנים לפני הוספת החדשים
        for fib_line in fib_lines:
            fib_line.remove()
        fib_lines = []

        # חישוב רמות פיבונאצ'י והצגתן בגרף
        levels = calculate_fibonacci_levels(min_price, max(prices))
        for i, (level, price) in enumerate(levels.items()):
            fib_line = ax.axhline(price, linestyle='--', color=fib_colors[i % len(fib_colors)], label=f'Fibonacci {level*100:.1f}%')
            fib_lines.append(fib_line)  # שמירה של כל קו כדי שנוכל למחוק אותו בעדכון הבא

        # עדכון המחיר הנוכחי בתווית בחלון tkinter
        price_label.config(text=f"Current Price: {prices[-1]:.2f}")

        # הצגת רמות פיבונאצ'י באגדה
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys(), loc='upper left', fontsize=10)

        plt.draw()
        plt.pause(0.1)  # השהייה קצרה בין כל עדכון של הגרף

        # עדכון חלון tkinter
        root.update()

    plt.ioff()  # יציאה ממצב אינטראקטיבי
    plt.show()
    root.mainloop()  # שמירה על חלון tkinter פתוח


# קריאה לפונקציה עם מחיר התחלתי 100 ותנועה במשך 10 דקות
plot_dynamic_graph(100,0, 1000, total_steps=1000, interval_minutes=1)






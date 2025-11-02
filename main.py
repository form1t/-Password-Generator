from flask import Flask, render_template, request
import random

symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
letter = ['A','B','C','D','E','F','G']
numbers = ['1','2','3','4','5','6','7','8','9','0']

chitats = [ "Будь собой. Остальные роли уже заняты. — Оскар Уайльд",
    "Успех — это идти от неудачи к неудаче, не теряя энтузиазма. — Уинстон Черчилль",
    "Лучше меньше, да лучше. — Лев Толстой",
    "Мечтай не о деньгах, а о делах, которые принесут деньги. — Элон Маск",
    "Ты — это то, что ты делаешь, когда это трудно. — Дерек Сиверс",
    "Не бойся медленно идти, бойся стоять. — Китайская мудрость",
    "Хочешь изменить мир — начни с себя. — Махатма Ганди"
]


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    lenght = None
    password = ""
    if request.method == 'POST':
        lenght = int(request.form['lenght'])
        vse_symbol = letter + symbols + numbers
        for i in range(lenght):
            password += random.choice(vse_symbol)
    return render_template('home.html', lenght=lenght, password=password)







@app.route('/chitata', methods=['GET', 'POST'])
def chitata():
    result = random.choice(chitats)

    return render_template('chitata.html', result = result)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contacts.html')







if __name__ == "__main__":
    app.run(debug=True)
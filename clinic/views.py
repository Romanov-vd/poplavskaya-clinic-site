from django.shortcuts import render


def index(request):
    context = {
        'active_page': 'index',
        'clinic_name': 'Медицинский центр «Новая Линия»',
        'slogan': 'Правильное направление к долголетию',
        'features': [
            'Передовые методы диагностики и лечения',
            'Врачи высшей категории, кандидаты наук',
            'Индивидуальные программы профилактики здоровья',
            'Современное оборудование экспертного класса',
        ],
    }
    return render(request, 'index.html', context)


def services(request):
    services_list = [
        {'name': 'Приём терапевта', 'price': '1 500 ₽'},
        {'name': 'УЗИ брюшной полости', 'price': '2 800 ₽'},
        {'name': 'ЭКГ', 'price': '1 200 ₽'},
        {'name': 'Общий анализ крови', 'price': '800 ₽'},
        {'name': 'МРТ головного мозга', 'price': '5 500 ₽'},
        {'name': 'Консультация кардиолога', 'price': '2 000 ₽'},
        {'name': 'Массаж спины (1 сеанс)', 'price': '1 800 ₽'},
        {'name': 'Стоматологический осмотр', 'price': '1 000 ₽'},
    ]
    context = {
        'active_page': 'services',
        'clinic_name': 'Медицинский центр «Новая Линия»',
        'slogan': 'Правильное направление к долголетию',
        'services': services_list,
    }
    return render(request, 'services.html', context)


def contacts(request):
    schedule = [
        {'day': 'Понедельник — Пятница', 'time': '08:00 – 20:00'},
        {'day': 'Суббота', 'time': '09:00 – 18:00'},
        {'day': 'Воскресенье', 'time': '10:00 – 16:00'},
    ]
    context = {
        'active_page': 'contacts',
        'clinic_name': 'Медицинский центр «Новая Линия»',
        'slogan': 'Правильное направление к долголетию',
        'address': 'г. Воронеж, ул. Красноармейская, д. 15',
        'phone': '+7 (473) 555-24-24',
        'email': 'info@nova-liniya-med.ru',
        'schedule': schedule,
    }
    return render(request, 'contacts.html', context)
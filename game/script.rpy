# Imagedissolve Transitions.
define circleirisout = ImageDissolve("id_circleiris.png", 1.0)
define povname = ""
define pov = DynamicCharacter(u"povname")

label start:
    $ povname = renpy.input("Меня зовут...")
    $ pol = renpy.input ("Мой пол (ж или м) :")
    scene black with fade
    scene bg1 with circleirisout
    pov "Где я?"
    pov "Что я тут делаю?"
    pov "Так темно..."
    pov "..."
    pov "Как же болит голова.."
    pov "Это чья-то шутка?"
    pov "Что со мной?"
    pov "{color=#CF4E61}{size=+10} ЭЙ!{/size}{/color}"
    pov "{color=#CF4E61}{size=+10} Есть тут кто?!{/size}{/color}"
    pov "Нет ответа.."
    pov "Нужно что-то делать."
    menu:
        "Идти вперед":
            pov "Лучше всего начать двигаться. Так я быстрее смогу выбраться."
        "Осмотреться":
            if pol=='ж':
                 pov "Я внимательно осмотрела комнату"
            else:
                 pov "Я внимательно осмотрел комнату"
            pov "Нужно найти то, что поможет мне выбраться.."
        "Кричать громче":
            pov "Что мне еще остается делать?"
    pov "Что ж..Кажется, мне нужно рассчитывать только на себя.."
    return

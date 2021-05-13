init:
    $ mods ["goodname"] = "Как хорошо ты знаешь Бесконечное Лето?"
    $ dissolveV = Dissolve(5,0)
    
label goodname:
    scene bg int_bus
    show unblink
    th "Я проснулся от бившего в глаза солнечного света." 
    show blinking
    play music music_list["raindrops"] fadein 5
    "Проморгался, и начал осматриваться. Кресла, узкий проход…"
    th "Автобус! {w}Неужели получилось!? {w}От радости чуть не заорал, но вовремя одернул себя. Мне все-таки 19 лет, уже взрослый для такого проявления эмоций."
    stop music fadeout 5
    th "И все же это правда, мне обещали день в Совенке, и похоже я его получил. {w}Ну, тогда не будем терять ни минуты!"
    
    play music music_list["forest_maiden"] fadein 5
    scene bg ext_camp_entrance_day with dissolve
    "Пулей вылетел из автобуса и помчался к воротам, и чуть не сбил выходившую оттуда Славю. {w}Ну а кто же еще, все по канону."
    show sl smile pioneer at center with dissolve_fast
    sl "Привет. Ты оттуда, да? На один день?"
    me "Да. Привет,Славя."
    "Она даже не удивилась, что я знаю ее имя. {w}Хотя, я же явно не первый турист, далеко не первый. {w}Сколько ж тут народу уже побывало до меня?"
    "Из раздумий меня вывела Славя"
    sl "Ну так что, пойдем? Остальные девочки уже ждут."
    me "А,да. Пойдем. Замечтался немного."
    "С глупой улыбкой проронил я."
    show sl smile pioneer at center with dspr
    "Славя улыбнулась."
    sl "Понимаю. Многие так стоят в первые минуты. Я уже привыкла."
    
    scene bg ext_clubs_day with dissolve 
    stop music fadeout 5
    "Прошел за Славей в ворота. {w}В далеке начали появляться здания кружков, возле которых стояли две выделяющихся рыжих фигуры."
    play music music_list["so_good_to_be_careless"] fadein 5
    show dv normal pioneer far at fleft with dissolve_fast
    show us grin sport far at fright with dspr
    th "Даа, ну и тандем, их же нельзя вместе ставить." 
    show dv normal pioneer at fleft with dissolve_fast
    show us grin sport at fright with dspr
    th "Если сколлапсируют, Совенок на воздух взлетит. {w}Только обрывки мешков из под сахара будут медленно опускаться вниз."
    show dv grin pioneer close at fleft with dissolve_fast
    show us grin sport at fright with dspr
    "Когда до огненного дуэта оставалось всего пару шагов, я заметил, что Ульянка что-то держит за спиной и хитро улыбается, а Алиса с интересом переводит взгляд с меня на подругу и обратно."
    "Ну, тут не надо быть заядлым игроком, чтобы понять, что она задумала."
    "Я, хитро прищурившись, посмотрел на девочку. {w}В эту игру могут играть двое! {w}Пусть Улька и является моим любимым героем, но так глупо я не собирался поступать."
    me "Ульяна, даже не думай! Меня этим не возьмешь."
    show us sad sport at fright with dissolve_fast
    "Девочка вмиг поникла"
    us "Ну вот. {w}Сколько уже таких как вы тут побывало, а срабатывает лишь на единицах. {w}Мог бы и подыграть девушке!"
    show dv smile pioneer close at fleft with dissolve_fast
    "Алиса прищурившись, как бы оценивая, посмотрела на меня"
    dv "А ты неплох. {w}Не красавец конечно, но и в кусты от тебя прятаться, желания нету."
    me "И тебе привет, Алиса. {w}Ты как всегда в своем репертуаре."
    th "Похоже мой комплимент пришелся ей по вкусу"
    "Может быть мы и дальше продолжили этот словесный бой, но Славя решила пресечь его на стадии зарождения."
    show sl serious pioneer close at center with dissolve_fast
    show us normal sport far at fright with dspr
    show dv normal pioneer far at fleft with dspr
    stop music fadeout 5
    sl "Так, давайте уже начнем, а то и так времени не очень много. Всего день у парня."
    play music music_list["two_glasses_of_melancholy"] fadein 5
    me "А.. Что начнем?"
    show sl smile2 pioneer close at center with dissolve_fast
    sl "Мы с недавнего времени решили организовать для новоприбывших викторину по вселенной Бесконечного Лета. {w}И ты будешь лишь третьим человеком, который попал под новый формат"
    th "Не то чтобы мне не понравилась такая идея, еще и третьим из всех буду, но я хотел просто прогуляться по лагерю, поиграть в футбол с Ульянкой, может выпить с Алисой, зайти в библиотеку позлить Женю. {w}Ну а в принцпипе теперь у меня нет выбора."
    show us grin sport at fright with dissolve_fast
    show sl smile2 pioneer far at center with dspr
    us "Даа. Посмотрим, как ты внимательно читал."
    "Ухмыльнулась Ульянка"
    show sl serious pioneer close at center with dissolve_fast
    "Славя с недовольством посмотрела на вмешавшуюся девочку, но промолчала и продолжила."
    show us normal sport far at fright with dissolve_fast
    sl "Ну вот. У нас есть три станции, три уровня сложности соответственно."
    sl "Первый, самый легкий, здесь, в кружке кибернетиков. {w}Заведуют Алиса с Ульяной. Если повезет, внутри познакомишься и с парнями, но они в последнее время что-то мастерят в старом лагере и редко здесь появляются."
    th "Оно и к лучшему. {w}Я сюда не ради пары безумных кибернетиков старался попасть"
    "Славя продолжила"
    sl "Вторая станция находится в Библиотеке. Там за главных Лена и Женя. {w}Там средний уровень сложности. Только если не уверен, лучше не испытывай судьбу."
    th "Меня подобное заявление заинтриговало"
    me "Это почему? За неправильные ответы дежурить заставят?"
    show us grin sport at fright with dissolve_fast
    show dv grin pioneer at fleft with dspr
    show sl laugh pioneer close at center with dspr
    "Славя засмеялась, а Алиса с Ульяной синхронно ухмыльнулись."
    show dv grin pioneer close at fleft with dissolve_fast
    show sl laugh pioneer at center with dspr
    dv "Нет, просто Женя очень бесится, когда отвечаешь неправильно. {w}Не дай бог у нее еще и настроение плохое. {w}Из лагеря уже не вернешься. {w}По крайней мере целым."
    th "Что ж. Очень на нее похоже. Ладно, буду начеку."
    me "Ладно, спасибо за наводку. {w}А на третьей станции кто?"
    show us normal sport at fright with dissolve_fast
    show dv grin pioneer at fleft with dspr
    show sl normal pioneer close at center with dspr
    sl "На третьей Мику с Юлей. Обитают в музклубе. Там уже серьезные вопросы. {w}Не только по сюжету и деталям, а уже и по околоигровой теме, про разработчиков, игровые файлы и прочее."
    "Славя на пару секунд замолчала, чтобы перевести дух."
    sl "Теперь в общем: на каждой станции по 15 вопросов. {w}Количество попыток неограничено, можешь пытаться снова и снова. {w}В конце девочки будут говорить тебе количество правильных ответов, но не скажут, в каких ошибки, мы посчитали такую меру неинтересной. {w}Все понял?"
    th "Вроде бы ничего сложного, и все равно моему процессору понадобилось пару десятков секунд, чтобы все уяснить до конца."
    "Наконец я сказал:"
    me "Так точно! Разрешите приступить."
    sl "Разрешаю."
    th "Так. С чего бы начать?"
    stop music fadeout 5
    jump map
    
label map:
    $ disable_all_zones() 
    $ set_zone ("clubs", "clubs")
    $ set_zone ("library", "library")
    $ set_zone ("music_club", "music_club")
    $ set_zone ("camp_entrance", "label_end")
    $ show_map()
    
label label_end:
    scene bg ext_bus with dissolve
    th "Наверное, с меня хватит."
    "Вышел за ворота, где меня уже ожидал автобус."
    sl "Уже уезжаешь?"
    "Послышался за спиной грустный голос Слави."
    "Развернулся, ожидая увидеть лишь её, но..."
    play music music_list["goodbye_home_shores"] fadein 5
    scene bg ext_camp_entrance_day with dissolve
    show dv sad pioneer far at fleft with dspr
    show un cry pioneer far at fright with dspr
    show us sad sport at left with dspr
    show mi sad pioneer at right with dspr
    show sl sad pioneer at center with dspr
    "Увидел всех девочек. {w}Они все выглядели расстроенными. {w}Даже Алиса не улыбалась, как обычно."
    "Причем что-то мне подсказывало, что это не заученный сценарий. {w}Видимо я им действительно понравился за этот день, и они действительно расстроены моим уходом."
    "Я переводил взгляд с одного кислого лица на другое. {w} Я четко видел, что каждая из них хотела что-то сказать, но слова не шли."
    me "Я понимаю вас. Мне тоже не хочется уезжать, но что поделать.{w} Мне было приятно встретиться о всеми вами вживую, я никогда не забуду нашу встречу, и думаю, что вы тоже. {w}Если повезет, я выбью еще одну поездку. {w}Будете ждать?"
    all "Конечно!" 
    stop music fadeout 5
    "Разом воскликнули все. Я даже опешил."
    me "Ну тогда договорились."
    show dv smile pioneer far at fleft with dspr
    show un smile pioneer far at fright with dspr
    show us smile sport at left with dspr
    show mi smile pioneer at right with dspr
    show sl smile pioneer at center with dspr
    "Я улыбнулся и подмигнул девчёнкам. Они сразу приободрились."
    all "Пока, Семен."
    play music music_list["reflection_on_water"]
    me "Не прощаюсь. Увидимся ещё!"
    "Я заставил себя отвернуться и зайти в автобус, не оборачиваясь."
    scene bg int_bus with dissolve2
    "Сел на то же место, на котором сидел, когда приехал. {w}В окно смотреть не стал. {w}Еще сложнее уехжать будет. {w}Надеюсь они поймут и не обидятся."
    th "Хороший был день. Один их лучших в жизни. Обязательно вернусь сюда. {w}{w}И возможно уже не на один день."
    play music music_list["afterword"] fadein 3
    
    return
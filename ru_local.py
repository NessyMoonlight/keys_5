# основной текст
TEXT_0 = ('На ваш город упала ядерная бомба. Вы всей семьёй вынуждены БЫСТРО захватить '
          'как можно больше припасов для выживания в бункере. ')
TEXT_0_1 = ('Когда вы открыли дверь бункера, то заметили, что на некоторых полках уже '
            'стоит провиант. Вы не помните откуда эти запасы, но счастливы, что нам повезло. ')
# день первый
TEXT_1 = 'Все добрались до убежища за секунду до взрыва! УРА! Вам повезло! '
TEXT_1_1 = 'Но к сожалению ваши запасы не совсем полные. Вам не хватает: '
TEXT_1_2 = ('Сначала вы все паниковали, потом ссорились, теперь все молчат. За последние часы '
            'ни слова. Ни единого. Вы уже не можете просто сидеть и изучать стены. Давайте уже займёмся чем-нибудь!')
# если включили радио, то:
RADIO = ('Cлушая музыку и переключая радиочастоты, вы наткнулись на какой-то странный сигнал. '
         'Несмотря на страшные помехи вам удалось различить голос иностранца. Возможно, стоит послушать разговор?')
RADIO_YES = 'Из-за сильных помех ничего не удалось понять. Какая досада!'
# Если тупить или шашки:
DO_NOTHING = 'Всё равно ужасно скучно. Может кто-нибудь пойдёт осматривать окрестности?'
DO_NOTHING_YES = 'Радиация в окрестностях очень высокая, вы сильно пострадали.'
# день второй
TEXT_2 = ('Вчера, играя в шарады, выяснилось, что Мэри Джейн не знает как писать '
          'слово «превысокомногорассмотрительствующий». Это вас очень расстроило, может стоит подучиться? ')
TEXT_2_YES = ('Мэри Джейн не стала терять время зря: тренировка по правописанию тут же сменилась повторением '
              'таблицы умножения и закончилась кратким курсом по ремонту самых разных предметов в убежище. '
              'Мэри Джейн решила попробовать починить старый фонарик, за что все согласились ее наградить. ')
TEXT_2_1 = ('Никто не думал, что кто-то позвонит так скоро после взрыва, и вот уже четко слышен звук звонящего '
            'телефона из телефонной будки на другой стороне улицы. Может, пойти поднять трубку? ')
TEXT_2_1_YES = ('Когда была поднята трубка, то стал слышен вздох облегчения с другой стороны. Человек представился '
                'уцелевшим из соседнего городка, и тут связь оборвалась. Радиация в окрестностях ещё слишком высокая. ')
TEXT_2_1_NO = 'Вы правильно сделали, что не пошли. Радиация сейчас очень высокая. '
# день третий
TEXT_3 = ('Наш город всё ещё сильно загрязнён радиацией. Путешествия опасны для здоровья, но '
          'нужно искать еду. Стоит ли вам пойти в экспедицию? ')
TEXT_3_YES = 'Что взять с собой? '
# день четвертый
TEXT_4 = ' вернулся с экспедиции'
TEXT_4_1 = ('Мы очень мало знаем о том, что происходит на поверхности. Хорошо бы услышать что-то или узнать, '
            'что кому-то удалось спастись. _, может сделаем что-нибудь?'
            '\n1) Использовать радиоприёмник вости!'
            '\n2) Ничего не делать')
TEXT_4_1_RADIO = ('Вам удалось поймать сигнал и прослушать экстренное сообщение от правительства. Отличные новости! '
                  'Большинство радиоактивных осадков уже развеялось! Теперь вылазки будут безопаснее!')
TEXT_4_2 = ' сегодня чувствует себя в полной боевой готовности. Отправиться в экспедицию? '
# день пятый/шестой/седьмой/восьмой/девятый
TEXT_5 = ' после тщательной подготовки к сегодняшней вылазке настроен на экспедицию. Отправиться?'
TEXT_5_YES = ('Что взять с собой?'
              '\n1) Винтовка(если есть)'
              '\n2) Топор(если есть)'
              '\n3) Руководство бойскаута'
              '\n4) Ничего(кроме противогаза, конечно)')
# день десятый
TEXT_10 = ('Мы проснулись под звуки стука в дверь. Точнее, создалось впечатление, что нашу дверь хотят выбить. '
           'Может, так оно и есть. Откроем?:')
TEXT_10_YES = ('Мы сделали это! Мы спаслись благодаря нашим храбрым военным! '
               'Это конец нашего отчаянного выживания. Ура!')
TEXT_10_NO = 'К сожалению, мы не дождались спасения. '
# рандомные события
EVENT_1 = ('Вас посетили сегодня очень необычные (немного сумасшедшие) гости. Они сказали, что ведут чрезвычайно '
           'важные поиски, в надежде найти волшебный кубок, но, к сожалению, потерялись в пустоши. '
           'Они попросили нашу карту.')
EVENT_1_YES = ('Вы правильно сделали, что дали её. Они проявили необычайную щедрость, и подарили нам топор'
               '(их волшебное боевое оружие) и немного еды')
EVENT_1_NO = 'Они были в отчаянии и разозлись, один напал, и пока мы давали ему отпор, второй успел нас обокрасть'

EVENT_2 = (' очень грязный. Если он сейчас не помоется – его стошнит. Здесь реально воняет, и ситуация '
           'вряд ли изменится в скором времени. Может сделать что-нибудь?'
           '\n1) Использовать мыло'
           '\n2) Использовать дихлофос'
           '\n3) Использовать бритву'
           '\n4) Использовать воду'
           '\n5) Использовать мыло и воду'
           '\n6) Ничего не делать')
EVENT_2_DICHLORVOS = 'Это была отчаянная попытка сымитировать дезодорант! '
EVENT_2_NO = ('Настал конец света. Кому сейчас нужен душ? Представим, что пошли в поход! '
              'Это будет… О нет, эта вонь просто ужасна! Только не блевать! Не…')
EVENT_2_YES = 'Ураа! С трудом, но смог помыться!'

EVENT_3 = ('И снова то же самое! Постоянно слышатся одни и те же странные звуки! Откуда они? Из труб? Стен? '
           'Или за дверью? Они сводят с ума! Надо разобраться, иначе завладеет паранойя.'
           '\n1) Использовать топор'
           '\n2) Поиграть в шашки'
           '\n3) Поиграть в карты'
           '\n4) Ничего не делать')
EVENT_3_AXE = 'Он отчаянно пытался найти и спугнуть источник звука, но никого не нашёл'
EVENT_3_ENTERTAINMENT = 'Мы немного повеселились, и это помогло забыть нам о… а что это было?'
EVENT_3_NO = ' сходит с ума всё больше и больше... Помогите!!!'

EVENT_4 = (' хочет сегодня что-то поделать. Что-то интересное. Иначе у него может '
           'случиться нервный срыв. А он же не хочет этого?')
EVENT_4_GUN = ('Кто-то должен проверить, в каком состоянии ружьё. Нужно всего-лишь заглянуть в дуло. '
               'Ауч! Кто-нибудь захватил аптечку, правда?')
EVENT_4_RADIO = ' поймал сигнал на бодрую музыку. У всех замечательное настроение!'
EVENT_4_SPINNER = 'Нервы немного успокоились, но в гости все еще стучится сумасшествие...)'
EVENT_4_CARD = ' неплохо скоротал время с семьёй'

EVENT_5 = 'К вам кто-то пришёл. Немного страшно, но, может это новый друг или солдат? Открыть? '
EVENT_5_YES = ('Как оказалось, это был загадочный, но приятный парень в странном костюме. '
               'Он дал немного еды. Это поможет вам выжить в ближайшие дни')

EVENT_6 = ('Вентиляция не работает, в убежище не поступает свежий воздух. '
           'Если её не починить, то скоро все задохнутся.')
EVENT_6_FLASHLIGHT = ('Когда вы посветили в вентиляцию фонариком, на вас вылетел рой злых насекомых мутантов. '
                      'Укусы болят и поднялась температура')
EVENT_6_BOOK = 'Вы починили вентиляцию'
EVENT_6_DICHLORVOS = 'В вентиляции как раз оказались насекомые-мутанты, дихлофос оказался как нельзя кстати'

EVENT_7 = (' наслаждался неповторимыми радиоактивными видами, как вдруг заметил женщину в камуфляжной форме. '
           'У неё было ружьё, но она окликнула нас дружелюбно. Сказала, что охотится на огромного паука-мутанта. '
           'У неё закончились патроны, попросила одолжить.')
EVENT_7_YES = ('Охотница пришла с прирученным пауком, когда мы его гладили, он мурлыкал. Какой милашка! '
               'В знак благодарности женщина дала нам еды')

EVENT_8 = 'Это просто безумие! Везде пауки. Вы больше не можете так жить, пора объявить им войну!'
EVENT_8_DICHLORVOS = ('Когда стоит вопрос «мы или они», любое оружие сгодится. Теперь вы похожи'
                      ' на фиолетового мутанта, зато после чистки врагов нашёл еды')
EVENT_8_NO = 'После тысячи укусов мы нашли их гнездо и задавили, но очень сильно пострадали'

EVENT_9 = 'К вам заглянул торговец. Он предложил сделку: вы ему еды, он вам неизвестный мешок. Принять?'
EVENT_9_YES = 'Вам повезло, в мешке оказалась вода и аптечка'

EVENT_10 = ('Тревога! Неподалеку бродит банда людей, одетых как пожарные. Они требуют, чтобы вы отдали '
            'все свои запасы. Утверждают, что сожгут вас, если вы этого не сделаете! ')
EVENT_10_LOCK = 'Всё обошлось, они не смогли сломать дверь'
EVENT_10_AXE = 'Это был тяжелый отпор, но вы смогли защитить семью'
EVENT_10_GUN = 'Они пытались нас поджечь, но убежали, при виде оружия'





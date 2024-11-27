import streamlit as st
import pathlib

# Set the page configuration
st.set_page_config(page_title='My Website', layout='wide')

# Sidebar navigation with emojis
page = st.sidebar.radio('Navigation',
                        ['🏠 Introduction', '🌱 Plants', '😊 Interaction', '💖 About Us'])

if page == '🏠 Introduction':
    st.title("The Poet's Quest: discover plant imagery in the Book of Song")
    st.write('')  # Adding an empty line for spacing

    # First submodule: Introduction to the Book of Songs
    st.header('Introduction 🏠')
    st.write('''
    Let's Embark on a Journey Through Poetry, Plants, and Time!

    The Book of Songs (《诗经》) is a foundational collection of poems intricately tied to social and historical development, serving as a prelude to Chinese national history. Created during the agricultural era, these poems capture:

    - Social Landscapes: Depictions of rural villages, marketplaces, and royal courts.
    - Historical Snapshots: Insights into ancestral lifestyles and living scenes.

    Through the Book of Songs, later generations can learn about the natural landscapes, flora and fauna, climate changes, land structures, production systems, ethnic distributions, transportation systems, and cultural customs from the early Western Zhou to mid-Spring and Autumn periods. The poems, carefully compiled, serve as vital historical documents for in-depth research into this era.

    In the Book of Songs, plants take center stage, weaving through nearly half of its 305 poems. With 386 plant-related references and 130 unique species, these verses reveal how deeply nature shaped ancient Chinese culture.
    ''')

    # Second submodule: Plants in the Spotlight
    st.header('Plants in the Spotlight')
    st.write('''
    🏆 The Plant Leaderboard

    🌿 桑 (Mulberry) – 40 mentions

    🌾 黍 (Millet) – 26 mentions

    🍂 葛 (Kudzu) – 21 mentions

    🍃 草 (Grass) – 19 mentions

    🌱 豆 (Bean) – 11 mentions

    🌲 松 (Pine) – 11 mentions

    🍁 柏 (Cypress) – 10 mentions

    🎋 竹 (Bamboo) – 7 mentions
    ''')

    # Image placeholders with local paths
    st.image('https://github.com/DMGT-0810/CHC5904/blob/main/digital/image/1.PNG?raw=true')
    st.image('https://github.com/DMGT-0810/CHC5904/blob/main/digital/image/2.PNG?raw=true')

    # Third submodule: Plants, Emotions, Seasons & Locations
    st.header('Plants, Emotions, Seasons & Locations')

    # 3-1
    st.subheader('Why should we care about the connection between plants and emotions?')
    st.write('''
    Most plants don’t express a single emotion—they are rich tapestries of overlapping feelings.

    In the Classic of Poetry, emotions are categorized into seven distinct types: 

    🌟 Joy

    🔥 Anger

    💭 Worry

    🤔 Contemplation

    😢 Sadness

    😨 Fear

    😲 Surprise

    By visualizing plants through this emotional lens, we can unlock a deeper understanding of their emotional significance, allowing us to connect with the poems written by our ancestors on a more personal level.
    ''')

    # Additional image placeholders for the third submodule
    st.image('https://github.com/DMGT-0810/CHC5904/blob/main/digital/image/3.png?raw=true')
    st.image('https://github.com/DMGT-0810/CHC5904/blob/main/digital/image/4.png?raw=true')

    # 3-2
    st.subheader('Seasonal Distribution of Selected Plants')
    st.write('''
        The Book of Songs beautifully ties plants to the rhythm of the seasons, revealing our ancestors' close relationship with nature. Our selected plants are predominantly associated with spring and autumn, reflecting the importance of these seasons in ancient agricultural life, however, 42% are not specified, which shows that the symbolic use of plants beyond seasonal constraints.
        ''')

    # Additional image placeholders for the third submodule
    st.image('https://github.com/DMGT-0810/CHC5904/blob/main/digital/image/5.png?raw=true')
    st.image('https://github.com/DMGT-0810/CHC5904/blob/main/digital/image/6.png?raw=true')

    # 3-3
    st.subheader('Tracing the Ancient Roots')
    st.write('''
        The Book of Songs also reveals the natural and cultural landscapes of early China, showing how the people in the past interacted with their environment. This geographical map invites you to connect with the landscapes that shaped our ancestors’ lives, offering a unique link to the past. As you explore these places, you’ll be reminded of how nature was deeply woven into daily life, agriculture, and culture.
        ''')

    # Load and display the HTML file
    file_path = pathlib.Path(__file__).parent / 'plants_in_poetry.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=600, scrolling=True)

    # Additional image placeholders for the third submodule
    # st.image('./image/5.png', caption='Third Plant Image')
    # st.image('./image/6.png', caption='Fourth Plant Image')

    categories_content = {
        "Mulberry(桑)": "期我乎桑中，要我乎上宫[《鄘风·桑中》]\n  - In Ancient Times: widespread in the Yellow River region, especially in Wei State (modern-day northern Henan and southern Hebei).\n  - Today: Mulberry trees are still common in northern China, particularly in areas like the ancient mulberry tree cluster in Xiajin, Shandong.",
        "Kudzu(葛)": "“葛生蒙楚，蔹蔓于野”[《周南·樛木》]\n  - In Ancient Times: Widespread in ancient China, especially in Chu (modern-day Hubei and Hunan).\n  - Today: Kudzu still grows in southern China, primarily used for traditional medicinal purposes and food processing.",
        "Panicum miliaceum(黍)": "“彼黍离离，彼稷之苗”[《王风·黍离》]\n  - In Ancient Times: Widely cultivated in the Yellow River region.\n  - Today: Still grown in northern China, especially in the Yellow River region, known as yellow millet, used in food processing.",
        "Various grasses(草)": "“蒹葭苍苍，白露为霜”[《秦风·蒹葭》]\n  - In Ancient Times: Various grasses, such as reeds, were common in ancient China’s wetland environments.\n  - Today: Grasses are found all over China, especially in the north, used in livestock farming, weaving, and other purposes.",
        "Beans and peas(豆)": "“菽（大豆）”[《豳风·七月》]\n  - In Ancient Times: Beans played an important role in ancient China’s agricultural society.\n  - Today: Beans are grown across China, being an important source of food and vegetables.",
        "Pine(松)": "“松柏丸丸，其下侯旬”[《小雅·斯干》]\n  - In Ancient Times: Pines were widespread in ancient China, especially in mountainous and hilly areas.\n  - Today: Pine trees are very common throughout China, particularly in the north and southwest, used for construction, furniture, and other purposes.",
        "Cypress(柏)": "“桧楫松舟”[《鄘风·柏舟》]\n  - In Ancient Times: Cypress trees were common in areas near water bodies in ancient China.\n  - Today: Cypress trees are primarily found in southern China, especially in Sichuan, Hubei, and Guizhou provinces.",
        "Bamboo(竹)": "“籊籊竹竿，以钓于淇”[《卫风·竹竿》]\n  - In Ancient Times: Bamboo was found along rivers in ancient China.\n  - Today: Bamboo grows widely in China, especially in the southern regions, used for construction, furniture, weaving, and various other purposes."
        }

        # 创建展开框显示各类别内容
    for category, content in categories_content.items():
        with st.expander(f"{category}"):
            st.write(content)

elif page == '🌱 Plants':
    st.title('Deep Dives into Plant Symbolism 🌱')

    # Sub-navigation for the "Plants" page
    plant_page = st.sidebar.radio('Plant Sections',
                                  ['🌿 Mulberry', '🍂 Kudzu', '🌼 Daisies', '🌵 Cacti', '🌴 Palms', '🌱 Succulents',
                                   '🍁 Maples', '🌲 Pines'])

    if plant_page == '🌿 Mulberry':
        st.header('Mulberry 桑')
        st.write(
            '''Mulberry is one of the earliest cultivated tree species in China, and it is also the most common plant near private houses in ancient times. The word "桑梓" has become a substitute for hometown. Mulberry trees have a wide range of uses: the leaves can be used to feed silkworms, while the fruit is sweet and edible, which can satisfy hunger and make into wine; The bark has been a famous medicine since ancient times, it can even be used to make bow, gricultural tools, utensils, chariots, etc. The line “十亩之间兮，桑者闲闲兮” shows the scene of a peasant woman happily picking mulberries, reflecting the praise of hardworking life.''')

        st.subheader('Symbolic Poems Associated with the Plant')
        poems = [
            ("《豳风·七月》",
             '''- “女执懿筐，遵彼微行，爰求柔桑。”\n- “七月流火，九月授衣。春日载阳，有鸣仓庚。女执懿筐，遵彼微行，爰求柔桑。'''),
            ("《氓》",
             '''- “氓之蚩蚩，抱布贸丝。匪来贸丝，来即我谋。”\n- “桑之未落，其叶沃若。于嗟鸠兮！无食桑葚。于嗟女兮！无与士耽。'''),
            ("《小雅·隰桑》",
             '''- “隰桑有阿，其叶有难。既见君子，其乐如何！”\n- “隰桑有阿，其叶有沃。既见君子，云何不乐！”\n- “隰桑有阿，其叶有幽。既见君子，德音孔胶。'''),
            ("《魏风·十亩之间》", '''- “十亩之间兮，桑者闲闲兮。行与子还兮。”\n- “十亩之外兮，桑者泄泄兮。行与子逝兮。'''),
            ("《鄘风·桑中》", "爰采唐矣？沬之乡矣。云谁之思？美孟姜矣。期我乎桑中，要我乎上宫，送我乎淇之上矣。"),
        ]

        # 创建多列
        cols = st.columns(5)  # 根据需要调整列数

        for col, (title, content) in zip(cols, poems):
            with col:
                # 使用更小号的标题字体
                st.markdown(f"<h4 style='text-align: center; font-size:18px;'>{title}</h4>", unsafe_allow_html=True)
                st.write(content)

        st.subheader('1. Seasonal connections ')
        tabs = st.tabs(["Statistical Results", "Agriculture", "Love"])
        contents = [
            "By screening the poems related to ‘桑 (mulberry)’ in the Book of Songs and the time elements contained in them, the results show that among the 36 occurrences of ‘桑’, 18 are in ‘spring’, 3 in ‘autumn’, and 2 include the flow of the three seasons ‘spring, summer, and autumn’, while the remaining 13 do not clearly reflect the seasonal characteristics. The results show that of the 36 occurrences of ‘桑’, 18 are in ‘spring’, 3 are in ‘autumn’, and 2 include the flow of the three seasons of ‘spring, summer, and autumn’, while the remaining 13 do not clearly reflect seasonal characteristics. From this we can see that in terms of seasons, ‘mulberry’ is more often associated with spring, followed by autumn, which may be related to the themes expressed in these verses, the two most prominent of which are agriculture and love, which are also two important themes of the Book of Songs.\n  In addition to this, related to time are the date and hour. Among these 36 occurrences, only one poem, ‘國風·豳風·七月’, mentions a specific month, from July to September, reflecting a detailed record of the months of agricultural activities in ancient societies. As for the hour, none of the verses explicitly mentions the hour, probably because these verses focus more on describing agricultural activities or emotional expressions than on specific points in time. It can be seen that compared to the relationship between ‘mulberry’ and the season, other time factors can hardly be taken into consideration.",
            "As far as farming is concerned, the two seasons of spring and autumn are crucial, one for sowing and the other for harvesting. Most of the poems related to ‘桑’ focus on spring, which is consistent with the fact that spring was the beginning of agricultural activities in ancient agricultural societies. Mulberry trees, as an important cash crop, and their young leaves were food for silkworms, so there were frequent activities of mulberry harvesting in spring. In addition, agricultural activities would also reflect seasonal changes. For example, the poem ‘國風·豳風·七月’ covers agricultural activities in all seasons of the year, from sowing in the spring to growing in the summer to harvesting in the autumn and preparing for the winter, which reflects the ancient agricultural society's reliance on and adaptation to seasonal changes. In the spring, the poem mentions ‘春日載陽’, indicating the arrival of spring, when agricultural activities, such as mulberry picking, begin. In the summer, the poem ‘七月流火’ implies the heat of summer, and ‘八月萑葦’ indicates the summer reeds. In autumn, the poem ‘八月其獲’ suggests that autumn is the season of harvesting. In winter, the poem ‘二之日鑿冰衝衝’ indicates that ice is chiselled in winter and used for preserving food.",
            "In the case of love, it is also tied to the seasons. In spring, there is an activity closely related to ‘桑’, namely ‘采桑 (picking mulberry)’. In the time of the Book of Songs, ‘采桑’ did not only represent agricultural activities, but was also a place for the expression of emotions and love between a man and a woman, as the activity of picking mulberry created an opportunity for young men and women to meet and get to know each other. The fact that most of these poems focus on spring reflects the importance of the mulberry tree in the economy and culture of ancient societies. The mulberry tree was not only a cash crop, but also a carrier of emotional and political allegories, such as a place for love between men and women and a praise for hard work."
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)

        st.subheader('2. Emotional associations')
        tabs = st.tabs(["Love and Marriage", "Diligent Living", "Homesick and Longing", "Politics"])
        contents = [
            '''《鄘风·桑中》, “期我乎桑中，要我乎上宫，送我乎淇之上矣”\nMulberry is often associated with love between men and women. In this poem, it depicts the meeting of young men and women in the Mulberry Forest, where mulberry has become a place for men and women to meet, and the tenderness and luxuriantness of the “桑树” shows the happiness and joy of the Mulberry picker and the gentleman. The tenderness and luxuriantness of the mulberry trees show the happiness and joy of the woman picking the mulberry tree when she meets with the gentleman, and expresses her joy and yearning for love.''',
            '''《卫风·氓》:“桑之未落，其叶沃若。于嗟鸠兮，无食桑葚！于嗟女兮，无与士耽！士之耽兮，犹可说也。女之耽兮，不可说也。桑之落矣，其黄而陨。自我徂尔，三岁食贫。”\nHere, the growing state of the mulberry tree is both a metaphor for the changes in sweet love, showing the woman's desire for love and her grief over the misfortune of marriage, and also a symbol of liveliness. In the first section:"The mulberry has not fallen, and its leaves are fertile", Mulberry is a metaphor for the harmony of the newlyweds with the growth and prosperity of the mulberry leaves; while the scene of the mulberry leaves withering and turning yellow to the ground is a metaphor for the misery of time and the change of lover's heart.\nHere, the growing state of the mulberry tree is both a metaphor for the changes in sweet love, showing the woman's desire for love and her grief over the misfortune of marriage, and also a symbol of liveliness. In the first section:"The mulberry has not fallen, and its leaves are fertile", Mulberry is a metaphor for the harmony of the newlyweds with the growth and prosperity of the mulberry leaves; while the scene of the mulberry leaves withering and turning yellow to the ground is a metaphor for the misery of time and the change of lover's heart.''',
            '''In some poems, mulberry is also associated with homesickness and nostalgia. For example, the verse “蜎蜎者蠋，烝在桑野” expresses the sadness of soldiers who do not return from an expedition and who miss their homes.''',
            '''“迨天之未阴雨，彻彼桑土，绸缪牖户”\nThe verse conveys, through the image of the mulberry, a political message of diligence and self-reliance, of saving for a rainy day, and of preventive preparations to protect one's homeland.'''
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)

        st.subheader('3. Human qualities')
        st.write('''
            《小雅·隰桑》

            隰桑有阿，其叶有难。既见君子，其乐如何！

            隰桑有阿，其叶有沃。既见君子，云何不乐！

            隰桑有阿，其叶有幽。既见君子，德音孔胶。
            ''')

        st.image('https://github.com/DMGT-0810/CHC5904/blob/main/digital/image/8.png?raw=true', width=300)

        tabs = st.tabs(["The purity and boldness of emotions", "Admiration and pursuit of morality for gentlemen"])
        contents = [
            "The emotional expression in the poem is pure and bold, direct and passionate, reflecting the poet's frank attitude and brave pursuit of love. In personal qualities, this frankness and courage are commendable, as they reflect one's sincerity and steadfastness",
            '''The term '君子' in the poem is not only a title for the beloved, but also implies an appreciation for their character. In ancient times, the term '君子' was often used to refer to a person of moral character. Therefore, the admiration for a "gentleman" is not only an admiration for oneself, but also a pursuit and longing for noble character'''
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)


    elif plant_page == '🍂 Kudzu':
        st.header('Kudzu 葛')
        st.write('''
                Before cotton was imported to China, Gebu was the fabric to make summer clothing. Here, the poem describes the size and strength of the kudzu vine and what it could be used for: kudzu grows long and strong, spreading all over the hills and valleys, with dense and lush leaves. Harvested and boiled, the fibers are stripped into fine threads to weave into kudzu cloth, wearing kudzu garments is truly comfortable!

                《周南·葛覃》:“葛之覃兮，施于中谷，维叶莫莫。是刈是濩，为絺为綌，服之无斁。”
                ''')

        st.subheader('Symbolic Poems Associated with the Plant')
        poems = [
            ("《王风·采葛》",
             '''- “彼采葛兮，一日不见，如三月兮。”\n- “彼采萧兮，一日不见，如三秋兮。”\n- “彼采艾兮，一日不见，如三岁兮。'''),
            ("《周南·葛覃》",
             '''- “葛之覃兮，施于中谷，维叶萋萋。”\n- “葛之覃兮，施于中谷，维叶莫莫。”\n- “是刈是濩，为絺为綌，服之无斁。'''),
            ("《唐风·葛生》",
             '''- “葛生蒙楚，蔹蔓于野。”\n- “葛生蒙棘，蔹蔓于域。”\n- “角枕粲兮，锦衾烂兮。'''),
            ("《邶风·旄丘》",
             '''  - “旄丘之葛兮，何诞之节兮。”\n  - “叔兮伯兮，何多日也？何其处也？必有与也！”\n  - “何其久也？必有以也！”'''),
            ("《王风·葛藟》", '''  - “绵绵葛藟，在河之浒。”\n  - “终远兄弟，谓他人父。”\n  - “谓他人父，亦莫我顾。”'''),
        ]

        # 创建多列
        cols = st.columns(5)  # 根据需要调整列数

        for col, (title, content) in zip(cols, poems):
            with col:
                # 使用更小号的标题字体
                st.markdown(f"<h4 style='text-align: center; font-size:18px;'>{title}</h4>", unsafe_allow_html=True)
                st.write(content)

        st.subheader('1. Seasonal connections ')
        tabs = st.tabs(["Statistical Results", "Symbolism"])
        contents = [
            '''By screening the poems related to ‘葛 (Kudze)’ in The Book of Songs and the time elements contained in them, the results show that among the 16 occurrences of ‘葛’, 5 are in ‘spring’, 4 in ‘autumn’, 3 in ‘winter’, 1 in ‘summer’, and the remaining 3 do not clearly reflect the seasonal characteristics. The results show that of the 16 occurrences of ‘葛’, 5 are in ‘spring’, 4 in ‘autumn’, 3 in ‘winter’, 1 in ‘summer’, and the remaining 3 do not clearly reflect the seasonal characteristics. Thus, in terms of seasons, ‘葛’ is more often associated with spring, followed by autumn and winter, and also with summer. This has something to do with the characteristics of ‘葛’ itself. In Shuowen Jiezi (說文解字), ‘葛’ means ‘grass’, which can grow all year round as long as the environment allows. At the same time, the fibres of ‘葛’ can be woven into cloth, which is closely related to clothes. Therefore, words related to wearing clothes appear several times in the poem, such as ‘葛屢 (grass shoes)’ three times, i.e., ‘葛屨五兩，冠緌雙止’ (國風·齊風·南山) , ‘糾糾葛屨，可以履霜’ (小雅·小旻之什·大東).\nSpecifically, spring is the most frequently mentioned season in these poems, with a total of five poems related to spring. Most of these poems depict the growth and gathering of kudzu, such as the description of the luxuriant growth of kudzu in the valley in ‘國風·周南·葛覃’ and the expression of longing for the kudzu gatherers in ‘國風·鄭風·采葛’. There are three poems related to autumn, such as ‘國風·邶風·旄丘’ and ‘國風·王風·葛藟’, in which most of the verses express thoughts of distant relatives and feelings about fate. Three poems are related to winter, such as ‘國風·齊風·南山’ and ‘小雅·小旻之什·大東’. The image of kudzu in these verses is mostly associated with cold frosts, symbolising resilience and vitality. One poem is associated with summer, namely ‘國風·魏風·葛屨’, which describes the use of kudzu shoes to tread on frost, reflecting the use of kudzu products in summer.\nApart from this, there is no explicit reference to a specific month in the verses, so the distribution of months cannot be analysed in detail. The verses also do not mention the specific hour, so the distribution of the hour cannot be analysed. However, from the content of the verses, most of them are related to daily work and life, which may coincide with the farming life of working at sunrise and resting at sunset.''',
            '''‘葛’ is not only a plant in nature in these verses, but also carries a rich symbolic meaning. It is not only a symbol of life force, but also a carrier of thoughts and emotions. The growth, collection and use of kudzu in the verses are closely related to people's daily life, reflecting the ancient people's lifestyle of living in harmony with nature. Whether it is the longing for loved ones, the feeling of fate or the desire for a better life, kudzu grass has become an important medium for the poet to express his emotions. To sum up, these verses not only depict the growth of kudzu grass in different seasons, but also reflect the ancient people's delicate observation and deep perception of natural landscape, as well as the important position of kudzu grass in ancient social life.''',
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)

        st.subheader('2. Emotional associations')
        tabs = st.tabs(["Diligent Living", "Thoughts of Longing", "Filial piety (归宁孝道)", "Mourning",
                        "Estrangement of Relatives"])
        contents = [
            '''《周南·葛覃》:“葛之覃兮，施于中谷，维叶萋萋。是刈是濩，为絺为。”\nKudzu is often associated with women's hard work and family life. This poem describes the growth of Kudzu and the labor of women, showing women harvesting kudzu vines, cooking the fibers, and weaving them into cloth, reflecting praise for hard work and women's contribution to the family.''',
            '''《王风·采葛》,:“彼采葛兮，一日不见，如三月兮！”\nThis poem expresses the deep longing for the woman who picks kudzu, and the fact that one day's absence is like three autumns, showing the intensity of the emotion and the longing for the beloved through the exaggerated sense of time. Here the word “kudzu” is used as a starting point, which actually comes from the daily life of production and is used as a starting point.''',
            '''《周南·葛覃》, “言告师氏，言告言归。薄污我私，薄澣我衣。害澣害否？归宁父母。”\n    Here, a woman is preparing to go home to visit her parents after laboring, reflecting filial piety and the importance of family.''',
            '''《唐风·葛生》, “葛生蒙楚，蔹蔓于野。予美亡此，谁与独处？”\nThrough the scene that the kudzu vine is left untended and wild to express the pain of mourning for the female lover, the worst result of planting kudzu is used as a metaphor for the sadness and misfortune of losing a lover.''',
            '''《王风·葛藟》中，“绵绵葛藟，在河之浒。终远兄弟，谓他人父。”\nHere, the poem describes a scene where the growth pattern of the kudzu vine branches out without being able to support each other. It is a metaphor for the estrangement and strangeness between members of the kinship.'''
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)

        st.subheader('3. Human qualities')
        st.write('''
                    《周南·葛覃》

                    葛之覃兮，施于中谷，维叶萋萋。黄鸟于飞，集于灌木，其鸣喈喈。

                    葛之覃兮，施于中谷，维叶莫莫。是刈是濩，为絺为綌，服之无斁。

                    言告师氏，言告言归。薄污我私，薄澣我衣。害澣害否？归宁父母。
                    ''')

        st.image('https://github.com/DMGT-0810/CHC5904/blob/main/digital/image/9.png?raw=true', width=300)

        tabs = st.tabs(["Diligence", "Filial Piety", "Sense of responsibility"])
        contents = [
            "The woman in the poem not only collects kudzu vines, but also personally weaves and makes clothes, which reflects the diligent qualities of ancient women. They not only had to participate in field work, but also be responsible for the textile work at home. This diligent spirit was an expectation and requirement of society for women at that time.",
            "The poem mentions a woman preparing to wash her clothes in order to visit her parents at home, which demonstrates her filial piety towards her parents. In the social context of that time, women still had to visit their parents' homes regularly after getting married to show respect and care for their parents.",
            "While preparing to return to her mother's home, the woman did not forget to seek advice from Shi, which shows her emphasis on family responsibilities. She not only has to take care of her own family, but also cares about the health of her parents, and this sense of responsibility is an important component of her personal qualities."
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)


    elif plant_page == '🌼 Daisies':
        st.header('Daisies')
        st.write("Coming Soon---")
    elif plant_page == '🌵 Cacti':
        st.header('Cacti')
        st.write("Coming Soon---")
    elif plant_page == '🌴 Palms':
        st.header('Palms')
        st.write("Coming Soon---")
    elif plant_page == '🌱 Succulents':
        st.header('Succulents')
        st.write("Coming Soon---")
    elif plant_page == '🍁 Maples':
        st.header('Maples')
        st.write("Coming Soon---")
    elif plant_page == '🌲 Pines':
        st.header('Pines')
        st.write("Coming Soon---")

elif page == '😊 Interaction':
    st.title('Interaction 😊')
    #st.write('Here you can find information about our team and our history.')

    st.subheader('1.Quest')
    st.write('Welcome to our journey to explore the world of poetry!')
    # 定义要嵌入的网页链接
    url = "https://view.genially.com/673c89a7fffb4fdecd627489/interactive-image-a-poets-quest"
    # 使用HTML的iframe元素嵌入网页
    iframe_html = f"""
        <iframe src="{url}" width="100%" height="400" frameborder="0">
            <p>您的浏览器不支持iframe标签。</p>
        </iframe>
        """
    # 使用st.markdown展示iframe，并设置unsafe_allow_html=True允许HTML代码渲染
    st.markdown(iframe_html, unsafe_allow_html=True)
    # 添加一个链接，点击可以直接跳转到网页
    st.markdown(f"[Click here.]({url})", unsafe_allow_html=True)

    st.subheader('2.Mini-Programme')
    st.image('https://github.com/DMGT-0810/CHC5904/blob/main/digital/image/10.png?raw=true', width=300)

elif page == '💖 About Us':
    st.title('About Us')
    st.subheader('Team Members ✨')
    st.write('''1.Humanities Analysis:
    
    XIAO Qifang (24003563G@connect.polyu.hk)
    
    DENG Junxuan(24043858G@connect.polyu.hk)
    
    ZENG Jingwen(24073054G@connect.polyu.hk)
    
    ZHANG Fengyue (24100774G@connect.polyu.hk)
    
    TIAN Yuan (24073183G@connect.polyu.hk)
            ''')
    st.write('''2.Technology Support:
    
    SU Zihan (24062583G@connect.polyu.hk)
    
    CHEN Youyang (24062058G@connect.polyu.hk)

            ''')

    st.subheader('Methodology 🔍')
    st.write('''1.Why we are interested in this research topic on plants, seasons, emotions and locations?

    The Book of Songs and its plant descriptions carry rich cultural connotations, representing the essence of traditional culturje. The botanical descriptions, in thwe Book of Songs contawin abundant cultural information. As carriers of emotion, plants embody the ancient people's sentiments and attitudes toward life. Meanwhile, the geographical features and seasonal climate reflected by these plants are alyso crucial components of their imagery. Analyzing the plants in thme Book of Songs through information visualizationg helps us understand its cultural messages and pass on both the Book of Songs and Chinese. 
                ''')
    st.write('''2.How we selected the plants?
        
    We used a text analysis tool to count the eight most frequently mentioned plants, which are: mulberry (40 times), millet (26 times), kudzu (21 times), grass (19 times), beans (11 times), pine (11 times), cypress (10 times), and bamboo (7 times).

               ''')
    st.write('''3.How do we present the content?
    
    We present the georaphical locations of plants through GIS, conduct close reading on seasons, emotional connotations, and human qualities, and we also created an interactive mini-game and a photo-poetry recognition mini-programme to provide users with a diverse experience.
                   ''')

    st.subheader('Workflow 🎨')
    # 滑块
    w = [
        "Occurrences of plants: \nThe Book of Songs contains 305 poems, among which 153 mention plants. Based on this data, we wrote a python program to create a pie chart for this overall distribution.",
        "Frequency of top mentioned plants: \nUsing text analysis tools, we identified the eight most frequently mentioned plants in the Book of Songs, which we then selected as our target species for further study. Subsequently, we created a bar chart to visualize this data.",
        "Emotional themes in selected plants: \nWe analyzed the emotional themes expressed through plants in the Book of Songs and categorized them into major categories and subcategories. This hierarchical structure helps understand the rich emotional palette of the poetry collection.",
        '''Emotional theme network: \nWe created a network visualization to show the relationships between plants and their associated emotional themes in the Book of Songs. The network consists of main emotional categories (like "Love & Longing", "Diligent Life", "National Spirit") connected to specific plant-emotion pairs.''',
        "Seasonal distribution: \nThe seasonal distribution of plants in the Book of Songs was analyzed in two complementary ways - a pie chart showing the overall distribution and a stacked bar chart showing the distribution by plant species. ",
        "Geographical location: \nTo perform GIS, I combined data with conclusions provided by AI to preliminarily determine the geographic locations (latitude and longitude) of the plants.",
    ]
    # 创建一个滑块
    index = st.slider(" ", 1, len(w) , format="Step %d")
    st.write(w[index - 1])

    st.subheader('Reference 📖')
    # 定义链接
    url1 = "http://eprints.utar.edu.my/3850/1/fyp_CH_2019_TJM_%2D_1606961.pdf"
    url2 = "https://kns.cnki.net/KCMS/detail/detail.aspx?dbname=CMFD2012&filename=1011254556.nh"
    #showcase
    st.write(f'[1.《诗经》中“桑”的意向]({url1})')
    st.write(f'[2.《诗经》中的植物及其文化解读]({url2})')

    st.subheader('Original Text 💎')
    url3 = "https://ctext.org/book-of-poetry"
    # 使用HTML的iframe元素嵌入网页
    iframe_html = f"""
            <iframe src="{url3}" width="100%" height="400" frameborder="0">
                <p>您的浏览器不支持iframe标签。</p>
            </iframe>
            """
    # 使用st.markdown展示iframe，并设置unsafe_allow_html=True允许HTML代码渲染
    st.markdown(iframe_html, unsafe_allow_html=True)
    # 添加一个链接，点击可以直接跳转到网页
    st.markdown(f"[Click here.]({url3})", unsafe_allow_html=True)





#  В магазинах имеются следующие товары. Магнит - молоко, соль, сахар, печенье, сыр.Пятерочка - мясо, молоко, сыр. Перекресток - молоко, творог, сыр, сахар, печенье. Лента- печенье, молоко, сыр, сметана.Определить:в каких магазинах нельзя приобрести сметану.какие товары из магазина Магнит отсутствуют в магазине Перекресток.какие товары из магазина Лента отсутствуют в магазине Магнит.
# Создаем множества товаров в каждом магазине
magazin_magnit = {'молоко', 'соль', 'сахар', 'печенье', 'сыр'}
magazin_pyaterochka = {'мясо', 'молоко', 'сыр'}
magazin_perekrestok = {'молоко', 'творог', 'сыр', 'сахар', 'печенье'}
magazin_lenta = {'печенье', 'молоко', 'сыр', 'сметана'}

# Определяем в каких магазинах нельзя приобрести сметану
magaziny_bez_smetany = []
for magazin, tovary in {'Магнит': magazin_magnit, 'Пятерочка': magazin_pyaterochka, 'Перекресток': magazin_perekrestok, 'Лента': magazin_lenta}.items():
    if 'сметана' not in tovary:
        magaziny_bez_smetany.append(magazin)
print('В магазинах', ', '.join(magaziny_bez_smetany), 'нельзя приобрести сметану.')

# Определяем какие товары из магазина Магнит отсутствуют в магазине Перекресток
tovary_otsutstvuyushie_v_perekrestok = magazin_magnit.difference(magazin_perekrestok)
print('В магазине Перекресток отсутствуют товары из магазина Магнит:', ', '.join(tovary_otsutstvuyushie_v_perekrestok))

# Определяем какие товары из магазина Лента отсутствуют в магазине Магнит
tovary_otsutstvuyushie_v_magnit = magazin_lenta.difference(magazin_magnit)
print('В магазине Магнит отсутствуют товары из магазина Лента:', ', '.join(tovary_otsutstvuyushie_v_magnit))

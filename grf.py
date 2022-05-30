import biblia

sas = biblia.graf_gen()


#генерируем графы


biblia.add_toch(sas, 1)
biblia.add_toch(sas, 2)
biblia.add_toch(sas, 3)
biblia.add_toch(sas, 4)
biblia.add_toch(sas, 5)
biblia.add_toch(sas, 6)
biblia.add_toch(sas, 7)
biblia.add_dg(sas, 1, 2, 12)
biblia.add_dg(sas, 1, 3, 3)
biblia.add_dg(sas, 1, 4, 4)
biblia.add_dg(sas, 2, 3, 5)
biblia.add_dg(sas, 3, 4, 11)
biblia.add_dg(sas, 3, 5, 7)
biblia.add_dg(sas, 3, 6, 6)
biblia.add_dg(sas, 4, 5, 12)
biblia.add_dg(sas, 5, 6, 13)
biblia.add_dg(sas, 5, 7, 14)
biblia.add_dg(sas, 6, 7, 7)
biblia.al_out(sas)
biblia.gen_ostov(sas, 1)
print()

biblia.gen_ostov(sas, 3)
print()

biblia.gen_ostov(sas, 7)
print()

print(biblia.short_way(sas, 1, 5))


print(biblia.short_way(sas, 1, 7))


print(biblia.short_way(sas, 1, 2))


biblia.add_toch(sas, 12)
biblia.add_toch(sas, 11)
biblia.add_dg(sas,12,11)
biblia.al_out(sas)
print(biblia.filde_show(sas))



print('3->', biblia.whiche_fild(sas, 3))
a = 2
b = 11
if biblia.own_fild(sas, a, b):
    print(a, ' ', b, 'В одной области.')
else:
    print(a, ' ', b, 'Не в одной области.')
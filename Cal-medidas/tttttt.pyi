def conversions():
    get_unit_1 = comb_from.get()
    get_unit_2 = comb_to.get()

    num_conver = float(en_inf_1.get())

    print(get_unit_1, get_unit_2, num_conver)
    if l_unit.cget("text").lower() in unit_all.keys():
        units_dict = unit_all[l_unit.cget("text").lower()]
        from_unit_value = next(item for item in units_dict if get_unit_1 in item)
        to_unit_value = next(item for item in units_dict if get_unit_2 in item)

        # Obtendo os valores de conversão
        from_value = list(from_unit_value.values())[0]
        to_value = list(to_unit_value.values())[0]

        # Realizando a conversão
        converted_value = (num_conver * from_value) / to_value

        # Exibindo o resultado na label de saída
        en_inf.config(text=f"{converted_value:.2f} {get_unit_2}")
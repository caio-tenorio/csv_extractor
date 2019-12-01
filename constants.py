
verbas_indenizatorias_header_list = ["aluguel", "condominio", "energia", "agua", "iptu_tpei", "internet_telefone", 'trasporte_hospedagens',
    "locacao_automovel", "pecas_veiculos", "servicos", "material_expediente", "locacao_equipamentos", "assinaturas_jornais", "servicos_graficos",
    "total_apresentado", "glosa", "pago_no_mes", "media_mensal", "media_mensal_acumulada"]


def get_verbas_indenizatorias_mapping():
    mapping = dict()
    count = 4
    for atributo in verbas_indenizatorias_header_list:
        mapping[count] = atributo
        count += 1
    return mapping


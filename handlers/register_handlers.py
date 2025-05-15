def register_handlers(dp):
    from handlers.money_block import register_money_block_handlers
    from handlers.zone_1.start import register_zone_1_handlers
    from handlers.zone_2.start import register_zone_2_handlers
    from handlers.zone_3.start import register_zone_3_handlers
    from handlers.zone_4.start import register_zone_4_handlers
    from handlers.zone_5.start import register_zone_5_handlers
    from handlers.zone_6.start import register_zone_6_handlers
    from handlers.zone_7.start import register_zone_7_handlers
    from handlers.zone_8.start import register_zone_8_handlers

    # Зона 1 — Деньги и самооценка
    register_money_block_handlers(dp)

    # Остальные зоны:
    register_zone_1_handlers(dp)
    register_zone_2_handlers(dp)
    register_zone_3_handlers(dp)
    register_zone_4_handlers(dp)
    register_zone_5_handlers(dp)
    register_zone_6_handlers(dp)
    register_zone_7_handlers(dp)
    register_zone_8_handlers(dp)#Регистрирует все зоны с 1 по 8

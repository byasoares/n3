CREATE TABLE `tabela_usuario` (
  `user_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_nome` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_sobrenome` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_matricula` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
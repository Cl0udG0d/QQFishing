CREATE DATABASE IF NOT EXISTS QQFishing default charset utf8 COLLATE utf8_general_ci;

use QQFishing;



CREATE TABLE `user` (
`id` int(11) unsigned NOT NULL AUTO_INCREMENT,
`email` varchar(20) NOT NULL,
`username` varchar(50) NOT NULL,
`pw_hash` varchar(128) NOT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `user` (`id`, `email`, `username`, `pw_hash`)
VALUES
(1,'springbird@qq.com','springbird','pbkdf2:sha256:150000$XNEKW4J4$726b6b5f7d07c3e7f4280634b547b90c64055018f31290c05857aade0b983057');

CREATE TABLE `target` (
`id` int(11) unsigned NOT NULL AUTO_INCREMENT,
`username` varchar(50) NOT NULL,
`password` varchar(100) NOT NULL,
`logindate` datetime,

PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



create schema daroca;

create table daroca.produtos(
    id int identity (1, 1) not null,
    nome varchar(30) null,
	imagem varchar (500) null,
    valor real null,
	descricao varchar(50) null,
	categoria int primary key clustered (id ASC)
);

insert into daroca.produtos 
(nome, imagem, valor, descricao, categoria) 
values
('Morango', 'https://conteudo.imguol.com.br/c/entretenimento/78/2018/02/28/morango-1519823853148_v2_4x3.jpg', 9.00, '', 1),
('Pêssego', 'https://diariodonordeste.verdesmares.com.br/image/contentid/policy:1.3193945:1645120337/image/p%C3%AAssego%203.jpg?f=16x9&$p$f=a08fbe8', 9.00, '', 1),
('Pêra', 'https://www.coisasdaroca.com/wp-content/uploads/2021/04/pera.jpg', 9.00, '', 1),
('Maçã verde', 'https://organicosinbox.com.br/wp-content/uploads/2020/12/maca-verde-organica.jpg', 9.00, '', 1),
('Banana', 'https://nutritotal.com.br/publico-geral/wp-content/uploads/2019/12/shutterstock_375477457.jpg', 9.00, '', 1),
('Uva', 'https://www.oceandrop.com.br/media/pdp-seo/blog-ocean/beneficios_da_uva.jpg', 9.00, '', 1),
('Kiwi', 'https://hospitalsantatereza.com.br/wp-content/uploads/2021/06/Design-sem-nome-6.jpg', 9.00, '', 1),
('Framboesa', 'https://doutorjairo.com.br/media/_versions/istock-_framboesa_fruta_widelg.jpg', 9.00, '', 1),
('Caju', 'https://www.dicasdemulher.com.br/wp-content/uploads/2018/05/caju-2--730x449.jpg', 9.00, '', 1),
('Laranja', 'https://diariodonordeste.verdesmares.com.br/image/contentid/policy:1.3171280:1639591513/Laranjas.jpg?f=default&$p$f=e4514e8', 9.00, '', 1),
('Limão', 'https://static1.minhavida.com.br/articles/cc/50/55/8f/limao-orig-1.jpg', 9.00, '', 1),
('Mamão', 'https://static.tuasaude.com/media/article/fk/vz/beneficios-do-mamao-papaia_33156_l.jpg', 9.00, '', 1),
('Melão', 'https://dm0fehhuxv6f6.cloudfront.net/wp-content/uploads/2021/06/07140448/melao.jpg', 9.00, '', 1),
('Melancia', 'https://jornalibia.com.br/wp-content/uploads/2017/02/melancia-beneficios.jpg', 9.00, '', 1),
('Abacaxi', 'https://p2.trrsf.com/image/fget/cf/774/0/images.terra.com/2021/11/16/1695654809-abacaxi-1.jpg', 9.00, '', 1),
('Abacate', 'https://minhasaude.proteste.org.br/wp-content/uploads/2022/10/abacates.jpg.webp', 9.00, '', 1);

-- Inserção dos valores dos legumes na tabela daroca.produtos
insert into daroca.produtos 
(nome, imagem, valor, descricao, categoria) 
values
('Cenoura', 'https://www.infoescola.com/wp-content/uploads/2010/08/cenoura_250834906.jpg', 9.00, '', 2),
('Abóbora', 'https://organicosinbox.com.br/wp-content/uploads/2020/11/abobora-organica.jpg', 9.00, '', 2),
('Batata', 'https://organicosinbox.com.br/wp-content/uploads/2020/11/batata-inglesa-organica.jpg', 9.00, '', 2),
('Rabanete', 'https://spdm.org.br/wp-content/uploads/2017/06/k2_items_src_4f424d273207076187fcaaac234fe4fd.jpg', 9.00, '', 2),
('Berijela', 'https://www.sodexobeneficios.com.br/data/files/E7/40/47/CA/559588102440F4887618F9C2/xbeneficios-da-berinjela.jpg.pagespeed.ic.0fuH2cn3ip.webp', 9.00, '', 2),
('Brócolis', 'https://s1.static.brasilescola.uol.com.br/be/conteudo/images/o-brocolis-pode-ser-preparado-no-vapor-5b4f5289ec913.jpg', 9.00, '', 2),
('Cebola', 'https://conteudo.imguol.com.br/c/entretenimento/61/2017/10/25/cebola-1508951722238_v2_1920x1275.jpg', 9.00, '', 2),
('Milho', 'https://www.massimaalimentacao.com.br/wp-content/uploads/2013/06/milho-verde-festa-junina.jpg', 9.00, '', 2),
('Alho-poró', 'https://static.tuasaude.com/media/article/nu/ys/alho-poro_62486_l.jpg', 9.00, '', 2),
('Ervilha', 'https://static.itdg.com.br/images/auto-auto/b2c52382f3b05766792fb9d4f2326e93/shutterstock-287797673.jpg', 9.00, '', 2),
('Tomate', 'https://tomatesmallmann.com.br/wp-content/uploads/2022/03/MALL_img_BLOG_28mar2022.jpg', 9.00, '', 2),
('Vagem', 'https://conteudo.imguol.com.br/c/entretenimento/47/2021/03/05/vagem-1614968081236_v2_1254x836.jpg', 9.00, '', 2),
('Chuchu', 'https://imagens.ne10.uol.com.br/veiculos/_midias/jpg/2024/04/17/806x444/1_istock_1401986077-26927858.jpg?20240430181231', 9.00, '', 2),
('Quiabo', 'https://static.tuasaude.com/media/article/ds/sw/beneficios-do-quiabo_22346_l.jpg', 9.00, '', 2),
('Pimentão Vermelho', 'https://www.soflor.com.br/wp-content/uploads/2014/08/pimentao-vermelho-50-sementes-4377-e1496690749652.jpg', 9.00, '', 2),
('Beterraba', 'https://static.tuasaude.com/media/article/ub/dv/beneficios-da-beterraba_33550_l.jpg', 9.00, '', 2);

insert into daroca.produtos 
(nome, imagem, valor, descricao, categoria) 
values
('Alface', 'https://organicosinbox.com.br/wp-content/uploads/2020/11/alface-crespa-organica.jpg', 9.00, '', 3),
('Espinafre', 'https://static.tuasaude.com/media/article/ad/da/beneficios-do-espinafre_18895_l.jpg', 9.00, '', 3),
('Acelga', 'https://static.tuasaude.com/media/article/fz/wf/acelga_3636_l.jpg', 9.00, '', 3),
('Escarola', 'https://conteudo.imguol.com.br/c/entretenimento/5c/2021/03/18/escarola-1616100826742_v2_450x450.jpg', 9.00, '', 3),
('Berijela', 'https://www.sodexobeneficios.com.br/data/files/E7/40/47/CA/559588102440F4887618F9C2/xbeneficios-da-berinjela.jpg.pagespeed.ic.0fuH2cn3ip.webp', 9.00, '', 3),
('Manjericão', 'https://nutritotal.com.br/publico-geral/wp-content/uploads/2021/11/Manjericao_beneficios_Nutritotal_Para_Todos_novosite.jpg', 9.00, '', 3),
('Couve-manteiga', 'https://conteudo.imguol.com.br/c/entretenimento/01/2020/07/17/couve-1595025720411_v2_4x3.jpg', 9.00, '', 3),
('Coentro', 'https://conteudo.imguol.com.br/c/entretenimento/53/2022/04/27/coentro-1651090322896_v2_450x450.jpg', 9.00, '', 3),
('Alho-poró', 'https://static.tuasaude.com/media/article/nu/ys/alho-poro_62486_l.jpg', 9.00, '', 3),
('Rúcula', 'https://tribunadejundiai.com.br/wp-content/uploads/2022/06/Descubra-quais-sao-os-beneficios-da-rucula-para-sua-saude-1200x900.jpg', 9.00, '', 3),
('Salsa', 'https://static.tuasaude.com/media/article/ui/or/salsa_56772_l.jpg', 9.00, '', 3),
('Repolho-roxo', 'https://quimicaempratica.com/wp-content/uploads/2017/07/benefc3adcios-do-repolho-roxo-aliado-da-imunidade.jpg?w=809', 9.00, '', 3),
('Alcachofra', 'https://cptstatic.s3.amazonaws.com/imagens/enviadas/materias/materia9699/horta-como-plantar-alcachofra-cynara-cardunculus-subsp-scolymus-cpt.jpg', 9.00, '', 3),
('Agrião', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTO-zu3qCmd226yZirPIVzo-X7qsD5wvko2cbS_Ms12qQ&s', 9.00, '', 3),
('Chicória', 'https://static.tuasaude.com/media/article/ez/ms/chicoria_32903_l.jpg', 9.00, '', 3),
('Aipo', 'https://i0.wp.com/revistajardins.pt/wp-content/uploads/2019/02/GettyImages-457740075.jpg?fit=1000%2C666&ssl=1', 9.00, '', 3);

select * from daroca.produtos order by categoria ASC

update daroca.produtos
set descricao = lower(nome);


--create table daroca.clientes(
--    usuario varchar(15) primary key,
--    nome varchar(60) not null,
--    senha varchar(20) not null,
--    nascimento date not null,
--    email varchar(60) not null unique,
--    frequencia varchar(20) not null,
--);

--insert into DaRoca_clientes
--(usuario, nome, senha, nascimento, email, frequencia)
--values
--('rafasinha', 'Rafaelly', 'fa13ra', '2008-10-06', 'rafinha13@gmail.com', 'semanal')
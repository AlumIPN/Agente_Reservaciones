import sqlite3

# Crear base de datos SQLite
conn = sqlite3.connect('Turismo_Agente.db')
cursor = conn.cursor()

# Crear ambas tablas en un solo execute
cursor.executescript('''
CREATE TABLE ciudades (
  id INTEGER PRIMARY KEY,
  nombre TEXT,
  estado TEXT DEFAULT 'Oaxaca'
);

CREATE TABLE agencias_autos (
  id INTEGER PRIMARY KEY,
  nombre TEXT,
  direccion TEXT,
  ciudad_id INTEGER,
  telefono TEXT,
  FOREIGN KEY (ciudad_id) REFERENCES ciudades(id)
);

CREATE TABLE atracciones (
  id INTEGER PRIMARY KEY,
  nombre TEXT,
  descripcion TEXT,
  ciudad_id INTEGER,
  tipo TEXT,
  FOREIGN KEY (ciudad_id) REFERENCES ciudades(id)
);

CREATE TABLE hoteles (
  id INTEGER PRIMARY KEY,
  nombre TEXT,
  direccion TEXT,
  ciudad_id INTEGER,
  estrellas INTEGER,
  servicios TEXT,
  FOREIGN KEY (ciudad_id) REFERENCES ciudades(id)
);

CREATE TABLE usuarios (
  id INTEGER PRIMARY KEY,
  nombre TEXT,
  correo TEXT,
  Apellidos TEXT,
  Edad INTEGER,
  Telefono TEXT
);

CREATE TABLE resenas (
  id INTEGER PRIMARY KEY,
  usuario_id INTEGER,
  entidad_tipo TEXT CHECK(entidad_tipo IN ('hotel','restaurante','agencia','atraccion','transporte')),
  entidad_id INTEGER,
  fecha_resena DATETIME DEFAULT CURRENT_TIMESTAMP,
  comentario TEXT,
  calificacion INTEGER,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE respuestas_usuarios (
  id INTEGER PRIMARY KEY,
  usuario_id INTEGER,
  fecha_respuesta DATETIME DEFAULT CURRENT_TIMESTAMP,
  tour TEXT,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE restaurantes (
  id INTEGER PRIMARY KEY,
  nombre TEXT,
  tipo_comida TEXT,
  direccion TEXT,
  ciudad_id INTEGER,
  descripcion TEXT,
  FOREIGN KEY (ciudad_id) REFERENCES ciudades(id)
);

CREATE TABLE transportes (
  id INTEGER PRIMARY KEY,
  tipo TEXT,
  empresa TEXT,
  ciudad_id INTEGER,
  contacto TEXT,
  FOREIGN KEY (ciudad_id) REFERENCES ciudades(id)
);
''')


cursor.executemany('''
INSERT INTO ciudades (id, nombre, estado) VALUES (?, ?, ?);
''', [
  (1, 'Oaxaca de Juárez', 'Oaxaca'),
  (2, 'Mazunte', 'Oaxaca'),
  (3, 'Puerto Escondido', 'Oaxaca'),
  (4, 'Huatulco', 'Oaxaca'),
  (5, 'San José del Pacífico', 'Oaxaca'),
  (6, 'Mitla', 'Oaxaca'),
  (7, 'Teotitlán del Valle', 'Oaxaca'),
  (8, 'Santa María del Tule', 'Oaxaca'),
  (9, 'Juchitán de Zaragoza', 'Oaxaca'),
  (10, 'Huajuapan de León', 'Oaxaca')
])

cursor.executemany('''
INSERT INTO agencias_autos (id, nombre, direccion, ciudad_id, telefono) VALUES (?, ?, ?, ?, ?)
''', [

(1, 'RentaCar Oaxaca', 'Av. Universidad 1200', 1, '9511234567'),
(2, 'Renta carro Mazunte', 'Av. mar 340', 2, '9451267643'),
(3, 'Herzt', 'Av. Cangrejo 30', 3, '9780067613'),
(4, 'Herzt', 'Av. Aeropuerto 10', 4, '9581208756'),
(5, 'Oaxaca Rent a Car', 'Calle de Manuel Doblado 101, Centro', 1, '9512345678'),
(6, 'Express Auto Rental', 'Calzada Madero 500, Col. Reforma', 1, '9518765432'),
(7, 'Puerto Rent a Car', 'Av. Oaxaca 123, Centro', 3, '9545821122'),
(8, 'Zicatela Auto Rental', 'Calle del Morro 45, Zicatela', 3, '9541234567'),
(9, 'EcoCar Puerto', 'Camino a Punta Zicatela 8', 3, '9548765432'),
(13, 'Oaxaca Auto Rent', 'Calzada Madero 456, Centro', 1, '9517654321'),
(14, 'Zapoteco Rides', 'Boulevard Eduardo Vasconcelos 89', 1, '9516789012'),
(15, 'Mazunte Rent-a-Car', 'Calle Rinconcito s/n, Mazunte', 2, '9581234567'),
(16, 'Costa Móvil', 'Av. Principal 45, Mazunte', 2, '9587654321'),
(17, 'Bahías Rent-a-Car', 'Boulevard Chahué 200, Sector H', 4, '9581234567'),
(18, 'Huatulco Auto Service', 'Av. Benito Juárez 89, La Crucecita', 4, '9587654321'),
(19, 'Pacífico Rides', 'Carretera Costera 175, Santa Cruz', 4, '9586789012'),
(20, 'Pacífico Renta 4x4', 'Carretera 175 km 135, San José del Pacífico', 5, '9512345678'),
(21, 'EcoRides Sierra Sur', 'Calle Principal s/n, San José del Pacífico', 5, '9518765432'),
(22, 'Montaña Móvil', 'Camino al Mirador 22, San José del Pacífico', 5, '9513456789'),
(23, 'Mitla Rent-a-Car', 'Av. Juárez 101, Mitla', 6, '9514567890'),
(24, 'Valle Auto Tours', 'Calle Hidalgo 22, Mitla', 6, '9516781234'),
(25, 'Zapoteco Drive', 'Calle Reforma 18, Mitla', 6, '9517894561'),
(26, 'Teotitlán Auto Renta', 'Calle del Telar 12, Teotitlán del Valle', 7, '9512341122'),
(27, 'Rutas Zapotecas', 'Av. Principal 45, Teotitlán del Valle', 7, '9518763344'),
(28, 'EcoDrive Teotitlán', 'Camino al Mirador 9, Teotitlán del Valle', 7, '9517892211'),
(29, 'Tule Rent-a-Car', 'Av. Juárez 12, Santa María del Tule', 8, '9513214567'),
(30, 'Árbol Móvil', 'Calle Hidalgo 22, Santa María del Tule', 8, '9516547890'),
(31, 'EcoTule Rides', 'Camino al Árbol 5, Santa María del Tule', 8, '9519873210'),
(32, 'Istmo Auto Rent', 'Av. Efraín R. Gómez 101, Juchitán', 9, '9712345678'),
(33, 'Zapoteco Drive', 'Calle 5 de Septiembre 33, Juchitán', 9, '9718765432'),
(34, 'Juchitán Rides', 'Boulevard Lázaro Cárdenas 88, Juchitán', 9, '9713456789'),
(35, 'Mixteca Rent-a-Car', 'Av. 5 de Febrero 120, Huajuapan', 10, '9531234567'),
(36, 'Sierra Auto Tours', 'Calle Morelos 45, Huajuapan', 10, '9537654321'),
(37, 'Huajuapan Móvil', 'Boulevard Valerio Trujano 89, Huajuapan', 10, '9539876543')
])

cursor.executemany('''
INSERT INTO atracciones (id, nombre, descripcion, ciudad_id, tipo) VALUES (?, ?, ?, ?, ?);
''', [
  (1, 'Zona Arqueológica de Monte Albán', 'Sitio arqueológico zapoteca', 1, 'histórica'),
(2, 'Centro Mexicano de la Tortuga', 'Sitio de conservación', 2, 'Reserva'),
(3, 'Playa Zicatela', 'Destino de surf internacional', 3, 'Playa'),
(4, 'Playa Carrizalillo', 'Destino de surf internacional', 3, 'Playa'),
(5, 'Playa La Entrega', 'Playa vírgen', 4, 'Playa'),
(6, 'Museo de las Culturas de Oaxaca', 'Museo dentro del ex convento de Santo Domingo', 1, 'cultural'),
(7, 'Hierve el Agua', 'Formaciones rocosas y pozas naturales en la sierra', 1, 'natural'),
(8, 'Laguna de Manialtepec', 'Laguna bioluminiscente ideal para paseos nocturnos en kayak', 3, 'ecoturismo'),
(9, 'Punta Cometa', 'Mirador natural con vistas espectaculares al atardecer', 3, 'paisajística'),
(12, 'Jardín Etnobotánico de Oaxaca', 'Espacio dedicado a la flora oaxaqueña con recorridos guiados y enfoque ecológico', 1, 'natural'),
(13, 'Mercado Benito Juárez', 'Centro tradicional de comercio con artesanías, comida típica y productos locales', 1, 'cultural'),
(14, 'Andador Turístico Macedonio Alcalá', 'Calle peatonal con arquitectura colonial, galerías, cafés y tiendas artesanales', 1, 'urbana'),
(15, 'Parque El Llano', 'Espacio verde en el centro de la ciudad ideal para paseos, eventos y descanso', 1, 'natural'),
(16, 'Punta Cometa', 'Mirador natural con vistas espectaculares al océano Pacífico, ideal para caminatas y atardeceres', 2, 'natural'),
(17, 'Playa Mazunte', 'Playa tranquila de arena dorada, perfecta para nadar, relajarse y practicar yoga', 2, 'recreativa'),
(18, 'Bahía de Santa Cruz', 'Playa principal con muelle turístico, ideal para nadar y tomar tours en lancha', 4, 'recreativa'),
(19, 'Parque Nacional Huatulco', 'Área protegida con selva, ríos y playas vírgenes, perfecta para ecoturismo', 4, 'natural'),
(20, 'Mirador de Tangolunda', 'Punto panorámico con vistas espectaculares al mar y a los resorts de la bahía', 4, 'escénica'),
(21, 'Mirador de San José', 'Punto panorámico con vistas espectaculares de la Sierra Sur', 5, 'escénica'),
(22, 'Temazcal Holístico', 'Experiencia tradicional de purificación corporal y espiritual', 5, 'cultural'),
(23, 'Ruta de los Hongos', 'Sendero guiado para conocer la biodiversidad fúngica de la región', 5, 'ecológica'),
(24, 'Zona Arqueológica de Mitla', 'Sitio zapoteca con grecas únicas y arquitectura funeraria', 6, 'histórica'),
(25, 'Museo Frissell', 'Colección de piezas arqueológicas y arte popular oaxaqueño', 6, 'cultural'),
(26, 'Mercado de Mitla', 'Espacio tradicional con textiles, mezcal y gastronomía local', 6, 'cultural'),
(27, 'Talleres de Telar Zapoteco', 'Espacios familiares donde se elaboran tapetes con tintes naturales', 7, 'cultural'),
(28, 'Iglesia Prehispánica de la Preciosa Sangre', 'Templo colonial construido sobre una plataforma zapoteca', 7, 'histórica'),
(29, 'Presa Piedra Azul', 'Área natural ideal para caminatas y observación de aves', 7, 'natural'),
(30, 'Árbol del Tule', 'Árbol milenario con el tronco más ancho del mundo, símbolo natural de Oaxaca', 8, 'natural'),
(31, 'Iglesia de Santa María', 'Templo colonial junto al Árbol del Tule con arte sacro y arquitectura tradicional', 8, 'histórica'),
(32, 'Mercado de Tule', 'Espacio gastronómico y artesanal con productos típicos de la región', 8, 'cultural'),
(33, 'Mercado 5 de Septiembre', 'Centro comercial tradicional con gastronomía istmeña y textiles zapotecos', 9, 'cultural'),
(34, 'Zona Arqueológica de Guiengola', 'Sitio prehispánico zapoteca en la cima de una montaña', 9, 'histórica'),
(35, 'Casa de la Cultura de Juchitán', 'Espacio artístico con exposiciones, danza, música y eventos comunitarios', 9, 'cultural'),
(36, 'Museo Regional de Huajuapan', 'Colección arqueológica y etnográfica de la Mixteca Alta', 10, 'cultural'),
(37, 'Templo de San Juan Bautista', 'Iglesia colonial con arquitectura barroca y valor histórico', 10, 'histórica'),
(38, 'Mirador del Cerro de las Minas', 'Vista panorámica de la ciudad y zona arqueológica mixteca', 10, 'escénica')
])

cursor.executemany('''
INSERT INTO hoteles (id, nombre, direccion, ciudad_id, estrellas, servicios) VALUES (?, ?, ?, ?, ?, ?);
''', [
  (1, 'Hotel Monte Albán', 'Centro Histórico', 1, 4, 'Cuenta con Tv, piscina, bar y estacionamiento'),
(2, 'Hotel Tortuga', 'Bulevar de la conservación', 2, 4, 'Cuenta con Tv, piscina, estacionamiento, vista al mar'),
(3, 'Hotel Playita', 'Bulevar Paseo internacional', 3, 3, 'Cuenta con Tv, piscina, estacionamiento, vista al mar, bar y resturante'),
(4, 'Barceló', 'Blvd. Benito Juárez 10, 70989 Tangolunda', 4, 5, 'Cuenta con Tv, piscina, estacionamiento, vista al mar, bares, resturantes, entretenimiento, gimnasio y spa'),
(5, 'Park Royal', 'Blvd. Benito Juárez 8, 70989 Tangolunda', 4, 5, 'Cuenta con Tv, piscina, estacionamiento, playa, bares, resturantes y entretenimiento'),
(6, 'Quinta Real Oaxaca', 'Centro Histórico', 1, 4, 'Cuenta con Tv, piscina, estacionamiento y resturante'),
(7, 'Casa Oaxaca Hotel', 'Calle Constitución 104-A, Centro', 1, 5, 'Cuenta con Tv, piscina, estacionamiento y resturante'),
(8, 'Hotel Azul Oaxaca', 'Calle Abasolo 313, Centro', 1, 4, 'Cuenta con Tv, piscina y resturante'),
(9, 'Hotel Santa Fe', 'Calle del Morro s/n, Zicatela', 3, 4, 'Piscina, restaurante, aire acondicionado, acceso a playa'),
(10, 'Casamar Suites', 'Calle Loma Bonita 2, Brisas de Zicatela', 3, 3, 'Cocina equipada, jardín, yoga, WiFi'),
(11, 'Hotel Rockaway', 'Calle del Morro 4, Playa Zicatela', 3, 4, 'Gimnasio, bar, piscina, estacionamiento'),
(15, 'Casa Pan de Miel', 'Camino a Punta Cometa, Mazunte', 2, 4, 'Piscina, WiFi, estacionamiento, desayuno incluido, vista al mar'),
(16, 'ZOA Hotel', 'Camino a Mermejita, Mazunte', 2, 4, 'Piscina, restaurante gourmet, jardín, zona de playa privada'),
(17, 'OceanoMar', 'Camino a Punta Cometa, Mazunte', 2, 4, 'Terraza, WiFi gratuito, cerca de la playa, servicio de masajes'),
(18, 'Casa Lu Hotel Boutique', 'Playa Mazunte, Mazunte', 2, 4, 'Piscina, estacionamiento privado, jardín, acceso directo a la playa'),
(20, 'Hotel Casa de las Bugambilias', 'Calle Reforma 402, Centro Histórico, Oaxaca de Juárez', 1, 4, 'WiFi, desayuno incluido, aire acondicionado, terraza, servicio de concierge'),
(21, 'Parador San Miguel Oaxaca', 'Calle Independencia 503, Centro Histórico, Oaxaca de Juárez', 1, 4, 'Restaurante, WiFi, aire acondicionado, servicio de lavandería, recepción 24 horas'),
(22, 'Hotel Castillo Huatulco', 'Boulevard Santa Cruz 303, Bahía de Santa Cruz, Huatulco', 4, 4, 'Piscina, restaurante, WiFi, aire acondicionado, estacionamiento'),
(23, 'Camino Real Zaashila', 'Playa Tangolunda, Huatulco', 4, 5, 'Playa privada, piscina, spa, restaurante, servicio a la habitación'),
(24, 'Hotel Alikar', 'Boulevard Chahué 151, Sector R, Huatulco', 4, 3, 'WiFi, piscina, restaurante, estacionamiento, aire acondicionado'),
(25, 'Cabañas Rancho Viejo', 'Carretera Federal 175, San José del Pacífico', 5, 3, 'Cabañas rústicas, chimenea, restaurante, vistas panorámicas, estacionamiento'),
(26, 'La Puesta del Sol', 'Camino a la Cumbre, San José del Pacífico', 5, 4, 'WiFi, terraza, restaurante, zona de fogata, servicio de transporte'),
(27, 'Cabañas El Mirador', 'Camino al Mirador, San José del Pacífico', 5, 3, 'Cabañas con vista, chimenea, zona de descanso, estacionamiento, acceso a senderos'),
(28, 'Hotel Don Cenobio', 'Av. Juárez 3, San Pablo Villa de Mitla', 6, 4, 'Restaurante, jardín, WiFi, estacionamiento, aire acondicionado'),
(29, 'Hotel Hacienda Don Juan', 'Carretera Internacional Km 45, Mitla', 6, 3, 'Piscina, restaurante, estacionamiento, zona de juegos, WiFi'),
(30, 'Hotel Mitla', 'Calle Benito Juárez 36, Centro, Mitla', 6, 3, 'WiFi, restaurante, terraza, servicio de recepción 24 horas, estacionamiento'),
(31, 'Casa Don José B&B', 'Calle Benito Juárez 12, Teotitlán del Valle', 7, 4, 'Desayuno incluido, WiFi, terraza, jardín, atención personalizada'),
(32, 'Hotel Tierra Antigua', 'Calle Hidalgo 45, Teotitlán del Valle', 7, 3, 'WiFi, estacionamiento, restaurante, zona de descanso, cerca de talleres textiles'),
(33, 'Casa de las Bugambilias Teotitlán', 'Calle Morelos 8, Teotitlán del Valle', 7, 4, 'WiFi, desayuno, jardín, decoración tradicional, servicio de guía local'),
(34, 'Hotel El Árbol del Tule', 'Av. Juárez 2, Santa María del Tule', 8, 3, 'WiFi, estacionamiento, jardín, desayuno incluido, cerca del Árbol del Tule'),
(35, 'Hostal de la Abuela', 'Calle Hidalgo 15, Santa María del Tule', 8, 3, 'WiFi, cocina compartida, terraza, atención familiar, zona tranquila'),
(36, 'Hotel Tule Plaza', 'Calle Reforma 101, Centro, Santa María del Tule', 8, 4, 'Restaurante, WiFi, aire acondicionado, estacionamiento, recepción 24 horas'),
(37, 'Hotel Central', 'Calle 5 de Septiembre 22, Centro, Juchitán de Zaragoza', 9, 3, 'WiFi, aire acondicionado, estacionamiento, restaurante, recepción 24 horas'),
(38, 'Hotel Santa Cruz', 'Av. Efraín R. Gómez 101, Juchitán de Zaragoza', 9, 3, 'WiFi, jardín, estacionamiento, desayuno incluido, zona tranquila'),
(39, 'Hotel Istmeño', 'Callejón del Encanto 8, Centro, Juchitán de Zaragoza', 9, 4, 'Restaurante, WiFi, terraza, servicio de habitaciones, decoración tradicional'),
(43, 'Hotel del Portal', 'Calle Valerio Trujano 5, Centro, Huajuapan de León', 10, 3, 'WiFi, restaurante, estacionamiento, recepción 24 horas, cerca del Zócalo'),
(44, 'Hotel La Cabaña', 'Carretera Internacional Km 2, Huajuapan de León', 10, 4, 'Piscina, restaurante, jardín, estacionamiento, habitaciones familiares'),
(45, 'Hotel San Miguel', 'Calle Morelos 18, Centro Histórico, Huajuapan de León', 10, 3, 'WiFi, terraza, servicio de habitaciones, desayuno incluido, atención personalizada')
])

cursor.executemany('''
INSERT INTO respuestas_usuarios (id, usuario_id, fecha_respuesta, tour) VALUES (?, ?, ?, ?);
''', [
  (1, 1, '2025-09-11 01:55:57', 'Del 15 al 20 de septiembre: Hotel Monte Albán, Restaurante La Olla, Monte Albán, Turismo Express')
])

cursor.executemany('''
INSERT INTO restaurantes (id, nombre, tipo_comida, direccion, ciudad_id, descripcion) VALUES (?, ?, ?, ?, ?, ?);
''', [
  (1, 'La Olla', 'Oaxaqueña', 'Calle Reforma 402', 1, 'Ideal para una cena romática, así como para ir con toda la familia '),
(2, 'El costeño', 'Mariscos', 'Calle tortuga 23', 2, 'Ideal para una cena con  vista al mar, así como para ir con toda la familia '),
(3, 'Mariscon Don Juan', 'Mariscos', 'Centro 120', 3, 'Ideal para comer mariscos frescos, ambiente familiar y buena atención '),
(4, 'El Fortim', 'Mariscos', 'Centro 1277', 4, 'Ideal para comer mariscos frescos, ambiente familiar y buena atención'),
(5, 'Los Danzantes', 'Fusión mexicana', 'Calle Macedonio Alcalá 403, Centro', 1, 'Ideal para probar comidas internacionales con el toque mexicano, con una buena ambeintación'),
(6, 'Origen', 'Alta cocina oaxaqueña', 'Av. Hidalgo 820, Centro', 1, 'Ideal para comer comida tradicional llevada al siguiente nivel'),
(7, 'El Cafecito', 'Internacional y mexicana', 'Av. del Morro 1, Zicatela', 3, 'Popular entre locales y turistas, ideal para desayunos y cenas relajadas'),
(8, 'Almoraduz', 'Alta cocina mexicana', 'Camino a Punta Zicatela 12', 3, 'Restaurante gourmet con ingredientes locales y técnicas contemporáneas'),
(9, 'La Olita', 'Fusión asiática y mexicana', 'Calle Tamarindos 1, Brisas de Zicatela', 3, 'Ambiente informal con tacos creativos y opciones vegetarianas'),
(13, 'Casa Oaxaca', 'Alta cocina oaxaqueña', 'Calle Constitución 104, Centro', 1, 'Restaurante elegante con terraza y platillos tradicionales reinterpretados con ingredientes locales'),
(14, 'Los Danzantes', 'Fusión oaxaqueña contemporánea', 'Calle Macedonio Alcalá 403, Centro', 1, 'Ambiente artístico con cocina creativa que mezcla tradición y modernidad'),
(15, 'El Biche Pobre', 'Comida típica oaxaqueña', 'Calzada Héroes de Chapultepec 213, Centro', 1, 'Restaurante familiar con platillos clásicos como tlayudas, moles y tasajo'),
(16, 'La Empanada', 'Comida oaxaqueña y mariscos', 'Calle Rinconcito, Mazunte', 2, 'Famoso por sus empanadas de camarón y ambiente rústico frente al mar'),
(17, 'Siddhartha', 'Fusión internacional y vegetariana', 'Camino a Punta Cometa, Mazunte', 2, 'Restaurante con vista al mar, ideal para desayunos saludables y cenas relajadas'),
(18, 'El Pescador', 'Mariscos y cocina costeña', 'Av. Principal, Mazunte', 2, 'Especializado en pescados frescos, ceviches y platillos típicos del Pacífico'),
(19, 'Terra-Cotta', 'Internacional y oaxaqueña', 'Guarumbo 307, La Crucecita, Huatulco', 4, 'Restaurante elegante con desayunos gourmet y platillos locales en un ambiente acogedor'),
(20, 'El Sabor de Oaxaca', 'Comida típica oaxaqueña', 'Boulevard Chahué, Sector H, Huatulco', 4, 'Especializado en moles, tlayudas y cocina tradicional con ingredientes locales'),
(21, 'Los Portales', 'Mariscos y cocina costeña', 'Av. Benito Juárez 5, Santa Cruz, Huatulco', 4, 'Famoso por sus pescados frescos, ceviches y vista a la bahía de Santa Cruz'),
(22, 'Café Hongo', 'Vegetariana y artesanal', 'Carretera Federal 175, San José del Pacífico', 5, 'Café rústico con opciones vegetarianas, postres caseros y vista panorámica'),
(23, 'Restaurante La Cumbre', 'Comida tradicional oaxaqueña', 'Camino al Mirador, San José del Pacífico', 5, 'Ofrece moles, tlayudas y bebidas calientes en un ambiente acogedor de montaña'),
(24, 'El Padrino', 'Comida mexicana y café', 'Centro, San José del Pacífico', 5, 'Pequeño restaurante con desayunos típicos, café local y atención familiar'),
(25, 'Comedor Doña Chica', 'Comida típica oaxaqueña', 'Calle Benito Juárez 18, Centro, Mitla', 6, 'Famoso por sus moles, memelas y atención casera cerca de la zona arqueológica'),
(26, 'Restaurante El Descanso', 'Mexicana tradicional', 'Av. Juárez 45, San Pablo Villa de Mitla', 6, 'Ambiente familiar con platillos regionales y tortillas hechas a mano'),
(27, 'Tierra Antigua Café', 'Fusión oaxaqueña y café artesanal', 'Calle Hidalgo 22, Mitla', 6, 'Café cultural con desayunos, bebidas locales y decoración inspirada en grecas zapotecas'),
(28, 'Tlamanalli', 'Comida zapoteca tradicional', 'Calle Guadalupe Victoria 65, Teotitlán del Valle', 7, 'Restaurante familiar dirigido por mujeres zapotecas, famoso por sus moles y cocina ancestral'),
(29, 'Comedor María Reyna', 'Comida oaxaqueña casera', 'Calle Hidalgo 22, Teotitlán del Valle', 7, 'Ofrece memelas, tasajo y bebidas tradicionales en un ambiente cálido y local'),
(30, 'Restaurante El Descanso Zapoteca', 'Comida regional y artesanal', 'Calle Juárez 10, Teotitlán del Valle', 7, 'Ideal para probar platillos elaborados con ingredientes locales y técnicas tradicionales'),
(31, 'Comedor El Tule', 'Comida típica oaxaqueña', 'Av. Juárez 10, Santa María del Tule', 8, 'Ofrece tlayudas, memelas y moles en un ambiente familiar frente al Árbol del Tule'),
(32, 'Restaurante La Ceiba', 'Mexicana tradicional', 'Calle Hidalgo 25, Santa María del Tule', 8, 'Restaurante con jardín y platillos regionales como tasajo, enchiladas y caldo de piedra'),
(33, 'Café del Tule', 'Café y repostería artesanal', 'Calle Reforma 8, Santa María del Tule', 8, 'Ideal para desayunos, café local y postres caseros en un espacio tranquilo'),
(34, 'La Palapa del Negro', 'Comida istmeña y mariscos', 'Av. Efraín R. Gómez 120, Juchitán de Zaragoza', 9, 'Especializado en garnachas, tamales de elote, mariscos frescos y ambiente tradicional'),
(35, 'Comedor Lupita', 'Cocina zapoteca casera', 'Calle 5 de Septiembre 45, Centro, Juchitán de Zaragoza', 9, 'Ofrece platillos típicos como estofado, molotes y bebidas regionales en ambiente familiar'),
(36, 'Restaurante Istmeñita', 'Comida regional oaxaqueña', 'Callejón del Encanto 10, Juchitán de Zaragoza', 9, 'Ideal para probar garnachas, enchiladas istmeñas y postres locales con atención cálida'),
(37, 'Comedor Lupita', 'Comida mixteca tradicional', 'Calle Morelos 45, Centro, Huajuapan de León', 10, 'Ofrece tamales de chileajo, mole mixteco y atención casera en ambiente familiar'),
(38, 'Restaurante El Campanario', 'Mexicana y regional', 'Av. 5 de Febrero 102, Huajuapan de León', 10, 'Restaurante amplio con menú variado, ideal para grupos y celebraciones locales'),
(39, 'Café La Cosecha', 'Café y repostería artesanal', 'Calle Valerio Trujano 12, Centro, Huajuapan de León', 10, 'Perfecto para desayunos, café local y postres caseros en un ambiente tranquilo')
])

cursor.executemany('''
INSERT INTO transportes (id, tipo, empresa, ciudad_id, contacto) VALUES (?, ?, ?, ?, ?);
''', [
  (1, 'Autobús', 'Turismo Express', 1, '9517654321'),
(2, 'Autobús', 'Gobierno Mazunte', 2, '9457812456'),
(3, 'Autobús', 'Gobierno', 3, '9784512456'),
(4, 'Autobús', 'Gobierno', 4, '9583491023'),
(5, 'Taxi turístico', 'Oaxaca Travel', 1, '9518881122'),
(6, 'Van privada', 'EcoTours Oaxaca', 1, '9514567890'),
(7, 'Taxi colectivo', 'Transportes Zicatela', 3, '9541123344'),
(8, 'Van turística', 'Puerto Shuttle', 3, '9549988776'),
(9, 'Autobús regional', 'ADO Puerto Escondido', 3, '9541239876'),
(13, 'Taxi local', 'Mazunte Eco Taxi', 2, '9581234567'),
(14, 'Van turística', 'Costa Sur Tours', 2, '9587654321'),
(15, 'Taxi turístico', 'Bahías Travel', 4, '9585832145'),
(16, 'Lancha recreativa', 'Tours Pacifico Azul', 4, '9581239876'),
(17, 'Taxi local', 'Montaña Mística', 5, '9512345678'),
(18, 'Van comunitaria', 'Sierra Sur Conecta', 5, '9518765432'),
(19, 'Transporte privado 4x4', 'EcoRutas Pacífico', 5, '9513456789'),
(20, 'Taxi local', 'Mitla Móvil', 6, '9514567890'),
(21, 'Van turística', 'Rutas del Mezcal', 6, '9516781234'),
(22, 'Transporte comunitario', 'Servicios Valle de Tlacolula', 6, '9517894561'),
(23, 'Taxi local', 'Zapoteco Tours', 7, '9512341122'),
(24, 'Van artesanal', 'Rutas del Telar', 7, '9518763344'),
(25, 'Transporte comunitario', 'Servicios Teotitlán', 7, '9517892211'),
(26, 'Taxi local', 'Tule Rápido', 8, '9513214567'),
(27, 'Van turística', 'Rutas del Árbol', 8, '9516547890'),
(28, 'Transporte comunitario', 'Servicios Tule Móvil', 8, '9519873210'),
(29, 'Taxi local', 'Istmo Rápido', 9, '9712345678'),
(30, 'Van regional', 'Transporte Zapoteca', 9, '9718765432'),
(31, 'Autobús interurbano', 'Istmeños Unidos', 9, '9713456789'),
(32, 'Taxi local', 'Mixteca Móvil', 10, '9531234567'),
(33, 'Van turística', 'Rutas Mixtecas', 10, '9537654321'),
(34, 'Autobús regional', 'Transportes Sierra Mixteca', 10, '9539876543')
])

cursor.executemany('''
INSERT INTO resenas (id, usuario_id, entidad_tipo, entidad_id, fecha_resena, comentario, calificacion) VALUES (?, ?, ?, ?, ?, ?, ?);
''', [
  (1, 1, 'hotel', 3, '2025-09-11 01:55:57', 'Excelente servicio y ubicación.', 5),
(2, 1, 'hotel', 3, '2025-09-19 01:02:42', 'Excelente servicio y ubicación.', 5),
(3, 1, 'hotel', 5, '2025-09-19 01:02:42', 'Habitaciones limpias pero algo pequeñas.', 4),
(4, 1, 'hotel', 7, '2025-09-19 01:02:42', 'Vista espectacular desde la terraza.', 5),
(5, 1, 'restaurante', 2, '2025-09-19 01:02:42', 'La tlayuda fue increíble, auténtico sabor oaxaqueño.', 5),
(6, 1, 'restaurante', 4, '2025-09-19 01:02:42', 'Buen ambiente pero el servicio fue lento.', 3),
(7, 1, 'restaurante', 6, '2025-09-19 01:02:42', 'Me encantó el mezcal artesanal que ofrecen.', 5),
(8, 1, 'atraccion', 1, '2025-09-19 01:02:42', 'Monte Albán es impresionante, muy bien conservado.', 5),
(9, 1, 'atraccion', 3, '2025-09-19 01:02:42', 'El jardín etnobotánico es muy educativo y relajante.', 4),
(10, 1, 'atraccion', 5, '2025-09-19 01:02:42', 'Punta Cometa tiene una vista inolvidable al atardecer.', 5),
(11, 1, 'atraccion', 7, '2025-09-19 01:02:42', 'El mercado de Tule tiene mucha variedad y buen precio.', 4),
(12, 1, 'hotel', 9, '2025-09-19 01:02:42', 'Ideal para descansar después de explorar el Istmo.', 4),
(13, 1, 'restaurante', 8, '2025-09-19 01:02:42', 'Comida deliciosa y atención cálida en el centro de Mitla.', 5),
(14, 1, 'atraccion', 10, '2025-09-19 01:02:42', 'El museo de Huajuapan tiene piezas únicas de la Mixteca.', 5),
(15, 1, 'atraccion', 12, '2025-09-19 01:02:42', 'Los talleres de telar en Teotitlán son fascinantes.', 5),
(16, 1, 'hotel', 11, '2025-09-19 01:02:42', 'Buena relación calidad-precio y cerca del centro.', 4),
(17, 1, 'restaurante', 10, '2025-09-19 01:02:42', 'Menú variado y excelente sazón mixteco.', 5),
(18, 1, 'atraccion', 14, '2025-09-19 01:02:42', 'La zona arqueológica de Mitla es muy interesante.', 5),
(19, 1, 'atraccion', 16, '2025-09-19 01:02:42', 'El mirador de San José ofrece una vista mágica.', 5),
(20, 1, 'hotel', 13, '2025-09-19 01:02:42', 'Perfecto para relajarse en Mazunte, muy tranquilo.', 5),
(21, 1, 'atraccion', 18, '2025-09-19 01:02:42', 'El Árbol del Tule es impresionante, vale la pena visitarlo.', 5)
])

cursor.executemany('''
INSERT INTO usuarios (id, nombre, correo, Apellidos, Edad, Telefono) VALUES (?, ?, ?, ?, ?, ?);
''', [
    (1, 'Brandon', 'brandon@example.com', 'Giron Cisneros', 25, '5510486557')
])


conn.commit()
conn.close()

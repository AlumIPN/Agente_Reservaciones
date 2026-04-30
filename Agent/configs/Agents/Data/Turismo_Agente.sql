-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 09-04-2026 a las 02:13:59
-- Versión del servidor: 9.4.0
-- Versión de PHP: 8.2.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `Turismo_Agente`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agencias_autos`
--

CREATE TABLE `agencias_autos` (
  `id` int NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `direccion` text,
  `ciudad_id` int DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `agencias_autos`
--

INSERT INTO `agencias_autos` (`id`, `nombre`, `direccion`, `ciudad_id`, `telefono`) VALUES
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
(37, 'Huajuapan Móvil', 'Boulevard Valerio Trujano 89, Huajuapan', 10, '9539876543');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atracciones`
--

CREATE TABLE `atracciones` (
  `id` int NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `descripcion` text,
  `ciudad_id` int DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `atracciones`
--

INSERT INTO `atracciones` (`id`, `nombre`, `descripcion`, `ciudad_id`, `tipo`) VALUES
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
(38, 'Mirador del Cerro de las Minas', 'Vista panorámica de la ciudad y zona arqueológica mixteca', 10, 'escénica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ciudades`
--

CREATE TABLE `ciudades` (
  `id` int NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `estado` varchar(100) DEFAULT 'Oaxaca'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `ciudades`
--

INSERT INTO `ciudades` (`id`, `nombre`, `estado`) VALUES
(1, 'Oaxaca de Juárez', 'Oaxaca'),
(2, 'Mazunte', 'Oaxaca'),
(3, 'Puerto Escondido', 'Oaxaca'),
(4, 'Huatulco', 'Oaxaca'),
(5, 'San José del Pacífico', 'Oaxaca'),
(6, 'Mitla', 'Oaxaca'),
(7, 'Teotitlán del Valle', 'Oaxaca'),
(8, 'Santa María del Tule', 'Oaxaca'),
(9, 'Juchitán de Zaragoza', 'Oaxaca'),
(10, 'Huajuapan de León', 'Oaxaca');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `hoteles`
--

CREATE TABLE `hoteles` (
  `id` int NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `direccion` text,
  `ciudad_id` int DEFAULT NULL,
  `estrellas` int DEFAULT NULL,
  `servicios` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `hoteles`
--

INSERT INTO `hoteles` (`id`, `nombre`, `direccion`, `ciudad_id`, `estrellas`, `servicios`) VALUES
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
(45, 'Hotel San Miguel', 'Calle Morelos 18, Centro Histórico, Huajuapan de León', 10, 3, 'WiFi, terraza, servicio de habitaciones, desayuno incluido, atención personalizada');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `itinerario`
--

CREATE TABLE `itinerario` (
  `id` int NOT NULL,
  `folio` varchar(20) NOT NULL,
  `tipo` varchar(30) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `ciudad` varchar(100) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `detalles` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `itinerario`
--

INSERT INTO `itinerario` (`id`, `folio`, `tipo`, `nombre`, `ciudad`, `fecha`, `detalles`) VALUES
(1, 'AX12G78T59HC023', 'Tour', 'Ruta Mediterránea', 'Valencia', '2026-04-02', 'Incluye transporte y hotel'),
(2, 'GJDOAX00001HVF', 'vuelo', 'Volaris Y41242', 'Guadalajara', '2026-04-10', 'Salida a las 16:54 desde Don Miguel Hidalgo y Costilla International, llegada a las 18:27 a Xoxocotlan'),
(3, 'GJDOAX00001HVF', 'hotel', 'Hotel Casa Maguey', 'Oaxaca', '2026-04-10', 'Check-in en C. de Los Libres 803, RUTA INDEPENDENCIA, Centro'),
(4, 'GJDOAX00001HVF', 'hotel', 'Hotel Casa Maguey', 'Oaxaca', '2026-04-17', 'Check-out en C. de Los Libres 803, RUTA INDEPENDENCIA, Centro'),
(5, 'GJDOAX00001HVF', 'restaurante', 'Los Danzantes', 'Oaxaca', '2026-04-13', 'Cena en C. Macedonio Alcalá 403-interior 4, RUTA INDEPENDENCIA, Centro'),
(6, 'RCBNT1234567890', 'vuelo', 'Vuelo VB4072 - VivaAerobus', 'Monterrey a Oaxaca', '2026-05-06', 'Salida: 13:10 desde MTY, Llegada: 15:00 a OAX'),
(7, 'RCBNT1234567890', 'hotel', 'Hotel Oaxaca Real', 'Oaxaca', '2026-05-06', 'Dirección: C. de Manuel García Vigil 306, RUTA INDEPENDENCIA, Centro, Oaxaca'),
(8, 'RCBNT1234567890', 'hotel', 'Hotel Oaxaca Real (check-out)', 'Oaxaca', '2026-05-12', 'Check-out'),
(9, '9Z7HGT53PCYW6KD', 'vuelo', 'Volaris - Vuelo Y41350', 'Puerto Escondido', '2026-05-05', 'Salida: 11:10, Llegada: 12:47'),
(10, '9Z7HGT53PCYW6KD', 'hotel', 'Hotel Santa Fe', 'Puerto Escondido', '2026-05-05', 'Check-in'),
(11, '9Z7HGT53PCYW6KD', 'hotel', 'Hotel Santa Fe', 'Puerto Escondido', '2026-05-10', 'Check-out'),
(12, '9Z7HGT53PCYW6KD', 'atracción', 'La Punta', 'Puerto Escondido', '2026-05-07', 'Surfear y relajarse'),
(13, 'POE2361H4T5Q7N8', 'vuelo', 'Volaris Y41350', 'Puerto Escondido', '2026-05-05', 'Salida: Guadalajara, 11:10, Llegada: 12:47'),
(14, 'POE2361H4T5Q7N8', 'hotel', 'Hotel Santa Fe', 'Puerto Escondido', '2026-05-05', 'Check-in'),
(15, 'POE2361H4T5Q7N8', 'hotel', 'Hotel Santa Fe', 'Puerto Escondido', '2026-05-10', 'Check-out'),
(16, 'POE2361H4T5Q7N8', 'atracción', 'La Punta', 'Puerto Escondido', '2026-05-07', 'Surf y relajación'),
(17, 'FDJ38Y6H9KPLMN0', 'vuelo', 'AM2467 de Aeromexico', 'Querétaro a Ciudad de México', '2026-06-01', 'Sale 18:40 - Llega 19:50'),
(18, 'FDJ38Y6H9KPLMN0', 'vuelo', 'AM394 de Aeromexico', 'Ciudad de México a Huatulco', '2026-06-01', 'Sale 17:10 - Llega 18:35'),
(19, 'FDJ38Y6H9KPLMN0', 'hotel', 'Holiday Inn Huatulco by IHG', 'Huatulco', '2026-06-01', 'Blvd. Benito Juárez 604-Sector \'A'),
(20, 'FDJ38Y6H9KPLMN0', 'hotel', 'Holiday Inn Huatulco by IHG', 'Huatulco', '2026-06-05', 'Check-out'),
(21, 'FDJ38Y6H9KPLMN0', 'atracción', 'Playa Maguey', 'Huatulco', '2026-06-02', 'Ninguno'),
(22, 'FDJ38Y6H9KPLMN0', 'renta_auto', 'More Car Renta de autos Huatulco', 'Huatulco', '2026-06-01', 'Aguaje Zapote, carretera federal 200'),
(23, 'J48R7Y3EWQS9KLF', 'vuelo', 'IB7483 de Iberia', 'Huatulco', '2026-04-10', 'Sale 13:55, Llega 15:10'),
(24, 'J48R7Y3EWQS9KLF', 'hotel', 'Barceló Huatulco', 'Huatulco', '2026-04-10', 'Ninguno'),
(25, 'J48R7Y3EWQS9KLF', 'atracción', 'Ruta del Café', 'Huatulco', '2026-04-12', 'Ninguno'),
(26, 'BKJ9DQW373BL145', 'vuelo', 'WestJet - Vuelo WS6122', 'Ciudad de México a Oaxaca', '2026-07-04', 'Hora de salida: 20:45, Hora de llegada: 22:02'),
(27, 'BKJ9DQW373BL145', 'vuelo', 'Volaris - Vuelo Y4441', 'Oaxaca a Ciudad de México', '2026-07-11', 'Hora de salida: 19:34, Hora de llegada: 20:45'),
(28, 'BKJ9DQW373BL145', 'hotel', 'Azul Cielo Hostel', 'Oaxaca', '2026-07-04', 'Dirección: Arteaga 608, colonia centro, 68000 Oaxaca de Juárez, Oax., México'),
(29, 'BKJ9DQW373BL145', 'atracción', 'Monte Albán', 'Oaxaca', '2026-07-07', 'Visita a la zona arqueológica'),
(30, 'A3FGH6J9KLPZ178', 'vuelo', 'Vuelo de ida', 'Puerto Escondido', '2026-04-28', 'Aeromexico, AM1639: Aguascalientes → Ciudad de México'),
(31, 'A3FGH6J9KLPZ178', 'vuelo', 'Vuelo de ida, conexión', 'Puerto Escondido', '2026-04-28', 'Iberia, IB7536: Ciudad de México → Puerto Escondido'),
(32, 'A3FGH6J9KLPZ178', 'vuelo', 'Vuelo de regreso', 'Aguascalientes', '2026-05-04', 'VivaAerobus, VB1189: Puerto Escondido → Ciudad de México'),
(33, 'A3FGH6J9KLPZ178', 'vuelo', 'Vuelo de regreso, conexión', 'Aguascalientes', '2026-05-04', 'Aeromexico, AM1640: Ciudad de México → Aguascalientes'),
(34, 'A3FGH6J9KLPZ178', 'hotel', 'Hotel Paraiso Escondido', 'Puerto Escondido', '2026-04-28', 'Dirección: Unión 10, Libertad, Puerto Escondido, Oax., México');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resenas`
--

CREATE TABLE `resenas` (
  `id` int NOT NULL,
  `usuario_id` int DEFAULT NULL,
  `entidad_tipo` enum('hotel','restaurante','agencia','atraccion','transporte') DEFAULT NULL,
  `entidad_id` int DEFAULT NULL,
  `fecha_resena` datetime DEFAULT CURRENT_TIMESTAMP,
  `comentario` text,
  `calificacion` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `resenas`
--

INSERT INTO `resenas` (`id`, `usuario_id`, `entidad_tipo`, `entidad_id`, `fecha_resena`, `comentario`, `calificacion`) VALUES
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
(21, 1, 'atraccion', 18, '2025-09-19 01:02:42', 'El Árbol del Tule es impresionante, vale la pena visitarlo.', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservas`
--

CREATE TABLE `reservas` (
  `folio` varchar(20) NOT NULL,
  `usuario_id` int NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `num_viajeros` int NOT NULL,
  `estado` varchar(20) DEFAULT 'pendiente',
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `reservas`
--

INSERT INTO `reservas` (`folio`, `usuario_id`, `fecha_inicio`, `fecha_fin`, `num_viajeros`, `estado`, `fecha_creacion`) VALUES
('9Z7HGT53PCYW6KD', 1, '2026-05-05', '2026-05-10', 1, 'Cancelado', '2026-04-08 00:31:48'),
('A1B2C3D4E5F6G7H', 1, '2026-04-02', '2026-04-08', 3, 'Cancelado', '2026-03-31 03:06:00'),
('A3FGH6J9KLPZ178', 1, '2026-04-28', '2026-05-04', 2, 'confirmado', '2026-04-08 23:34:52'),
('abcdef3445', 1, '2026-03-30', '2026-04-03', 2, 'Cancelado', '2026-03-31 02:52:33'),
('AX12G78T59HC023', 1, '2026-04-01', '2026-04-15', 3, 'Cancelado', '2026-03-31 03:15:21'),
('BKJ9DQW373BL145', 1, '2026-07-04', '2026-07-11', 1, 'confirmado', '2026-04-08 23:20:53'),
('FDJ38Y6H9KPLMN0', 1, '2026-06-01', '2026-07-07', 10, 'confirmado', '2026-04-08 01:11:07'),
('GJDOAX00001HVF', 1, '2026-04-10', '2026-04-17', 1, 'confirmado', '2026-04-01 00:04:54'),
('J48R7Y3EWQS9KLF', 1, '2026-04-10', '2026-04-14', 1, 'confirmado', '2026-04-08 01:47:42'),
('J94MC98ZXMK2015GX74D', 1, '2026-04-08', '2026-04-15', 1, 'confirmado', '2026-03-26 21:00:25'),
('POE2361H4T5Q7N8', 1, '2026-05-05', '2026-06-12', 1, 'confirmado', '2026-04-08 00:32:53'),
('RCBNT1234567890', 1, '2026-05-06', '2026-04-14', 2, 'confirmado', '2026-04-05 16:20:31'),
('RV00000000123AB', 1, '2026-04-16', '2026-04-20', 2, 'Cancelado', '2026-03-31 03:21:29');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `respuestas_usuarios`
--

CREATE TABLE `respuestas_usuarios` (
  `id` int NOT NULL,
  `usuario_id` int DEFAULT NULL,
  `fecha_respuesta` datetime DEFAULT CURRENT_TIMESTAMP,
  `tour` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `respuestas_usuarios`
--

INSERT INTO `respuestas_usuarios` (`id`, `usuario_id`, `fecha_respuesta`, `tour`) VALUES
(1, 1, '2025-09-11 01:55:57', 'Del 15 al 20 de septiembre: Hotel Monte Albán, Restaurante La Olla, Monte Albán, Turismo Express');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `restaurantes`
--

CREATE TABLE `restaurantes` (
  `id` int NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `tipo_comida` varchar(100) DEFAULT NULL,
  `direccion` text,
  `ciudad_id` int DEFAULT NULL,
  `descripcion` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `restaurantes`
--

INSERT INTO `restaurantes` (`id`, `nombre`, `tipo_comida`, `direccion`, `ciudad_id`, `descripcion`) VALUES
(1, 'La Olla', 'Oaxaqueña', 'Calle Reforma 402', 1, 'Ideal para una cena romática, así como para ir con toda la familia '),
(2, 'El costeño', 'Mariscos', 'Calle tortuga 23', 2, 'Ideal para una cena con  vista al mar, así como para ir con toda la familia '),
(3, 'Mariscon Don Juan', 'Mariscos', 'Centro 120', 3, 'Ideal para comer mariscos frescos, ambiente familiar y buena atención '),
(4, 'El Fortim', 'Mariscos', 'Centro 1277', 4, 'Ideal para comer mariscos frescos, ambiente familiar y buena atención'),
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
(39, 'Café La Cosecha', 'Café y repostería artesanal', 'Calle Valerio Trujano 12, Centro, Huajuapan de León', 10, 'Perfecto para desayunos, café local y postres caseros en un ambiente tranquilo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `transportes`
--

CREATE TABLE `transportes` (
  `id` int NOT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `empresa` varchar(100) DEFAULT NULL,
  `ciudad_id` int DEFAULT NULL,
  `contacto` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `transportes`
--

INSERT INTO `transportes` (`id`, `tipo`, `empresa`, `ciudad_id`, `contacto`) VALUES
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
(34, 'Autobús regional', 'Transportes Sierra Mixteca', 10, '9539876543');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `Apellidos` varchar(50) DEFAULT NULL,
  `Edad` int DEFAULT NULL,
  `Telefono` varchar(10) DEFAULT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `correo`, `Apellidos`, `Edad`, `Telefono`, `username`, `password`) VALUES
(1, 'Brandon', 'brandon@example.com', 'Giron Cisneros', 25, '5510486557', 'BrandGC18', 'AgentPr3'),
(2, 'Juan', 'Juan@example.com', 'Perez Lopez', 30, '4565287768', 'JP136', '1234abcd'),
(3, 'Diana', 'DiaGT@example.com', 'García Torres', 30, '5551234567', 'DianaGT', 'abcd1234'),
(4, 'Jose', 'JoseG@example.com', 'Gordillo Salazar', 22, '5545384560', 'JoseGS', 'GorSal18'),
(5, 'Sofia', 'SofiMo@example.com', 'Loaiza Morales', 25, '5595345978', 'SofiLM', 'abcd1234');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `agencias_autos`
--
ALTER TABLE `agencias_autos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ciudad_id` (`ciudad_id`);

--
-- Indices de la tabla `atracciones`
--
ALTER TABLE `atracciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ciudad_id` (`ciudad_id`);

--
-- Indices de la tabla `ciudades`
--
ALTER TABLE `ciudades`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `hoteles`
--
ALTER TABLE `hoteles`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ciudad_id` (`ciudad_id`);

--
-- Indices de la tabla `itinerario`
--
ALTER TABLE `itinerario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `folio` (`folio`);

--
-- Indices de la tabla `resenas`
--
ALTER TABLE `resenas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD PRIMARY KEY (`folio`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `respuestas_usuarios`
--
ALTER TABLE `respuestas_usuarios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `restaurantes`
--
ALTER TABLE `restaurantes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ciudad_id` (`ciudad_id`);

--
-- Indices de la tabla `transportes`
--
ALTER TABLE `transportes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ciudad_id` (`ciudad_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `correo` (`correo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `agencias_autos`
--
ALTER TABLE `agencias_autos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT de la tabla `atracciones`
--
ALTER TABLE `atracciones`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT de la tabla `ciudades`
--
ALTER TABLE `ciudades`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `hoteles`
--
ALTER TABLE `hoteles`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de la tabla `itinerario`
--
ALTER TABLE `itinerario`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT de la tabla `resenas`
--
ALTER TABLE `resenas`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `respuestas_usuarios`
--
ALTER TABLE `respuestas_usuarios`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `restaurantes`
--
ALTER TABLE `restaurantes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT de la tabla `transportes`
--
ALTER TABLE `transportes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `agencias_autos`
--
ALTER TABLE `agencias_autos`
  ADD CONSTRAINT `agencias_autos_ibfk_1` FOREIGN KEY (`ciudad_id`) REFERENCES `ciudades` (`id`);

--
-- Filtros para la tabla `atracciones`
--
ALTER TABLE `atracciones`
  ADD CONSTRAINT `atracciones_ibfk_1` FOREIGN KEY (`ciudad_id`) REFERENCES `ciudades` (`id`);

--
-- Filtros para la tabla `hoteles`
--
ALTER TABLE `hoteles`
  ADD CONSTRAINT `hoteles_ibfk_1` FOREIGN KEY (`ciudad_id`) REFERENCES `ciudades` (`id`);

--
-- Filtros para la tabla `itinerario`
--
ALTER TABLE `itinerario`
  ADD CONSTRAINT `itinerario_ibfk_1` FOREIGN KEY (`folio`) REFERENCES `reservas` (`folio`);

--
-- Filtros para la tabla `resenas`
--
ALTER TABLE `resenas`
  ADD CONSTRAINT `resenas_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD CONSTRAINT `reservas_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `respuestas_usuarios`
--
ALTER TABLE `respuestas_usuarios`
  ADD CONSTRAINT `respuestas_usuarios_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `restaurantes`
--
ALTER TABLE `restaurantes`
  ADD CONSTRAINT `restaurantes_ibfk_1` FOREIGN KEY (`ciudad_id`) REFERENCES `ciudades` (`id`);

--
-- Filtros para la tabla `transportes`
--
ALTER TABLE `transportes`
  ADD CONSTRAINT `transportes_ibfk_1` FOREIGN KEY (`ciudad_id`) REFERENCES `ciudades` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

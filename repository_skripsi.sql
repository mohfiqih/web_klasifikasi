-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 02, 2023 at 06:12 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `repository_skripsi`
--

-- --------------------------------------------------------

--
-- Table structure for table `berkas`
--

CREATE TABLE `berkas` (
  `id` int(11) NOT NULL,
  `judul` varchar(256) NOT NULL,
  `tanggal_berkas` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `berkas`
--

INSERT INTO `berkas` (`id`, `judul`, `tanggal_berkas`) VALUES
(7, 'bg.png', '2022-06-08 01:59:54');

-- --------------------------------------------------------

--
-- Table structure for table `daftar_soal`
--

CREATE TABLE `daftar_soal` (
  `id_soal` int(11) NOT NULL,
  `paket_id` int(11) NOT NULL,
  `soal` varchar(500) NOT NULL,
  `type_soal` enum('Skala Likert','Teks Singkat') NOT NULL,
  `sangat_setuju` int(11) NOT NULL DEFAULT 4,
  `setuju` int(11) NOT NULL DEFAULT 3,
  `tidak_setuju` int(11) NOT NULL DEFAULT 2,
  `sangat_tidak_setuju` int(11) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `daftar_soal`
--

INSERT INTO `daftar_soal` (`id_soal`, `paket_id`, `soal`, `type_soal`, `sangat_setuju`, `setuju`, `tidak_setuju`, `sangat_tidak_setuju`) VALUES
(145, 31, 'Bagus syncnau', 'Skala Likert', 4, 3, 2, 1),
(146, 31, 'Tampilan syncnau menarik', 'Skala Likert', 4, 3, 2, 1),
(147, 33, 'Oase baguss', 'Skala Likert', 4, 3, 2, 1),
(148, 31, 'Syncnau bagus', 'Skala Likert', 4, 3, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `klasifikasi`
--

CREATE TABLE `klasifikasi` (
  `id` int(11) NOT NULL,
  `id_identitas` varchar(100) NOT NULL,
  `nama_lengkap` varchar(200) NOT NULL,
  `prodi` enum('TI','TKOM','AK','FARM','SPMI','TIK') NOT NULL,
  `sebagai` enum('Super Admin','Pengevaluasi','Dosen','Mahasiswa') NOT NULL,
  `gender` enum('L','P') NOT NULL,
  `id_paket_jawaban` int(11) NOT NULL,
  `jawaban` text NOT NULL,
  `label` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `klasifikasi`
--

INSERT INTO `klasifikasi` (`id`, `id_identitas`, `nama_lengkap`, `prodi`, `sebagai`, `gender`, `id_paket_jawaban`, `jawaban`, `label`) VALUES
(83, '', '', '', '', '', 31, 'bagusss', 'Baik'),
(84, '22092002', 'Fiqih', 'TI', 'Mahasiswa', 'L', 31, 'Baguss bangettt', 'Baik');

-- --------------------------------------------------------

--
-- Table structure for table `kuesioner`
--

CREATE TABLE `kuesioner` (
  `id` int(11) NOT NULL,
  `id_identitas` varchar(100) NOT NULL,
  `nama_lengkap` varchar(200) NOT NULL,
  `prodi` enum('TI','TKOM','AK','FARM','SPMI','TIK') NOT NULL,
  `sebagai` enum('Super Admin','Pengevaluasi','Dosen','Mahasiswa') NOT NULL,
  `gender` enum('L','P') NOT NULL,
  `id_paket_jawaban` int(11) NOT NULL,
  `id_soal_kuesioner` int(11) NOT NULL,
  `type_soal` enum('Skala Likert','Teks Singkat') NOT NULL,
  `jawaban` text NOT NULL,
  `datecreated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kuesioner`
--

INSERT INTO `kuesioner` (`id`, `id_identitas`, `nama_lengkap`, `prodi`, `sebagai`, `gender`, `id_paket_jawaban`, `id_soal_kuesioner`, `type_soal`, `jawaban`, `datecreated`) VALUES
(216, '22092002', 'Moh. Fiqih Erinsyah', 'TI', 'Mahasiswa', 'L', 31, 145, 'Skala Likert', '4', '2023-04-30 16:51:46'),
(217, '22092002', 'Moh. Fiqih Erinsyah', 'TI', 'Mahasiswa', 'L', 31, 146, 'Skala Likert', '4', '2023-04-30 16:51:46'),
(218, '22092002', 'Moh. Fiqih Erinsyah', 'TI', 'Mahasiswa', 'L', 31, 148, 'Skala Likert', '4', '2023-04-30 16:51:46'),
(219, '22092002', 'Moh. Fiqih Erinsyah', 'TI', 'Mahasiswa', 'L', 31, 145, 'Skala Likert', '4', '2023-04-30 16:54:58'),
(220, '22092002', 'Moh. Fiqih Erinsyah', 'TI', 'Mahasiswa', 'L', 31, 146, 'Skala Likert', '4', '2023-04-30 16:54:58'),
(221, '22092002', 'Moh. Fiqih Erinsyah', 'TI', 'Mahasiswa', 'L', 31, 148, 'Skala Likert', '4', '2023-04-30 16:54:58'),
(222, '22092002', 'Moh. Fiqih Erinsyah', 'TI', 'Mahasiswa', 'L', 31, 145, 'Skala Likert', '4', '2023-04-30 17:19:06'),
(223, '22092002', 'Moh. Fiqih Erinsyah', 'TI', 'Mahasiswa', 'L', 31, 146, 'Skala Likert', '4', '2023-04-30 17:19:06'),
(224, '22092002', 'Moh. Fiqih Erinsyah', 'TI', 'Mahasiswa', 'L', 31, 148, 'Skala Likert', '4', '2023-04-30 17:19:06');

-- --------------------------------------------------------

--
-- Table structure for table `manajerial`
--

CREATE TABLE `manajerial` (
  `id_m` int(11) NOT NULL,
  `nama_apl` enum('Oase','Syncnau') NOT NULL,
  `versi_apl` varchar(50) NOT NULL,
  `tgl_publish` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `penyedia_apl` enum('TIK','Vendor') NOT NULL,
  `link_berkas` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `manajerial`
--

INSERT INTO `manajerial` (`id_m`, `nama_apl`, `versi_apl`, `tgl_publish`, `penyedia_apl`, `link_berkas`) VALUES
(68, 'Oase', '1.2', '2023-04-12 00:11:00', 'Vendor', 'https://drive.google.com/drive/folders/1LyGfiepI3wZlA7ekN58-GUh6QIn1pxOG?usp=sharing');

-- --------------------------------------------------------

--
-- Table structure for table `paket_soal`
--

CREATE TABLE `paket_soal` (
  `id_paket` int(11) NOT NULL,
  `nama_paket` varchar(256) NOT NULL,
  `aplikasi` enum('Syncnau','Oase') NOT NULL,
  `versi_apl_paket` varchar(256) NOT NULL,
  `tgl_kuesioner` datetime NOT NULL,
  `responden` varchar(50) NOT NULL,
  `jumlah_soal` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `paket_soal`
--

INSERT INTO `paket_soal` (`id_paket`, `nama_paket`, `aplikasi`, `versi_apl_paket`, `tgl_kuesioner`, `responden`, `jumlah_soal`) VALUES
(31, 'Sync', 'Syncnau', '1', '2023-04-04 23:52:00', 'Mahasiswa', 1),
(33, 'Oase', 'Oase', '1', '2023-04-04 23:52:00', 'Dosen,Mahasiswa', 1);

-- --------------------------------------------------------

--
-- Table structure for table `shared_link`
--

CREATE TABLE `shared_link` (
  `id` int(11) NOT NULL,
  `link_kuesioner` text NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shared_link`
--

INSERT INTO `shared_link` (`id`, `link_kuesioner`, `date_created`) VALUES
(11, 'https://e-repository.my.id/kuesioner/form/RVZWZlpoUlRPQU84YlhxMGpEOWlyZw', '2023-04-16 12:40:01');

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `nama` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`id`, `nama`) VALUES
(1, 'fiqih'),
(2, 'erinsyah');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `username_id` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `user_password` text COLLATE utf8_unicode_ci NOT NULL,
  `user_namalengkap` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `user_foto` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `user_level` enum('Super Admin','Pengevaluasi','Dosen','Mahasiswa','Sisfo','TIK') COLLATE utf8_unicode_ci NOT NULL,
  `user_prodi` enum('TI','ASP','TKOM','AK','FARM','PER','BID','MSN','DKV','PRWT','ELKTR','TIK','SPMI','ADM_TI','ADM_TKOM','ADM_AK') COLLATE utf8_unicode_ci NOT NULL,
  `user_gender` enum('L','P') COLLATE utf8_unicode_ci NOT NULL,
  `user_created` datetime NOT NULL DEFAULT current_timestamp(),
  `user_edited` datetime DEFAULT NULL,
  `user_status` enum('Aktif','Nonaktif') COLLATE utf8_unicode_ci NOT NULL,
  `hash_key` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `hash_expiry` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `email`, `username_id`, `user_password`, `user_namalengkap`, `user_foto`, `user_level`, `user_prodi`, `user_gender`, `user_created`, `user_edited`, `user_status`, `hash_key`, `hash_expiry`) VALUES
('230318024647', 'dosen@gmail.com', '14151617', '$2y$10$sDwUfZfVPkbGNl0Bcv4kye3/v9r.QCEIrTtnEKygCNa2Tq4OJzfSu', 'Dosen', '2aa88be5ccb5c84ac6b5ab1bbde81052.png', 'Dosen', 'TI', 'L', '2023-03-18 08:46:47', NULL, 'Nonaktif', NULL, NULL),
('230319073905', 'mahasiswa@gmail.com', '22092002', '$2y$10$/pzDfeCt1UoMMmwTwcjJfuqzYOx5jpHfz69J/CN4Z4ndS69qyk5AG', 'Moh. Fiqih Erinsyah', '2847697c164752b09e6cc20b6589c9ea.png', 'Mahasiswa', 'TKOM', 'L', '2023-03-19 13:39:05', NULL, 'Aktif', NULL, NULL),
('230331004608', 'spmi@gmail.com', '12345', '$2y$10$x2Swf1joaaYluaDfIL388eI.qvG3yoUtaZza6KNHR61f4JEJifBQ.', 'Bidang SPMI', 'fff30ea3a331e347448ff27b600d1e3a.png', 'Pengevaluasi', 'SPMI', 'L', '2023-03-31 05:46:08', NULL, 'Aktif', NULL, NULL),
('230407050455', 'mohfiqiherinsyah@gmail.com', '112233', '$2y$10$wvyNQyd9y0C8j/wKS6YZWeavDwqwx/UJ05Z/NLGDWKl9YZ2ueJjMq', 'Moh. Fiqih', '3178547fc6e54f70d1ccad650e4c5b5b.jpg', 'Super Admin', 'TIK', 'L', '2023-04-07 10:04:55', NULL, 'Aktif', '$2y$10$NXFjQAL/jQP7wxMX/rbf8uyppZ6uk.U17yxxQxGRUBjcPIMARiYVC', '2023-05-02 18:40'),
('230410160014', 'cproject163@gmail.com', '123567', '$2y$10$gCjvkAw3Dsf4c7N/X85Kh.RADF2/kfMqphjbZTIIpKDmgN/VmXVnO', 'Project', '', 'Mahasiswa', 'TI', 'L', '2023-04-10 21:00:14', NULL, 'Aktif', NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `berkas`
--
ALTER TABLE `berkas`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `daftar_soal`
--
ALTER TABLE `daftar_soal`
  ADD PRIMARY KEY (`id_soal`),
  ADD UNIQUE KEY `soal` (`soal`),
  ADD KEY `paket_id` (`paket_id`);

--
-- Indexes for table `klasifikasi`
--
ALTER TABLE `klasifikasi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_paket` (`id_paket_jawaban`);

--
-- Indexes for table `kuesioner`
--
ALTER TABLE `kuesioner`
  ADD PRIMARY KEY (`id`),
  ADD KEY `paket` (`id_paket_jawaban`),
  ADD KEY `soal` (`id_soal_kuesioner`);

--
-- Indexes for table `manajerial`
--
ALTER TABLE `manajerial`
  ADD PRIMARY KEY (`id_m`);

--
-- Indexes for table `paket_soal`
--
ALTER TABLE `paket_soal`
  ADD PRIMARY KEY (`id_paket`);

--
-- Indexes for table `shared_link`
--
ALTER TABLE `shared_link`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `user_nama` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `berkas`
--
ALTER TABLE `berkas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `daftar_soal`
--
ALTER TABLE `daftar_soal`
  MODIFY `id_soal` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=149;

--
-- AUTO_INCREMENT for table `klasifikasi`
--
ALTER TABLE `klasifikasi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;

--
-- AUTO_INCREMENT for table `kuesioner`
--
ALTER TABLE `kuesioner`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=225;

--
-- AUTO_INCREMENT for table `manajerial`
--
ALTER TABLE `manajerial`
  MODIFY `id_m` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=70;

--
-- AUTO_INCREMENT for table `paket_soal`
--
ALTER TABLE `paket_soal`
  MODIFY `id_paket` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `shared_link`
--
ALTER TABLE `shared_link`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `klasifikasi`
--
ALTER TABLE `klasifikasi`
  ADD CONSTRAINT `id_paket` FOREIGN KEY (`id_paket_jawaban`) REFERENCES `paket_soal` (`id_paket`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `kuesioner`
--
ALTER TABLE `kuesioner`
  ADD CONSTRAINT `paket` FOREIGN KEY (`id_paket_jawaban`) REFERENCES `paket_soal` (`id_paket`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `soal` FOREIGN KEY (`id_soal_kuesioner`) REFERENCES `daftar_soal` (`id_soal`) ON DELETE NO ACTION ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

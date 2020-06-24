-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 08, 2020 at 12:27 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `group20`
--

-- --------------------------------------------------------

--
-- Table structure for table `action`
--

CREATE TABLE `action` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `action`
--

INSERT INTO `action` (`id`, `name`) VALUES
(48, 'Apply for college');

-- --------------------------------------------------------

--
-- Table structure for table `alternatives`
--

CREATE TABLE `alternatives` (
  `id` int(11) NOT NULL,
  `alt_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `alternatives`
--

INSERT INTO `alternatives` (`id`, `alt_name`) VALUES
(15, 'IIITD'),
(16, 'Thapar'),
(17, 'NIT_Raipur');

-- --------------------------------------------------------

--
-- Table structure for table `alt_objectives`
--

CREATE TABLE `alt_objectives` (
  `alt_name` varchar(20) NOT NULL,
  `Minimize_Cost` varchar(40) DEFAULT NULL,
  `Maximize_Safety` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `alt_objectives`
--

INSERT INTO `alt_objectives` (`alt_name`, `Minimize_Cost`, `Maximize_Safety`) VALUES
('Thapar', NULL, NULL),
('NITRR', NULL, NULL),
('hufhf', NULL, NULL),
('IIITD', 'keep_upto_80000', 'safe_environment'),
('Thapar', NULL, NULL),
('NIT_Raipur', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `alt_uncertainties`
--

CREATE TABLE `alt_uncertainties` (
  `alt_name` varchar(20) DEFAULT NULL,
  `Teaching_capability` varchar(40) DEFAULT NULL,
  `Placements` varchar(40) DEFAULT NULL,
  `Reputation_of_college` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `alt_uncertainties`
--

INSERT INTO `alt_uncertainties` (`alt_name`, `Teaching_capability`, `Placements`, `Reputation_of_college`) VALUES
('Thapar', NULL, NULL, NULL),
('NITRR', NULL, NULL, NULL),
('hufhf', NULL, NULL, NULL),
('IIITD', 'good', 'Very_good', 'good'),
('Thapar', NULL, NULL, NULL),
('NIT_Raipur', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `decision`
--

CREATE TABLE `decision` (
  `id` int(10) NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `decision`
--

INSERT INTO `decision` (`id`, `name`) VALUES
(29, 'Which institute for Btech');

-- --------------------------------------------------------

--
-- Table structure for table `information_unc`
--

CREATE TABLE `information_unc` (
  `decision_id` int(11) NOT NULL,
  `unc_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `institute_attribute`
--

CREATE TABLE `institute_attribute` (
  `alt_name` varchar(50) NOT NULL,
  `date` varchar(40) DEFAULT NULL,
  `application_fees` varchar(40) DEFAULT NULL,
  `tution_fees` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `institute_attribute`
--

INSERT INTO `institute_attribute` (`alt_name`, `date`, `application_fees`, `tution_fees`) VALUES
('IIITD', '23/05/2020', '1000', '95000'),
('Thapar', NULL, NULL, NULL),
('NIT_Raipur', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `objectives`
--

CREATE TABLE `objectives` (
  `id` int(11) NOT NULL,
  `imperative` varchar(30) NOT NULL,
  `verb` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `objectives`
--

INSERT INTO `objectives` (`id`, `imperative`, `verb`) VALUES
(15, 'Minimize', 'Cost'),
(16, 'Maximize', 'Safety');

-- --------------------------------------------------------

--
-- Table structure for table `uncertainties`
--

CREATE TABLE `uncertainties` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `type` varchar(40) NOT NULL,
  `edge_type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `uncertainties`
--

INSERT INTO `uncertainties` (`id`, `name`, `type`, `edge_type`) VALUES
(26, 'Fees', 'Deterministic', 'informational'),
(27, 'security_fees', 'Non_deterministic', 'conditional'),
(28, 'hostel_fees', 'Non_deterministic', 'conditional'),
(29, 'Reputation_of_college', 'Non_deterministic', 'informational'),
(30, 'Placements', 'Non_deterministic', 'functional'),
(31, 'Teaching_capability', 'Non_deterministic', 'functional');

-- --------------------------------------------------------

--
-- Table structure for table `uncertainties_to_uncertainties`
--

CREATE TABLE `uncertainties_to_uncertainties` (
  `u1` int(50) NOT NULL,
  `u2` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `uncertainties_to_uncertainties`
--

INSERT INTO `uncertainties_to_uncertainties` (`u1`, `u2`) VALUES
(27, 26),
(28, 26);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `action`
--
ALTER TABLE `action`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `alternatives`
--
ALTER TABLE `alternatives`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `decision`
--
ALTER TABLE `decision`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `objectives`
--
ALTER TABLE `objectives`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `uncertainties`
--
ALTER TABLE `uncertainties`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `action`
--
ALTER TABLE `action`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `alternatives`
--
ALTER TABLE `alternatives`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `decision`
--
ALTER TABLE `decision`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `objectives`
--
ALTER TABLE `objectives`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `uncertainties`
--
ALTER TABLE `uncertainties`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

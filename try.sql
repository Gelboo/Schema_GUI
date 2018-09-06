-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 05, 2018 at 02:31 PM
-- Server version: 5.7.23-0ubuntu0.18.04.1
-- PHP Version: 5.6.37-1+ubuntu18.04.1+deb.sury.org+1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `try`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `Id` int(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  `website` varchar(20) NOT NULL,
  `lat` int(10) NOT NULL,
  `longg` int(10) NOT NULL,
  `primary_poc` varchar(20) NOT NULL,
  `sales_rep_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Orders`
--

CREATE TABLE `Orders` (
  `Id` int(10) NOT NULL,
  `account_id` int(10) NOT NULL,
  `standard_qty` int(10) NOT NULL,
  `poster_qty` int(10) NOT NULL,
  `total` int(10) NOT NULL,
  `standard_amt_usd` int(10) NOT NULL,
  `gloss_amt_usd` int(10) NOT NULL,
  `poster_amt_usd` int(10) NOT NULL,
  `total_amt_usd` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `region`
--

CREATE TABLE `region` (
  `Id` int(10) NOT NULL,
  `name` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `sales_reps`
--

CREATE TABLE `sales_reps` (
  `Id` int(11) NOT NULL,
  `name` int(11) NOT NULL,
  `region_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `web_events`
--

CREATE TABLE `web_events` (
  `occured_at` date NOT NULL,
  `account_id` int(11) NOT NULL,
  `channel` int(11) NOT NULL,
  `Id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `sales_rep_id` (`sales_rep_id`);

--
-- Indexes for table `Orders`
--
ALTER TABLE `Orders`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `account_id` (`account_id`);

--
-- Indexes for table `region`
--
ALTER TABLE `region`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `sales_reps`
--
ALTER TABLE `sales_reps`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `region_id` (`region_id`);

--
-- Indexes for table `web_events`
--
ALTER TABLE `web_events`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `account_id` (`account_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts`
--
ALTER TABLE `accounts`
  ADD CONSTRAINT `accounts_ibfk_1` FOREIGN KEY (`Id`) REFERENCES `web_events` (`account_id`);

--
-- Constraints for table `Orders`
--
ALTER TABLE `Orders`
  ADD CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `accounts` (`Id`);

--
-- Constraints for table `sales_reps`
--
ALTER TABLE `sales_reps`
  ADD CONSTRAINT `sales_reps_ibfk_1` FOREIGN KEY (`region_id`) REFERENCES `region` (`Id`),
  ADD CONSTRAINT `sales_reps_ibfk_2` FOREIGN KEY (`Id`) REFERENCES `accounts` (`sales_rep_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

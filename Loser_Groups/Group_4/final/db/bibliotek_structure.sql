-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  lun. 21 mai 2018 à 12:11
-- Version du serveur :  10.1.31-MariaDB
-- Version de PHP :  7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `bibliotek`
--
CREATE DATABASE IF NOT EXISTS `bibliotek` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;
USE `bibliotek`;

-- --------------------------------------------------------

--
-- Structure de la table `authors`
--

CREATE TABLE `authors` (
  `authorId` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  `image_url` varchar(200) NOT NULL,
  `wiki_url` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `books`
--

CREATE TABLE `books` (
  `bookId` int(11) NOT NULL,
  `title` varchar(300) NOT NULL,
  `authorId` int(11) NOT NULL,
  `publisher` varchar(150) NOT NULL,
  `published_date` varchar(15) DEFAULT NULL,
  `description` text,
  `isbn10` varchar(20) DEFAULT NULL,
  `isbn13` varchar(20) DEFAULT NULL,
  `categoryId` int(11) NOT NULL,
  `booktype` varchar(30) NOT NULL,
  `language` varchar(30) NOT NULL,
  `thumbnail` varchar(200) DEFAULT NULL,
  `page_count` int(5) DEFAULT NULL,
  `md5` varchar(32) DEFAULT NULL,
  `url_info` varchar(200) DEFAULT NULL,
  `dl_link1` varchar(200) DEFAULT NULL,
  `dl_link2` varchar(200) DEFAULT NULL,
  `chosen_url` varchar(10) NOT NULL,
  `filepath` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `categories`
--

CREATE TABLE `categories` (
  `categoryId` int(11) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `portfolios`
--

CREATE TABLE `portfolios` (
  `portfolioId` int(11) NOT NULL,
  `name` varchar(300) NOT NULL,
  `userId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `portfolios_books`
--

CREATE TABLE `portfolios_books` (
  `portfolio_bookId` int(11) NOT NULL,
  `bookId` int(11) NOT NULL,
  `portfolioId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `userId` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `surname` varchar(200) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `authors`
--
ALTER TABLE `authors`
  ADD PRIMARY KEY (`authorId`);

--
-- Index pour la table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`bookId`),
  ADD KEY `authorId` (`authorId`),
  ADD KEY `categoryId` (`categoryId`);

--
-- Index pour la table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`categoryId`);

--
-- Index pour la table `portfolios`
--
ALTER TABLE `portfolios`
  ADD PRIMARY KEY (`portfolioId`),
  ADD KEY `userId` (`userId`);

--
-- Index pour la table `portfolios_books`
--
ALTER TABLE `portfolios_books`
  ADD PRIMARY KEY (`portfolio_bookId`),
  ADD KEY `bookId` (`bookId`),
  ADD KEY `portfolioId` (`portfolioId`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userId`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `authors`
--
ALTER TABLE `authors`
  MODIFY `authorId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT pour la table `books`
--
ALTER TABLE `books`
  MODIFY `bookId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT pour la table `categories`
--
ALTER TABLE `categories`
  MODIFY `categoryId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT pour la table `portfolios`
--
ALTER TABLE `portfolios`
  MODIFY `portfolioId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT pour la table `portfolios_books`
--
ALTER TABLE `portfolios_books`
  MODIFY `portfolio_bookId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `userId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `books_ibfk_1` FOREIGN KEY (`authorId`) REFERENCES `authors` (`authorId`),
  ADD CONSTRAINT `books_ibfk_2` FOREIGN KEY (`categoryId`) REFERENCES `categories` (`categoryId`);

--
-- Contraintes pour la table `portfolios`
--
ALTER TABLE `portfolios`
  ADD CONSTRAINT `portfolios_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `users` (`userId`);

--
-- Contraintes pour la table `portfolios_books`
--
ALTER TABLE `portfolios_books`
  ADD CONSTRAINT `portfolios_books_ibfk_1` FOREIGN KEY (`bookId`) REFERENCES `books` (`bookId`),
  ADD CONSTRAINT `portfolios_books_ibfk_2` FOREIGN KEY (`portfolioId`) REFERENCES `portfolios` (`portfolioId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

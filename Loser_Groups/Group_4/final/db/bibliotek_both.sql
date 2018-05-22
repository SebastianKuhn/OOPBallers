-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  lun. 21 mai 2018 à 12:12
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

--
-- Déchargement des données de la table `authors`
--

INSERT INTO `authors` (`authorId`, `name`, `description`, `image_url`, `wiki_url`) VALUES
(1, 'Tibshirani robert', 'asdasd', 'asdasdasd', 'asdasdasdasdas'),
(2, 'JeanBonnessadadadds', 'Jemappelasda', 'http://wikipedia.com', 'asdasdasdasdas'),
(3, 'Tibshirani jambes', 'asdasd', 'asdasdasd', 'asdasdasdasdas'),
(5, 'Tibshirani jambes', 'asdasd', 'http://wikipedia.com', 'asdasdasdasdas'),
(6, 'Tibshirasdasdasdani jambes', 'asdasd', 'http://wikipedia.com', 'asdasdasdasdas'),
(7, 'Tibshirani james', 'asdasd', 'asdasdasd', 'asdasdasdasdas'),
(8, 'Tibshirani jamesasdasd', 'asdasd', 'asdasdasd', 'asdasdasdasdas'),
(9, 'Tibshirani jamesasdasdasdadasd', 'asdasd', 'asdasdasd', 'asdasdasdasdas'),
(11, 'Benjamin Graham', 'Benjamin Graham (; né Grossbaum; May 9, 1894 – September 21, 1976) was a British-born American investor, economist, and professor', 'https://upload.wikimedia.org/wikipedia/commons/7/71/Benjamin-Graham-fundamental.jpg', 'https://en.wikipedia.org/wiki/Benjamin_Graham'),
(14, 'Kevin P. Murphy', '', '', ''),
(15, 'Trevor Hastie', '', '', ''),
(16, 'Ashlee Vance', '', '', ''),
(17, 'Tibshirani jameasdassasdasdasdadasd', 'asdasd', 'asdasdasd', 'asdasdasdasdas'),
(18, 'Steven C. Chapra', '', '', ''),
(19, 'Jeffrey M. Wooldridge', '', '', ''),
(20, 'Thomas H. Cormen', '', '', ''),
(21, 'Stuart Russell', '', '', ''),
(22, 'Tibshirani jameasdassasdasdssasdadasd', 'asdasd', 'asdasdasd', 'asdasdasdasdas'),
(24, 'Jon Loeliger', '', '', ''),
(25, 'David M. Beazley', 'David Beazley is an American software engineer', 'https://upload.wikimedia.org/wikipedia/commons/d/d4/David_Beazley_-_PyData_Chicago_2016.png', 'https://en.wikipedia.org/wiki/David_M._Beazley'),
(26, 'Deborah de Wolff', 'Cool girl!', 'http://placeholder.it/200x200', 'asdas');

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

--
-- Déchargement des données de la table `books`
--

INSERT INTO `books` (`bookId`, `title`, `authorId`, `publisher`, `published_date`, `description`, `isbn10`, `isbn13`, `categoryId`, `booktype`, `language`, `thumbnail`, `page_count`, `md5`, `url_info`, `dl_link1`, `dl_link2`, `chosen_url`, `filepath`) VALUES
(19, 'Machine Learning', 14, 'MIT Press', '2012-08-24', 'A comprehensive introduction to machine learning that uses probabilistic models and inference as a unifying approach.', '0262018020', '9780262018029', 10, 'pdf', 'en', 'http://books.google.com/books/content?id=NZP6AQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 1067, 'NaN', 'https://www.googleapis.com/books/v1/volumes/NZP6AQAAQBAJ', 'http://libgen.pw/view.php?id=870085', 'http://libgen.io/ads.php?md5=8ECFEEB2E1F9A19C770FBA1FF85FA566', 'dl_link2', '../../download/kevin-p-murphy/machine-learning.pdf'),
(23, 'Numerical Methods for Engineers', 18, 'NaN', '2016-03', 'Numerical Methods for Engineers retains the instructional techniques that have made the text so successful. Chapra and Canale\'s unique approach opens each part of the text with sections called \"Motivation\" \"Mathematical Background\" and \"Orientation\". Each part closes with an \"Epilogue\" containing \"Trade-Offs\" \"Important Relationships and Formulas\" and \"Advanced Methods and Additional References\". Much more than a summary the Epilogue deepens understanding of what has been learned and provides a peek into more advanced methods. Numerous new or revised problems are drawn from actual engineering practice. The expanded breadth of engineering disciplines covered is especially evident in these exercises which now cover such areas as biotechnology and biomedical engineering. Excellent new examples and case studies span all areas of engineering giving students a broad exposure to various fields in engineering.McGraw-Hill Education\'s Connect is also available as an optional add on item. Connect is the only integrated learning system that empowers students by continuously adapting to deliver precisely what they need when they need it how they need it so that class time is more effective. Connect allows the professor to assign homework quizzes and tests easily and automatically grades and records the scores of the student\'s work. Problems are randomized to prevent sharing of answers an may also have a \"multi-step solution\" which helps move the students\' learning along if they experience difficulty.', '9789814670876', '9814670871', 14, 'pdf', 'en', 'http://books.google.com/books/content?id=Z-vgsgEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api', 970, 'NaN', 'https://www.googleapis.com/books/v1/volumes/Z-vgsgEACAAJ', 'http://libgen.pw/view.php?id=1300946', 'http://libgen.io/ads.php?md5=4B1C96F1187FBDC0184EB1856D06A1E4', 'dl_link2', '../../download/steven-c-chapraraymond-p-canale/numerical-methods-for-engineers.pdf'),
(24, 'Introductory Econometrics: A Modern Approach', 19, 'Cengage Learning', '2015-09-30', 'Discover how empirical researchers today actually think about and apply econometric methods with the practical professional approach in Wooldridge\'s INTRODUCTORY ECONOMETRICS: A MODERN APPROACH 6E. Unlike traditional books this unique presentation demonstrates how econometrics has moved beyond just a set of abstract tools to become genuinely useful for answering questions in business policy evaluation and forecasting environments. INTRODUCTORY ECONOMETRICS is organized around the type of data being analyzed with a systematic approach that only introduces assumptions as they are needed. This makes the material easier to understand and ultimately leads to better econometric practices. Packed with timely relevant applications the book introduces the latest emerging developments in the field. Gain a full understanding of the impact of econometrics in real practice today with the insights and applications found only in INTRODUCTORY ECONOMETRICS: A MODERN APPROACH 6E. Important Notice: Media content referenced within the product description or the product text may not be available in the ebook version.', '1305446380', '9781305446380', 15, 'pdf', 'en', 'http://books.google.com/books/content?id=wUF4BwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 912, 'NaN', 'https://www.googleapis.com/books/v1/volumes/wUF4BwAAQBAJ', 'http://libgen.pw/view.php?id=935014', 'http://libgen.io/ads.php?md5=A96C6C5AF5DBE7011B01C3D8AC3AF248', 'dl_link2', '../../download/jeffrey-m-wooldridge/introductory-econometrics-a-modern-approach.pdf'),
(25, 'Introduction to Algorithms', 20, 'MIT Press', '2009-07-31', 'A new edition of the essential text and professional reference with substantial new material on such topics as vEB trees multithreaded algorithms dynamic programming and edge-based flow.', '0262533057', '9780262533058', 10, 'pdf', 'en', 'http://books.google.com/books/content?id=aefUBQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 1292, 'NaN', 'https://www.googleapis.com/books/v1/volumes/aefUBQAAQBAJ', 'http://libgen.pw/view.php?id=2158070', 'http://libgen.io/ads.php?md5=47214322FA81F9292AF442C9CAE67335', 'dl_link2', '../../download/thomas-h-cormen/introduction-to-algorithms.pdf'),
(35, 'The Intelligent Investor Rev. Ed', 11, 'Harper Collins', '2009-03-17', 'The greatest investment advisor of the twentieth century Benjamin Graham taught and inspired people worldwide. Graham\'s philosophy of “value investing”—which shields investors from substantial error and teaches them to develop long-term strategies—has made The Intelligent Investor the stock market bible ever since its original publication in 1949. Over the years market developments have proven the wisdom of Graham’s strategies. While preserving the integrity of Graham’s original text this revised edition includes updated commentary by noted financial journalist Jason Zweig whose perspective incorporates the realities of today’s market draws parallels between Graham’s examples and today’s financial headlines and gives readers a more thorough understanding of how to apply Graham’s principles. Vital and indispensable The Intelligent Investor is the most important book you will ever read on how to reach your financial goals.', '0061745170', '9780061745171', 15, 'pdf', 'en', 'http://books.google.com/books/content?id=-NdcCSt8t_YC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 640, 'NaN', 'https://www.googleapis.com/books/v1/volumes/-NdcCSt8t_YC', 'http://libgen.pw/view.php?id=727419', 'http://libgen.io/ads.php?md5=13BE6D6F1ECB3B5EF769BE7379B26D35', 'dl_link2', '../../download/benjamin-graham/the-intelligent-investor-rev-ed.pdf'),
(54, 'Version Control with Git', 24, '\"O\'Reilly Media Inc.\"', '2012-08-14', 'Get up to speed on Git for tracking branching merging and managing code revisions. Through a series of step-by-step tutorials this practical guide takes you quickly from Git fundamentals to advanced techniques and provides friendly yet rigorous advice for navigating the many functions of this open source version control system. This thoroughly revised edition also includes tips for manipulating trees extended coverage of the reflog and stash and a complete introduction to the GitHub repository. Git lets you manage code development in a virtually endless variety of ways once you understand how to harness the system’s flexibility. This book shows you how. Learn how to use Git for several real-world development scenarios Gain insight into Git’s common-use cases initial tasks and basic functions Use the system for both centralized and distributed version control Learn how to manage merges conflicts patches and diffs Apply advanced techniques such as rebasing hooks and ways to handle submodules Interact with Subversion (SVN) repositories—including SVN to Git conversions Navigate use and contribute to open source projects though GitHub', '1449345042', '9781449345044', 10, 'pdf', 'en', 'http://books.google.com/books/content?id=qIucp61eqAwC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 456, 'NaN', 'https://www.googleapis.com/books/v1/volumes/qIucp61eqAwC', 'http://libgen.pw/view.php?id=188793', 'http://libgen.io/ads.php?md5=CBDE94479683C890075913936E60276F', 'dl_link2', '../../download/jon-loeligermatthew-mccullough/version-control-with-git.pdf'),
(55, 'Python Cookbook', 25, '\"O\'Reilly Media Inc.\"', '2013-05-10', 'If you need help writing programs in Python 3 or want to update older Python 2 code this book is just the ticket. Packed with practical recipes written and tested with Python 3.3 this unique cookbook is for experienced Python programmers who want to focus on modern tools and idioms. Inside you’ll find complete recipes for more than a dozen topics covering the core Python language as well as tasks common to a wide variety of application domains. Each recipe contains code samples you can use in your projects right away along with a discussion about how and why the solution works. Topics include: Data Structures and Algorithms Strings and Text Numbers Dates and Times Iterators and Generators Files and I/O Data Encoding and Processing Functions Classes and Objects Metaprogramming Modules and Packages Network and Web Programming Concurrency Utility Scripting and System Administration Testing Debugging and Exceptions C Extensions', '1449357350', '9781449357351', 10, 'pdf', 'en', 'http://books.google.com/books/content?id=S_SJ2LaZH8EC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 706, 'NaN', 'https://www.googleapis.com/books/v1/volumes/S_SJ2LaZH8EC', 'http://libgen.pw/view.php?id=927749', 'http://libgen.io/ads.php?md5=874C56CBC659EA2E7BA8B90CFCD1E316', 'dl_link2', '../../download/david-beazleybrian-k-jones/python-cookbook.pdf');

-- --------------------------------------------------------

--
-- Structure de la table `categories`
--

CREATE TABLE `categories` (
  `categoryId` int(11) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `categories`
--

INSERT INTO `categories` (`categoryId`, `name`) VALUES
(6, 'Psychology'),
(7, 'Entrepreneurship'),
(8, 'Business'),
(9, 'Mathematics'),
(10, 'Computers'),
(13, 'Programming'),
(14, 'Technology & Engineering'),
(15, 'Business & Economics'),
(18, 'Fantasy');

-- --------------------------------------------------------

--
-- Structure de la table `portfolios`
--

CREATE TABLE `portfolios` (
  `portfolioId` int(11) NOT NULL,
  `name` varchar(300) NOT NULL,
  `userId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `portfolios`
--

INSERT INTO `portfolios` (`portfolioId`, `name`, `userId`) VALUES
(13, 'The Amazing portfolio of James Dmaan', 4);

-- --------------------------------------------------------

--
-- Structure de la table `portfolios_books`
--

CREATE TABLE `portfolios_books` (
  `portfolio_bookId` int(11) NOT NULL,
  `bookId` int(11) NOT NULL,
  `portfolioId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `portfolios_books`
--

INSERT INTO `portfolios_books` (`portfolio_bookId`, `bookId`, `portfolioId`) VALUES
(24, 19, 13),
(25, 23, 13),
(26, 24, 13);

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
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`userId`, `name`, `surname`, `email`, `password`) VALUES
(2, 'Bastien', 'Girardet', 'bastien.girardet@gmail.com', '712985CC1194DFFE8B30127444E0C92FE214420A84A5B2D28ABE6684F4540409'),
(3, 'Bastien', 'Girardet', 'bastien.girardet@student.unisg.ch', '712985CC1194DFFE8B30127444E0C92FE214420A84A5B2D28ABE6684F4540409'),
(4, 'James', 'Damian', 'James.damian@unisg.ch', '712985CC1194DFFE8B30127444E0C92FE214420A84A5B2D28ABE6684F4540409'),
(5, 'John', 'Doe', 'John.doe@johndoe.com', '712985CC1194DFFE8B30127444E0C92FE214420A84A5B2D28ABE6684F4540409'),
(6, 'Deborah', 'De Wolff', 'deborah.dewolffdemoorsel@student.unisg.ch', '712985CC1194DFFE8B30127444E0C92FE214420A84A5B2D28ABE6684F4540409');

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

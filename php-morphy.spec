%define		pkgname	morphy
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	phpMorphy is morphological analyzer library
Summary(ru.UTF-8):	Библиотека морфологического анализа
Name:		php-%{pkgname}
Version:	0.3.7
Release:	0.1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	http://downloads.sourceforge.net/phpmorphy/phpmorphy-%{version}.zip
# Source0-md5:	003aa905cd1d39144e31149747fe1ea7
URL:		http://phpmorphy.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	php-common >= 4:%{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir			%{php_data_dir}/%{pkgname}

# _phpdocdir / php_docdir / phpdoc_dir ?
%define		_phpdocdir		%{_docdir}/phpdoc

# bad depsolver
%define		_noautopear	pear

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
phpMorphy is morphological analyzer library written in pure PHP.
Currently supports Russian, English and German languages.

%description -l ru.UTF-8
phpMorphy позволяет решать следующие задачи:
- Лемматизация (получение нормальной формы слова)
- Получение всех форм слова
- Получение грамматической информации для слова (часть речи, падеж,
  спряжение и т.д.)
- Изменение формы слова в соответствии с заданными грамматическими
  характеристиками
- Изменение формы слова по заданному образцу
- Поддерживаемые языки: Русский, Английский, Немецкий (AOT).
  Украинский, Эстонский (на основе ispell). Есть возможность добавить
  поддержку других языков при помощи myspell словаря.

%prep
%setup -q -n phpmorphy-%{version}
%undos AUTHORS CHANGES INSTALL README 
%undos -f php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a src/* $RPM_BUILD_ROOT%{_appdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES INSTALL README 
%{_appdir}
%{_examplesdir}/%{name}-%{version}

%define debug_package %{nil}

%define oname %(echo %name | tr - _)

Summary:	Download,update, and run the Tor Browser Bundle
Name:		torbrowser-launcher
Version:	0.3.7
Release:	3
License:	MIT
Group:		Networking/WWW
Url:		https://www.github.com/micahflee/torbrowser-launcher
Source0:	https://github.com/micahflee/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	gettext
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(distro)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	%{_lib}appstream-glib8

#BuildRequires:	python%{pyver}dist(gpg)
#BuildRequires:	python%{pyver}dist(packaging)
#BuildRequires:	python%{pyver}dist(pyside6)
#BuildRequires:	python%{pyver}dist(pysocks)
#BuildRequires:	python%{pyver}dist(requests)
Requires:	gnupg2
Requires:	tor

ExclusiveArch: %{ix86} %{x86_64}

%patchlist
# (upstream) https://gitlab.torproject.org/tpo/applications/torbrowser-launcher/-/merge_requests/19?commit_id=35b3fbb27aea6b9fdbe0f245bd93c82d240af7a4
#https://gitlab.torproject.org/tpo/applications/torbrowser-launcher/-/merge_requests/19.patch

%description
Tor Browser Launcher is intended to make the Tor Browser Bundle (TBB) easier
to maintain and use for GNU/Linux users. You install torbrowser-launcher
from your distribution's package manager and it handles downloading the most
recent version of TBB for you, in your language and for your architecture. 

It also adds a "Tor Browser" application launcher to your operating system's
menu, and lets you set Tor Browser as your default web browser. When you
first launch Tor Browser Launcher, it will download TBB from
https://www.torproject.org/, extract it in your home directory, and execute
it. When you run it after that it will just execute TBB. When you open Tor
Browser after an update, it will download the newer version of TBB for you
and extract it over your old TBB directory, so you will maintain your TBB
bookmarks and always be running the latest version.

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_sysconfdir}/apparmor.d/*
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/torbrowser.png
%{_metainfodir}/*.metainfo.xml
%{py_puresitedir}/%{oname}-%{version}-py%{python3_version}.egg-info
%{py_puresitedir}/%{oname}/*

#----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%py_build

%install
%py_install
 
# locales
%find_lang %{name}


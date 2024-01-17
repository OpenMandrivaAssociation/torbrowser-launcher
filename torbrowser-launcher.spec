%define debug_package %{nil}

%define oname %(echo %name | tr - _)

Summary:	Download,update, and run the Tor Browser Bundle
Name:		torbrowser-launcher
Version:	0.3.6
Release:	1
Url:		https://www.github.com/micahflee/torbrowser-launcher
Source0:	https://github.com/micahflee/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
License:	MIT
Group:		Networking/WWW
	
BuildRequires:	gettext
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(distro)
BuildRequires:	%{_lib}appstream-glib8
	
Requires:	gnupg2
Requires:	tor

ExclusiveArch: %{ix86} %{x86_64}

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
%autosetup

%build
%py_build

%install
%py_install
 
# locales
%find_lang %{name}


%define debug_package %{nil}

%define oname %(echo %name | tr - _)

Summary:	Download,update, and run the Tor Browser Bundle
Name:		torbrowser-launcher
Version:	0.3.3
Release:	1
Url:		https://www.github.com/micahflee/torbrowser-launcher
Source0:	https://github.com/micahflee/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
License:	MIT
Group:		Networking/WWW
	
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(distro)
BuildRequires:	%{_lib}appstream-glib8
	
Requires:	python3
Requires:	gnupg2
Requires:	python-qt5
Requires:	python3dist(gpg)
Requires:	python3dist(pysocks)
Requires:	python3dist(packaging)
Requires:	python3dist(requests)
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
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/torbrowser.png
%{_metainfodir}/torbrowser.appdata.xml
%{py3_puresitedir}/%{oname}-%{version}-py%{python3_version}.egg-info
%{py3_puresitedir}/%{oname}/*
%{_sysconfdir}/apparmor.d/*

%prep
%autosetup

# fix distro name
sed -i -e 's|import platform|import distro|' \
       -e 's|platform.dist|distro.linux_distribution|g' \
	setup.py

# fix gnupg: gpg2 binary is gpg
sed -i "s|gpg2|gpg|g" torbrowser_launcher/common.py

%build
%py3_build

%install
%py3_install

# appdata
install -pm 0755 -d %{buildroot}%{_datadir}/appdata/
install -pm 0644 share/metainfo/*.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

# .desktop files
desktop-file-validate share/applications/torbrowser.desktop
desktop-file-validate share/applications/torbrowser-settings.desktop
 
# locales
%find_lang %{name}

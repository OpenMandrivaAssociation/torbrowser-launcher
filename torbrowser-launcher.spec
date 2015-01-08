%define name torbrowser-launcher
%define version 0.1.7
%define release 2
%define oname torbrowser_launcher

Summary:	Download,update, and run the Tor Browser Bundle
Name:		%{name}
Version:	%{version}
Release:	%{release}
Url:		https://www.github.com/micahflee/torbrowser-launcher
Source0:	https://github.com/micahflee/torbrowser-launcher/archive/v0.1.7.tar.gz
License:	MIT
Group:		Networking/WWW
BuildArch:	noarch

BuildRequires: pkgconfig(python)
BuildRequires: pythonegg(psutil)
BuildRequires: pythonegg(twisted)
BuildRequires: wmctrl 
BuildRequires: gnupg 
BuildRequires: fakeroot

Requires: pythonegg(psutil)
Requires: pythonegg(twisted)
Requires: wmctrl 
Requires: pythonegg(service-identity)
Requires: pythonegg(txsocksx)
Requires: pythonegg(parsley)
Requires: pythonegg(pyliblzma)


%description
Tor Browser Launcher is intended to make the 
Tor Browser Bundle (TBB) easier to maintain 
and use for GNU/Linux users. 
You install torbrowser-launcher from your 
distribution's package manager and it handles 
downloading the most recent 
version of TBB for you, in your 
language and for your architecture. 
It also adds a "Tor Browser" 
application launcher to your 
operating system's menu, and 
lets you set Tor Browser as your 
default web browser.
When you first launch Tor Browser Launcher, 
it will download TBB from https://www.torproject.org/, 
extract it in your home directory, and execute it. 
When you run it after that it will just execute TBB. 
When you open Tor Browser after an update, 
it will download the newer version of TBB 
for you and extract it over your old TBB 
directory, so you will maintain your TBB 
bookmarks and always be running the latest version.


%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}


%files 
%doc LICENSE README.md
%{_bindir}/%{name}
%{py_puresitedir}/%{oname}-%{version}-*.egg-info
%{py_puresitedir}/%{oname}/
%{_datadir}/appdata/torbrowser.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.xpm
%{_datadir}/%{name}
%{_sysconfdir}/apparmor.d/*


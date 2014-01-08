Summary:	Front end for controlling remote desktop sessions
Name:		winswitch
Version:	0.12.20
Release:	0.8
License:	GPL v3
Group:		Networking
#Source0:	http://winswitch.org/src/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	b2814b2fd6274408ff9820d8fb519a85
URL:		http://winswitch.org/
BuildRequires:	python
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.672
BuildRequires:	sed >= 4.0

Requires:	avahi
Requires:	avahi-ui

Requires:	gstreamer

#Requires:	gnome-python2-rsvg
#Requires:	nautilus-python
Requires:	python-utmp

Requires:	python-Crypto
Requires:	python-PIL
Requires:	python-TwistedConch
Requires:	python-TwistedCore
#Requires:	python-ctypes
#Requires:	python-hashlib
Requires:	python-pygtk-gtk
#Requires:	python-uuid
#Requires:	python-xlib

Requires:	python

Requires:	python-pyasn1

#Requires:	xorg-x11-server-utils

Requires:	openssh-clients
#Requires:	tigervnc-server >= 1.0.90
Requires:	xpra >= 0.7
Suggests:	nx
Suggests:	rdesktop

Suggests:	ImageMagick
Suggests:	dbus-x11
#Suggests:	devilspie
Suggests:	gnome-menus
#Suggests:	gnome-python2
Suggests:	tigervnc
Suggests:	xfreerdp
#Suggests:	xloadimage

Obsoletes:	shifter
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_prefix}/lib

%define		_noautoreq_java ClassDataVersion

%description
Start and control remote GUI sessions via xpra, NX, VNC, RDP or plain
ssh X11 forwarding. You can start, suspend, resume and send supported
sessions to other clients.

%prep
%setup -q

# TODO: bashism:
# skel/libexec/winswitch/firewall
# skel/libexec/winswitch/kill_parent

grep -rl '/usr/bin/env python' winswitch skel | xargs %{__sed} -i -e '1s,^#!.*python,#!%{__python},'

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

# nautilus 2.x (no gnome 2 in pld)
rm $RPM_BUILD_ROOT%{_libexecdir}/nautilus/extensions-2.0/python/nautilus_winswitch.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%dir %{_sysconfdir}/winswitch
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/winswitch/firewall
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/winswitch/ports.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/winswitch/server_defaults.conf
%attr(755,root,root) %{_bindir}/wcw
%attr(755,root,root) %{_bindir}/winswitch_applet
%attr(755,root,root) %{_bindir}/winswitch_away
%attr(755,root,root) %{_bindir}/winswitch_back
%attr(755,root,root) %{_bindir}/winswitch_client
%attr(755,root,root) %{_bindir}/winswitch_command_wrapper
%attr(755,root,root) %{_bindir}/winswitch_open_remotely
%attr(755,root,root) %{_bindir}/winswitch_server
%attr(755,root,root) %{_bindir}/winswitch_ssh_Xnest
%attr(755,root,root) %{_bindir}/winswitch_ssh_session
%attr(755,root,root) %{_bindir}/winswitch_stdio_socket
%attr(755,root,root) %{_bindir}/winswitch_stdio_tcp
%{_mandir}/man1/wcw.1*
%{_mandir}/man1/winswitch_*.1*
%{_desktopdir}/winswitch.desktop
%{_iconsdir}/hicolor/*/apps/winswitch*.png
%{_iconsdir}/winswitch_applet.png
%{_datadir}/mime/packages/winswitch.xml

%{_datadir}/winswitch
%{py_sitescriptdir}/winswitch
%{py_sitescriptdir}/winswitch-%{version}-py*.egg-info

%dir %{_libexecdir}/winswitch
%dir %{_libexecdir}/winswitch/bin-override
%attr(755,root,root) %{_libexecdir}/winswitch/bin-override/xdg-open
%attr(755,root,root) %{_libexecdir}/winswitch/delayed_start
%attr(755,root,root) %{_libexecdir}/winswitch/firewall
%attr(755,root,root) %{_libexecdir}/winswitch/gst_capture
%attr(755,root,root) %{_libexecdir}/winswitch/gst_playback
%attr(755,root,root) %{_libexecdir}/winswitch/kill_parent
%attr(755,root,root) %{_libexecdir}/winswitch/mime_open
%attr(755,root,root) %{_libexecdir}/winswitch/server_monitor
%attr(755,root,root) %{_libexecdir}/winswitch/server_portinfo
%attr(755,root,root) %{_libexecdir}/winswitch/virt_server_daemonizer

# thunar
%{_datadir}/Thunar/sendto/thunar-winswitch.desktop

# Vash - https://github.com/thevash/vash
# .jar to make screenshots
# TODO: package as java-vash and suggest it
%{_datadir}/Vash

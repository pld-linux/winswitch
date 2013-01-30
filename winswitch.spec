%define VERSION 0.12.18


# Basic groups of dependencies (platform specific overrides below)
%define xorg_utils xorg-x11-server-utils
%define python_base pygtk2, python-crypto, python-twisted, python-imaging, python-xlib
%define python_extras nautilus-python, dbus-python
%define proto_deps xpra >= 0.3, nx, rdesktop, openssh-clients, tigervnc, tigervnc-server >= 1.0.90
%define mdns avahi
%define gstreamer gstreamer
%define pyasn1 python-pyasn1
%define xorg_extras dbus-x11, xloadimage, devilspie, ImageMagick
%define recommends_base gnome-menus, gnome-python2, xfreerdp
%define python_extras nautilus-python, python-utmp, gnome-python2-rsvg
%define mdns avahi avahi-ui-tools

%define recommends %{recommends_base}, %{xorg_extras}

%define proto_deps xpra, nx, rdesktop, openssh-clients
%define recommends %{recommends_base}, tigervnc
%define nautilus_lib /usr/lib/nautilus
%define mdns avahi avahi-tools

%define python_base_deps %{python_base}, python-uuid, python-ctypes, python-hashlib

Summary:	Front end for controlling remote desktop sessions
Name:		winswitch
Version:	%{VERSION}
Release:	0.1
License:	GPL3
Group:		Networking
URL:		http://winswitch.org/
Requires:	%{gstreamer}
Requires:	%{mdns}
Requires:	%{proto_deps}
Requires:	%{pyasn1}
Requires:	%{python_base_deps}
Requires:	%{python_extras}
Requires:	%{xorg_utils}
Requires:	python
Suggests:	%{recommends}
Source0:	http://winswitch.org/src/%{name}-0.12.16.src.tar.bz2
BuildRequires:	python
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	setuptool
Obsoletes:	shifter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Start and control remote GUI sessions via xpra, NX, VNC, RDP or plain
ssh X11 forwarding. You can start, suspend, resume and send supported
sessions to other clients.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%if 0
%attr(755,root,root) %{_bindir}/winswitch_*
%attr(755,root,root) %{_bindir}/wcw
%{_prefix}/lib*/python*/*packages/winswitch*
%{_libexecdir}/winswitch
%{_sysconfdir}/winswitch
%{_datadir}/winswitch
%{_desktopdir}/winswitch.desktop
%{_iconsdir}
%{_datadir}/mime
%{_mandir}
%{_datadir}/Thunar
%{_datadir}/Vash
#%{nautilus_lib}/extensions-2.0/python/nautilus_winswitch.*
%endif

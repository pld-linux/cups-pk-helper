Summary:	PolicyKit helper to configure cups with fine-grained privileges
Name:		cups-pk-helper
Version:	0.2.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.freedesktop.org/software/cups-pk-helper/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	26dc2db9566804930a7f1dad37ac4a78
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	cups-devel
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gnome-common
BuildRequires:	intltool >= 0.40.6
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.97
Requires:	dbus
Requires:	glib2 >= 1:2.30.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cups-pk-helper is an application which makes cups configuration
interfaces available under control of PolicyKit.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README
%attr(755,root,root) %{_libdir}/cups-pk-helper-mechanism
%{_datadir}/dbus-1/system-services/org.opensuse.CupsPkHelper.Mechanism.service
%{_datadir}/polkit-1/actions/org.opensuse.cupspkhelper.mechanism.policy
/etc/dbus-1/system.d/org.opensuse.CupsPkHelper.Mechanism.conf
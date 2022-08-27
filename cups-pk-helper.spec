Summary:	PolicyKit helper to configure CUPS with fine-grained privileges
Summary(pl.UTF-8):	Program pomocniczy PolicyKit do konfiguracji CUPS-a z właściwymi uprawnieniami
Name:		cups-pk-helper
Version:	0.2.7
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://www.freedesktop.org/software/cups-pk-helper/releases/%{name}-%{version}.tar.xz
# Source0-md5:	0cdadec9ea8f88b7fc7af8ca206da2bd
BuildRequires:	cups-devel >= 1:1.6
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	meson >= 0.49.2
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.97
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	cups-lib >= 1:1.6
Requires:	dbus
Requires:	glib2 >= 1:2.36.0
Requires:	polkit >= 0.97
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cups-pk-helper is an application which makes cups configuration
interfaces available under control of PolicyKit.

%description -l pl.UTF-8
cups-pk-helper to aplikacja udostępniająca interfejsy konfiguracyjne
CUPS-a pod kontrolą usługi PolicyKit.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README
%attr(755,root,root) %{_libexecdir}/cups-pk-helper-mechanism
%{_datadir}/dbus-1/system-services/org.opensuse.CupsPkHelper.Mechanism.service
%{_datadir}/dbus-1/system.d/org.opensuse.CupsPkHelper.Mechanism.conf
%{_datadir}/polkit-1/actions/org.opensuse.cupspkhelper.mechanism.policy

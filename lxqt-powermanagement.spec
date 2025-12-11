#
# Conditional build:
#
%define		qtver		6.6.0

Summary:	Powermanagement daemon for LXQt desktop suite
Summary(pl.UTF-8):	Demon zarządzania energią dla środowiska graficznego LXQt
Name:		lxqt-powermanagement
Version:	2.3.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	https://github.com/lxqt/lxqt-powermanagement/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	21efb33bdbefdff6b9bd9332c49e5a28
URL:		http://www.lxqt.org/
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Svg-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	kf6-kidletime-devel >= 6.0.0
BuildRequires:	kf6-solid-devel >= 6.0.0
BuildRequires:	liblxqt-devel >= 2.3.0
BuildRequires:	libxcb-devel
BuildRequires:	lxqt-build-tools >= 2.3.0
BuildRequires:	lxqt-globalkeys-devel >= 2.3.0
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Powermanagement daemon for LXQt desktop suite.

%description -l pl.UTF-8
Demon zarządzania energią dla środowiska graficznego LXQt.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-config-powermanagement
%attr(755,root,root) %{_bindir}/lxqt-powermanagement
/etc/xdg/autostart/lxqt-powermanagement.desktop
%{_desktopdir}/lxqt-config-powermanagement.desktop
%{_iconsdir}/hicolor/scalable/devices/laptop-lid.svg
# required for the lang files
%dir %{_datadir}/lxqt/translations/lxqt-config-powermanagement
%dir %{_datadir}/lxqt/translations/lxqt-powermanagement

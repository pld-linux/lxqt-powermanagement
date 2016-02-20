#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-powermanagement
Name:		lxqt-powermanagement
Version:	0.10.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	e17763f5e7c2a9f8595a58209d51cb86
URL:		http://www.lxqt.org/
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.10.0
BuildRequires:	libqtxdg-devel >= 0.5.3
BuildRequires:	libxcb-devel
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-powermanagement.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../

%{__make}

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
%{_desktopdir}/lxqt-config-powermanagement.desktop
%{_iconsdir}/hicolor/scalable/devices/laptop-lid.svg
%dir %{_datadir}/lxqt/translations/lxqt-config-powermanagement
%dir %{_datadir}/lxqt/translations/lxqt-powermanagement
